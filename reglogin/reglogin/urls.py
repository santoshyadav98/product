"""
URL configuration for reglogin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from smart import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('smart/',views.home.as_view()),
    path('smart/productinput',views.productinput.as_view()),
    path('smart/insert',views.Insert.as_view()),
    path('smart/display',views.displayview.as_view()),
    path('smart/delete',views.deletinput.as_view()),
    path('smart/deleteview',views.deleteview.as_view()),
    path('smart/updateinput',views.UpdateInput.as_view()),
    path('smart/updatedetails',views.UpdateDetails.as_view()),
    path('smart/update',views.Update.as_view()),
    path('smart/product',views.displayview.as_view()),
    
]
