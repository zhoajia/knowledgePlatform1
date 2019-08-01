from django.shortcuts import render
from django.contrib import auth
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse


# 登陆拦截
class LoginFilter(MiddlewareMixin):

    def process_request(self, request):
        if request.path == '/' or request.path == '/login' or request.path.startswith('/admin'):
            return
        if request.user.is_authenticated:  # 是否已登录
            print("一登录")
            return
        else:
            print("未登录")
            context = dict()
            context['errorMsg'] = '请先登陆'
            return HttpResponse(context['errorMsg']);

    def process_view(self, request, callback, callback_args, callback_kwargs):
        pass

    def process_exception(self, request, exception):
        pass

    def process_response(self, request, response):
        return response