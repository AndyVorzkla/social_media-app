from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile


@login_required(login_url='core:signin')
def index(request):
    return render(request, 'core/index.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('core:signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('core:signup')
            else:
                user = User.objects.create_user(username=username,
                                                email=email,
                                                password=password, )
                user.save()

                # Log user in and redirect to settings page
                user = auth.authenticate(username=username, password=password)
                auth.login(request, user)
                # Create a profile object for the new user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('core:signup')
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('core:signup')
    else:
        return render(request, 'core/signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('core:index')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('core:signin')
    else:
        return render(request, 'core/signin.html')


@login_required(login_url='core:signin')
def logout(request):
    auth.logout(request)
    return redirect('core:signin')


@login_required(login_url='core:signin')
def settings(request):

    return render(request, 'core/setting.html')
