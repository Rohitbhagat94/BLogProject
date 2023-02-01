"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from myblog import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.show,name="show"),
    path('base',views.base),
    path('user',views.user,name="user"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
    # path('add',views.add,name="add"),
    path('search',views.search,name="search"),
    path('readmore<int:id>',views.readmore,name="readmore"),
    path('contactus',views.contactus1,name="contactus"),
    path('delete <int:id>',views.delete,name="delete"),
    path('profile',views.profileadd,name="profile"),
    path('pshow',views.pshow,name="pshow"),
    path('update <int:id>', views.update,name="update"),
    path('plus',views.Plus,name="plus"),
    path('change_password',views.change_password,name="change_password"),
    path('change_pic<int:id>',views.change_pic,name="change_pic")




]
