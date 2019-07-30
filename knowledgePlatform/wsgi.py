"""
WSGI config for knowledgePlatform project.
作为你的项目的运行在 WSGI 兼容的Web服务器上的入口
It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'knowledgePlatform.settings')

application = get_wsgi_application()
