"""knowledgePlatform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
"""

from django.conf.urls import url
from django.urls import include, path

from .login import login
from .Index import index
from .top_type import views as top_type
from django.contrib import admin

top_type_patterns = [
    path('create_top_type', top_type.create_top_type),  # 跳转注册页
]

urlpatterns = [
    path('', index.go_index),  # 登陆接口
    path('admin', admin.site.urls),  # 管理后台root/87908502
    path('login', login.do_login),  # 登陆接口
    path('register', login.register),  # 注册接口
    path('go_register', login.go_register),  # 跳转注册页
    path('top/',include(top_type_patterns))
]
