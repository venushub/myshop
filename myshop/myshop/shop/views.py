from django.shortcuts import render

# Create your views here.
from myshop.shop.models import Category, Brand, Item, Order
from myshop.shop.serializers import BrandSerializer, ItemSerializer, OrderSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from myshop.shop.permissions import UserAccessPermission, AdminOrReadOnly
#from .mailer import Mailer

class BrandList(APIView):
    permission_classes = [permissions.IsAuthenticated, AdminOrReadOnly]

    def get(self, request):
        brands = Brand.objects.all()
        serializer = BrandSerializer(brands, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemList(APIView):
    permission_classes = [permissions.IsAuthenticated, AdminOrReadOnly]

    def get(self, request):
        items = Item.objects.select_related('item_brand', 'item_category').all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        if Category.objects.filter(id=request.data['item_category']).exists():
            category = Category.objects.get(id=request.data['item_category'])
        else:
            return Response({"No Object" : "Invalid Entry for Category"}, status=status.HTTP_400_BAD_REQUEST)

        if Brand.objects.filter(id=request.data['item_brand']).exists():
            brand = Brand.objects.get(id=request.data['item_brand'])
        else:
            return Response({"No Object" : "Invalid Entry for Brand"}, status=status.HTTP_400_BAD_REQUEST)

        item = Item(item_category=category, item_brand=brand)
        print(request.data)
        serializer = ItemSerializer(item, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class OrderList(APIView):
    permission_classes = [permissions.IsAuthenticated, UserAccessPermission]

    # def get(self, request):
    #     orders = Order.objects.all()
    #     serializer = OrderSerializer(orders, many=True)
    #     return Response(serializer.data)

    def post(self, request):

        user = self.request.user

        if Item.objects.filter(id=request.data['order_item']).exists():
            item = Item.objects.get(id=request.data['order_item'])
            if item.item_quantity > 0:
                item.quantity = item.item_quantity - 1
            else:
                return Response({"Error" : "No Items in store"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"No Object" : "Invalid Entry for Item"}, status=status.HTTP_400_BAD_REQUEST)

        order = Order(order_user = user,order_item = item)
        serializer = OrderSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            item.save()
            serializer.save()
            # mail = Mailer()
            # mail.send_messages(subject='Order Placed!!',
            #                    template='emails/order_placed.html',
            #                    context={'customer': self},
            #                    to_emails=[self.user.email])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def perform_create(self, serializer):
    #     serializer.save(order_user=self.request.user)


class BrandDetail(APIView):
    permission_classes = [permissions.IsAuthenticated, AdminOrReadOnly]

    def get_object(self, pk):
        try:
            return Brand.objects.get(pk=pk)
        except Brand.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        brand = self.get_object(pk)
        serializer = BrandSerializer(brand)
        return Response(serializer.data)

    def put(self, request, pk):
        brand = self.get_object(pk)
        serializer = BrandSerializer(brand, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        brand = self.get_object(pk)
        brand.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ItemDetail(APIView):
    permission_classes = [permissions.IsAuthenticated, AdminOrReadOnly]

    def get_object(self, pk):
        try:
            return Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        item = self.get_object(pk)
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    def put(self, request, pk):
        item = self.get_object(pk)
        serializer = ItemSerializer(item, data=request.data, partial=True)
        print(item, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        item = self.get_object(pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
