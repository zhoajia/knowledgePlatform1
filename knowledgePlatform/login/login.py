from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import auth


def go_login(request):
    return render(request, 'login.html')


def go_register(request):
    return render(request, 'register.html')


# 用户登陆
def do_login(request):
    request.encoding = 'utf-8'
    if 'user_name' in request.POST:
        print(request.POST['password'])
        try:
            if request.user.is_authenticated:  # 是否已登录
                return render(request, 'index.html')
            else:
                user = auth.authenticate(username=request.POST['user_name'], password=request.POST['password'])
                if user is not None:
                    auth.login(request,user)
                    return render(request, 'index.html')
                else:
                    context = dict()
                    context['errorMsg'] = '用户名或者密码错误'
                    return render(request, 'login.html', context)
        except Exception as e:
            print(e.__str__())
            context = dict()
            context['errorMsg'] = '系统异常'
            return render(request, 'login.html', context)


# 用户注册
def register(request):
    request.encoding = 'utf-8'
    if 'user_name' in request.POST and 'password' in request.POST:
        # 注册创建用户
        User.objects.create_user(request.POST['user_name'],None,request.POST['password'])
        return render(request, 'login.html')
    else:
        context = dict()
        context['errorMsg'] = '请输入用户名和密码'
        return render(request, 'register.html')