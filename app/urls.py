from django.urls import path,re_path
import json
from .views import *
from django.contrib.auth import login

urlpatterns = [



#path('login/', login,name="login"),
#path('sign_up',SignUp.as_view(), name="sign_up"),
path('cart',UserCartView.as_view(),name="cart"),
path('categories/',CategoryView.as_view(),name="category"),
path('categories/<str:categoryname>/',CategoryView.as_view(),name="category")

]