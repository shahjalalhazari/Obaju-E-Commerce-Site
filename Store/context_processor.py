from .models import ForWhom, Category

def for_whom_context(request):
    return {
        'whoms': ForWhom.objects.all(),
    }