from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import auth

def go_login(request):
    return render(request, 'login.html')


def do_login(request):
    request.encoding = 'utf-8'
    if 'user_name' in request.POST:
        try:
            if request.user.is_authenticated():  # 是否已登录
                return render(request, 'index.html')
            else:
                user = auth.authenticate(username=request.POST['user_name'], password=request.POST['password'])
                if user is not None:
                    return render(request, 'index.html')
                else:
                    context = {}
                    context['errorMsg'] = '用户名或者密码错误'
                    return render(request, 'login.html',context)
        except Exception as e:
            print(e.__str__())
            context = {}
            context['errorMsg'] = '系统异常'
            return render(request, 'login.html', context)