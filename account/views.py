from django.shortcuts import render,redirect,HttpResponse, get_object_or_404

# Create your views here.
from django.http import request
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout 
from .forms import UserRegistrationForm,LoginForm,UserEditForm,ProfileEditForm
from django.contrib import auth, messages
from .models import UserProfile
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, Permission, User

def register(request):
    if request.user.is_authenticated:
        messages.success(request,"You already have logged-in in your current account.")
        return redirect('')
    elif request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid ():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            #Profile
            # Create the user profile
            fullname = f"{new_user.first_name} {new_user.last_name}"
            UserProfile.objects.create(user=new_user,full_name=fullname,email=new_user.email,)
             
            #Automate Logged in new Signup user
            login(request, new_user)
            return redirect("accounts:signup_done")
            #return render(request,'account/register_done.html',{'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,'account/register.html',{'user_form': user_form})






def user_login(request):
    if request.user.is_authenticated:
        msg = messages.success(request,"You Already have account.")
        return redirect('')
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                        username=cd['username'],
                                        password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('core:home')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


def user_logout(request):
    logout(request)
    # return HttpResponseRedirect(request,'log_out.html',context_instance = RequestContext(request))
    return redirect("accounts:login")
    
@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                data=request.POST)
        profile_form = ProfileEditForm(
                                    instance=request.user.userprofile,
                                    data=request.POST,
                                    files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated '\
                                    'successfully')
            return redirect('accounts:dashboard')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(
                                    instance=request.user.userprofile)
    return render(request,
                'account/edit.html',
                {'user_form': user_form,
                'profile_form': profile_form})






@login_required
def dashboard(request):
    return render(request,
                'account/dashboard.html')




@login_required
def user_profile_detail(request, pk):
    profile = get_object_or_404(UserProfile, pk=pk)
    context = {'profile':profile}
    return render(request,'account/profile-detail.html',context)
