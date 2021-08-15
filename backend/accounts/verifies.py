from django.contrib import messages
from django.contrib.auth.backends import UserModel
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import redirect
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.contrib.auth import login as auth_login
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.views.generic import View

from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

from .tokens import account_activation_token


import threading

# class EmailThread(threading.Thread):
#     def __init__(self, subject, message, user):
#         self.subject = subject
#         self.message = message
#         self.user = user
#         threading.Thread.__init__(self)

#     def run (self):
#         self.user.email_user(self.subject, self.message)

# def send_mail(request,user):
#     current_site = get_current_site(request)
#     subject = 'Activate Your CSIT Association of BMC Account'
#     message = render_to_string('accounts/emails/account_activation_email.html', {
#     'user': user,
#     'domain': current_site.domain,
#     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#     'token': account_activation_token.make_token(user),
#     })
    
#     EmailThread(subject, message, user).start()

def send_mail(request,user):
    current_site = get_current_site(request)
    subject = 'Activate Your CSIT Association of BMC Account'
    message = render_to_string('accounts/emails/account_activation_email.html', {
    'user': user,
    'domain': current_site.domain,
    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
    'token': account_activation_token.make_token(user),
    })
    user.email_user(subject, message)

    messages.success(request, ('Please Confirm your email to complete registration.'))
    
            
class ActivateAccount(View):

    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.userprofile.email_confirmed = True
            user.save()
            user.userprofile.save()
            auth_login(request, user)
            messages.success(request, ('Your account have been confirmed.'))
        else:
            messages.warning(request, ('The confirmation link was invalid, possibly because it has already been used.'))
        return redirect('home')
        

def password_reset_request(request):
    current_site = get_current_site(request)
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            
            print(associated_users)
            
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "accounts/password_reset_email.txt"
                    c = {
                        "email":user.email,
                        'domain':current_site.domain,
                        'site_name': 'CSIT Association of BMC',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    message = render_to_string(email_template_name, c)
                    try:
                        # send_mail(
                        #     subject, 
                        #     message, 
                        #     'roman.kc.17@gmail.com' , 
                        #     [user.email], 
                        #     fail_silently=False
                        # )
                        user.email_user(subject, message)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect ("password_reset_done")
            else:
                messages.warning(request, ('No user is associated with this email address'))
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="accounts/password_reset.html", context={"form":password_reset_form})