from rest_framework import serializers
from myshop.shop.models import Category, Brand, Item, Order


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name']

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'brand_name']


class ItemSerializer(serializers.ModelSerializer):
    item_category = CategorySerializer(read_only=True)
    item_brand = BrandSerializer(read_only=True)
    class Meta:
        model = Item
        fields = ['id', 'item_name', 'item_quantity',
                    'item_image', 'item_category', 'item_brand']
        depth = 1


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['id', 'order_user' ,'order_item']
