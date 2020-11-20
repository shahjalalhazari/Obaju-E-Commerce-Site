from django.shortcuts import render, redirect, HttpResponse, get_object_or_404, Http404
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import send_mail, BadHeaderError
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .models import User, Profile
from .forms import SignUpForm, CustomPasswordResetForm, ProfileForm
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


#PASSWORD RESET VIEW
def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = CustomPasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "Account/Password/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Obaju',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, '' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					messages.info(request, 'A message with reset password instructions has been sent to your inbox.')
					return redirect("store:home")
			messages.warning(request, 'An invalid email has been entered.')
	password_reset_form = CustomPasswordResetForm()
	return render(request=request, template_name="Account/Password/password_reset.html", context={"password_reset_form":password_reset_form})


#CUSTOMER PROFILE VIEW
@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)
    form = ProfileForm(instance=profile)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            form = ProfileForm(instance=profile)
            messages.success(request, 'Changed Saved!')
    return render(request, 'Account/profile.html', {'form': form})


#PASSWORD CHANGE VIEW
@login_required
def change_password(request):
    current_user = request.user
    form = PasswordChangeForm(current_user)
    if request.method == "POST":
        form = PasswordChangeForm(current_user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password Changed Successfully! Please log in.')
            return redirect("account:profile")
    return render(request, 'Account/change_password.html', {'form': form})