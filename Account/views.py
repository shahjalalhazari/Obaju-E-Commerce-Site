from django.shortcuts import render, redirect, HttpResponse, get_object_or_404, Http404
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import User, Profile
from .forms import SignUpForm
from .token import activation_token


#SIGNUP VIEW
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            site = get_current_site(request)
            subject = "Confirmation message to active your account."
            message = render_to_string("account/activation_mail.html", {
                "user": user,
                "domain": site.domain,
                "uid": user.id,
                "token": activation_token.make_token(user)
            })
            to_email = form.cleaned_data.get('email')
            to_email_list = [to_email]
            from_email = settings.EMAIL_HOST_USER
            send_mail(subject, message, from_email, to_email_list, fail_silently=True)
            return HttpResponse("<h2>Thanks for your registration. An activation mail was send to your account. Please active your account.</h2>")
    else:
        form = SignUpForm()
    return render(request, 'Account/signup.html', {'form':form})

#ACCOUNT ACTIVATION VIEW
def activate(request, uid, token):
    try:
        user = get_object_or_404(User, pk=uid)
    except:
        raise Http404("User Not Found!")
    if user is not None and activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Your account is activated. Now you can log in.")
        return redirect('account:login')
    else:
        messages.warning(request, "Invalid activation code.")
        return redirect("store:home")


#LOGIN VIEW
def login_page(request):
    return render(request, 'Account/login.html', {})

#USER LOGIN VIEW
def user_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You are logged in!")
            return redirect('store:home')
        else:
            messages.warning(request, "Invalid Email or Password")
            return redirect('account:login')


#LOGOUT VIEW
@login_required
def logout_user(request):
    logout(request)
    messages.warning(request, 'You are logged out!')
    return redirect('store:home')