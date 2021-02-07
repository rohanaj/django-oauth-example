from rest_framework import status
from django.shortcuts import render
from django.contrib.auth import login,authenticate
from django.http import JsonResponse
from .models import *
from .serializers import *
# Create your views here.
from rest_framework.response import Response
from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse
from rest_framework import generics
from .permissions import IsAuthenticatedOrCreate
from rest_framework.views import APIView
from django.shortcuts import render, redirect, get_object_or_404,get_list_or_404
from rest_framework import status
from rest_framework.response import Response


#class SignUp(generics.CreateAPIView):
#    queryset = User.objects.all()
#    serializer_class = SignUpSerializer
#    permission_classes = (IsAuthenticatedOrCreate,)
class CategoryView(ProtectedResourceView,APIView):
    def get(self,request):
        category = Category.objects.all()
        categoryser = CategorySerializer(category,many=True)
        listcat = []
        for i in categoryser.data:
            listcat.append(i["categoryname"])

        return Response({"categorylist":listcat})
    def post(self,request):
        data = request.data
        categoryvalue = data.get("categoryname")
        categorydict = {"categoryname":str(categoryvalue)}
        cser=CategorySerializer(data=categorydict)
        cser.is_valid(raise_exception=True)
        cser.save()
        return Response(cser.data, status=status.HTTP_201_CREATED)

    def delete(self,request,categoryname):
        data = request.data
        categoryvalue = categoryname
        category = get_list_or_404(Category,categoryname=categoryvalue)
        for i in category:
            i.delete()
        return Response({"message": "Category Name {} is deleted ".format(categoryvalue)})



class UserCartView(ProtectedResourceView,APIView):
    def get(self,request):
        cart = get_object_or_404(UserCart,user=request.user)
        productname = cart.productname
        p = get_object_or_404(Products,productname=productname)
        productname = p.productname
        price = p.price
        category = p.categoryname
        c = get_object_or_404(Category,categoryname=category)
        categoryname = c.categoryname
        quantity = cart.quantity
        return JsonResponse({"productname":productname,"quantity":quantity,"price":price,"categoryname":categoryname})
    def post(self,request):
        datacart = request.data

        productname = datacart.get("productname")
        quantity = datacart.get("quantity")
        #product = Products.objects.filter(productname=productname)

        serializer = UserCartSerializer(data=datacart)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)



