from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.ProductListView.as_view(),name='product_list'),
    path('<int:pk>/', views.ProductDetailView.as_view(),name='product_detail'),
    path('create/', views.ProductCreateView.as_view(),name='product_create'), 
    path('update/<int:pk>/', views.ProductUpdateView.as_view(),name='product_update'), 
    path('delete/<int:pk>/', views.ProductDeleteView.as_view(),name='product_delete'), 
] 
