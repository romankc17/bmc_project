from django.contrib import admin
from .models import UserProfile,VerificationImage

admin.site.register([UserProfile,VerificationImage])
