from .models import *
from rest_framework import serializers,permissions,generics







class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')





class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('categoryname',)
class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('productname','price','categoryname',)
    def create(self,validated_data):
        categoryname = CategorySerializer()

'''class UserCartSerializer(serializers.Serializer):

    products = ProductsSerializer()

    quantity = serializers.IntegerField()
    class Meta:
        model = UserCart
        fields ='__all__'
    def create(self,validated_data):
        quantity = validated_data.pop("quantity")
        products = validated_data.pop("products")



        try:
            product = Products.objects.get(productname =products["productname"])
        except:
            product = Products.objects.create(**products)

        validated_data.update({"products":product,"quantity":quantity})
        return UserCart.objects.create(**validated_data)
'''






