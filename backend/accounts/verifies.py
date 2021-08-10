from django.contrib import messages
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
            user.is_active = True
            user.userprofile.email_confirmed = True
            user.save()
            user.userprofile.save()
            auth_login(request, user)
            messages.success(request, ('Your account have been confirmed.'))
            return redirect('home')
        else:
            messages.warning(request, ('The confirmation link was invalid, possibly because it has already been used.'))
            return redirect('home')
        

