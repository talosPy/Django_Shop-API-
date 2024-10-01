from rest_framework import serializers
from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'popularity']  # Include fields you need



class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True, read_only=True)  # Use the serializer to get category names

    class Meta:
        model = Product
        fields = '__all__'  # Or specify the fields you want



''' fields = ['value','value','value'] is also an option! (only values that you have
                                                         in your model class) '''
