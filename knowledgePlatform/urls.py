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
from .sub_type import views as sub_type
from .repository import views as repository
from .webservice import views as webservice
from .log_info import views as logInfo
from .User import views as user
from .kpermissions import views as permission
from .krole import views as role
from django.contrib import admin

top_type_patterns = [
    path('create_top_type', top_type.create_top_type),  # 创建top_type
    path('update_top_type', top_type.update_top_type),  # 修改top_type
    path('top_type_list', top_type.findall_top_type),  # 查询所有的top_type
]

sub_type_patterns = [
    path('sub_type_list', sub_type.find_all_active_sub_type),  # 查询所有的sub_type
]

repository_patterns = [
    path('go_repository', repository.go_repository),  # 跳转至repository页面
    path('repository_list', repository.get_all_repository_for_webservice),  # 获取repository列表
    path('repository_create', repository.repository_create),  # 获取repository列表
]

webservice_patterns = [
    path('go_webservice', webservice.go_webservice),  # 跳转至webservice页面
    path('webservice_list', webservice.get_all_webservice),  # 获取webservice列表
    path('webservice_info', webservice.get_webservice_info),  # 获取webservice
    path('webservice_create', webservice.webservice_create),  # 创建webservice
    path('webservice_update', webservice.webservice_update),  # 修改webservice
]

user_patterns = [
    path('go_user_list', user.go_user_list),  # 跳转至user管理页面
    path('get_user_list', user.get_user_list),  # 跳转至user管理页面
]

log_patterns = [
    path('log_list', logInfo.get_top_log),  # 获取loginfo列表
]

permission_patterns = [
    path('go_permission', permission.go_permission_list),  # 获取权限列表
    path('go_role_list', role.go_role_list),  # 获取角色列表
    path('get_role_list', role.get_role_list),  # 获取角色列表
    path('get_user_by_role_id', role.get_user_by_role_id),  # 获取角色列表
    path('create_role', role.create_role),  # 创建角色列表
    path('get_permission_list', permission.get_permission_list),  # 获取权限列表
    path('permission_create', permission.permission_create),  # 创建权限列表
    path('load_permission_tree', permission.load_permission_tree),  # 获取权限列表（树形加载）
    path('get_permissions_by_role_id', role.get_permissions_by_role_id),  # 获取角色已配置权限列表
]

urlpatterns = [
    path('', index.go_index),  # 登陆接口
    path('admin', admin.site.urls),  # 管理后台root/87908502
    path('login', login.do_login),  # 登陆接口
    path('register', login.register),  # 注册接口
    path('go_register', login.go_register),  # 跳转注册页
    path('go_search', index.go_search),  # 跳转注册页
    path('top/', include(top_type_patterns)),
    path('sub/', include(sub_type_patterns)),
    path('repository/', include(repository_patterns)),
    path('webservice/', include(webservice_patterns)),
    path('log_info/', include(log_patterns)),
    path('user/', include(user_patterns)),  # 用户管理页
    path('permission/', include(permission_patterns)),  # 用户管理页
]
