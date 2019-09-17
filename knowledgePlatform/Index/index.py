from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render


# 跳转值登陆页
def go_index(request):
    return render(request,'login.html')


# 跳转搜索页
def go_search(request):
    return render(request,'search.html')