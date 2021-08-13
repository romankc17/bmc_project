from django.contrib import admin
from .models import UserProfile,VerificationImage
from django.contrib.auth.models import Group,User

admin.site.unregister((Group,User))

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username','name','email','batch','roll_no','sec',)
    list_filter = ('batch','sec',)
    
    def username(self,obj):
        return obj.user.username
    
    def email(self,obj):
        return obj.user.email
    
    
    # def has_change_permission(self, request, obj=None):
    #     return obj is None or obj.user == request.user
    
    def get_readonly_fields(self, request, obj=None):
        if obj.user != request.user:
            return ['user','name','roll_no','sec','permanent_address',
                    'temporary_address','batch','image']
        
        if obj:
            return ['user']
        return self.readonly_fields
    
    def has_add_permission(self, request):
        return False

@admin.action(description='Verify selected Users')
def verify(modeladmin, request, queryset):
    for obj in queryset:
        obj.user.is_active = True
        obj.user.save()

@admin.register(VerificationImage)
class VerificationImageAdmin(admin.ModelAdmin):
    list_display =('user','name','batch','roll_no','image')
    actions = [verify]
    
    def name(self,obj):
        return obj.user.userprofile.name
    
    def batch(self,obj):
        return obj.user.userprofile.batch
    
    def roll_no(self,obj):
        return obj.user.userprofile.roll_no
    
    def get_queryset(self, request):
        qs = super(VerificationImageAdmin, self).get_queryset(request)
        
        return qs.filter(user__is_active=False)
    
    def has_add_permission(self, request):
        return False
    
    