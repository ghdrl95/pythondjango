'''
Created on 2018. 10. 28.

@author: user
'''
from django.urls import path
from .views import signup ,signin, signout

app_name ='customlogin'

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('signout/', signout, name='signout')
    ]