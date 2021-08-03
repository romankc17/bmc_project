from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib import messages
from .forms import ExtendedUserCreationForm, UserProfileForm, VerificationImageForm
import nepali_datetime
from .verifies import send_mail


# Create your views here.
def register(request):
    user_form = ExtendedUserCreationForm()
    profile_form = UserProfileForm()
    verification_image_form = VerificationImageForm()
        
    nepali_current_year = nepali_datetime.datetime.now().year
    
    if request.method == 'POST':
        user_form = ExtendedUserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        verification_image_form = VerificationImageForm(request.POST, request.FILES)
        
        if user_form.is_valid() and profile_form.is_valid() and verification_image_form.is_valid():
            try:
                user = user_form.save(commit=False)

                profile = profile_form.save(commit=False)
                
                roll_no = profile_form.cleaned_data['roll_no']
                if len(str(roll_no).strip())==1:
                    roll_no = int('0'+str(roll_no).strip())
                profile.roll_no = roll_no
                
                user.username = f'{profile.batch}-{profile.roll_no}'
                user.is_active = False
                
                try:
                    user.save()
                except Exception as e:
                    messages.error(request, "Already SignUped with this roll number and batch")
                    context = {
                        'user_form': user_form, 
                        'profile_form': profile_form,
                        'verification_image_form': verification_image_form,
                        'nepali_current_year':nepali_current_year
                    }

                    return render(request, 'accounts/register.html', context)
                
                profile.user = user
                profile.save()
                
                verification_image = verification_image_form.save(commit=False)
                verification_image.user = user
                verification_image.save()
                
                try:
                    send_mail(user) 
                except Exception as e:  
                    messages.error(request, "Sending verification mail failed")
                
                messages.success(request, f"YOUR USERNAME IS '{user.username}'")
                return redirect('login')
            
            except Exception as e:
                messages.error(request, "Something went wrong. Please try again!")
        else:
            messages.error(request, "Invalid form")

    context = {
        'user_form': user_form, 
        'profile_form': profile_form,
        'verification_image_form': verification_image_form,
        'nepali_current_year':nepali_current_year
    }

    return render(request, 'accounts/register.html', context)



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            print(user)
            return redirect("/")
        else:
            messages.error(request, "username or password not correct")

            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

