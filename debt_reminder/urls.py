from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.CustomerListView.as_view(),name='customer_list'),
    path('<int:pk>/', views.CustomerDetailView.as_view(),name='customer_detail'),
    path('create/', views.CustomerCreateView.as_view(),name='customer_create'), 
    path('update/<int:pk>/', views.CustomerUpdateView.as_view(),name='customer_update'), 
    path('delete/<int:pk>/', views.CustomerDeleteView.as_view(),name='customer_delete'), 
] 
