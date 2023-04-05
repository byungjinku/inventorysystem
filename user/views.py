from .models import UserModel
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib import auth

# Create your views here.

def sign_up_view(request):
    if request.method == 'GET':
        return render(request, 'account/signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)

        if password != password2:
            return render(request, 'account/signup.html')
        else:
            exist_user = get_user_model().objects.filter(username=username)
            if exist_user:
                return render(request, 'account/signup.html')  # 사용자가 존재하기 때문에 사용자를 저장하지 않고 회원가입 페이지를 다시 띄움
            else:
                UserModel.objects.create_user(username=username, password=password)
                return redirect('/sign-in')

def sign_in_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        me = auth.authenticate(request, username=username, password=password)
        if me is not None:  
            auth.login(request, me)
            return HttpResponse(me.username)
        else:
            return redirect('/login')
    elif request.method == 'GET':
        return render(request, 'account/signin.html')