from django.urls import path
#from rest_framework.urlpatterns import format_suffix_patterns
from myshop.shop import views

urlpatterns = [
    path('brands/', views.BrandList.as_view()),
    path('items/', views.ItemList.as_view()),
    path('orders/', views.OrderList.as_view()),
    path('brands/<int:pk>/', views.BrandDetail.as_view()),
    path('items/<int:pk>/', views.ItemDetail.as_view()),
]


#urlpatterns = format_suffix_patterns(urlpatterns)
