from django.shortcuts import render
from django.core.mail import send_mail
from Emailproject.settings import EMAIL_HOST_USER

# Create your views here.

def Index(request):
    template_name = 'app1/form.html'
    if request.method == 'POST':
        sub = request.POST.get('subject')
        msg = request.POST.get('message')
        email = request.POST.get('email')

        send_mail(
            sub, msg, EMAIL_HOST_USER, [email]
        )
    return render(request, template_name)
