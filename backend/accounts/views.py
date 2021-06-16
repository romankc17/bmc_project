from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth

# Create your views here.
def register(request):
    if request.method =='POST':
        global first_name
        global last_name
        global username
        global password1
        global email
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        


        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken ")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Taken ")
                return redirect('register')
            else:
                
                
                
                send_mail(
                    'Verify Your Account',
                    'Hey!'+first_name +' '+ 'your 6 digit verification code is ' +' '+ str(code),
                    'nepaleseboy80@gmail.com',
                    [email],
                    fail_silently= False
                    
                    

                 )
                
                
                return render (request,'verify_email.html')
        else :
            messages.info(request, "Password do not matched ")
            return redirect('register')

    else:
        return render(request,'register.html')
    
    return redirect('/')

def user_login(request):
    return render(request, 'accounts/user_login.html')

def staff_login(request):
    return render(request, 'accounts/staff_login.html')

def logout(request):
    
    auth.logout(request)
    return redirect('/')