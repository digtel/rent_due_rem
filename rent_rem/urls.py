from django import urls
from  django.urls import path
from . import views

urlpatterns = [
    path('',views.indexx,name='home'),
    # path('signup',views.signup,name='signu'),
    # path('generic',views.generic,name='generic'),
    # path('generic',views.generic,name='generic')
    # path('<home>',views.index,name='index'),
    
]