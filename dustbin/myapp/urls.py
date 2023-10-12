from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage, name='homepage'),
    path('login',views.login, name='login'),
    path('register',views.register, name='register'),
    path('logout',views.logout, name='logout'),
    path('results',views.results,name="results"),
    path('result1',views.result1,name="result1"),
    path('result2',views.result2,name="result2"),
    path('result3',views.result3,name="result3"),
]
