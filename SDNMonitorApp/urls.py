"""SDNMonitorApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required

from django_netjsongraph.api import urls as netjsongraph_api
from django_netjsongraph.visualizer import urls as netjsongraph_visualizer

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Appmonitorsite/', include('Appmonitor.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', login_required(TemplateView.as_view(template_name='home.html')), name='home'),

    url('map1/', include(netjsongraph_api)),
    url('map2/', include(netjsongraph_visualizer)),
    url('logs/', views.logs, name='logs'),
    url('topo_request', views.topology_request),
]
