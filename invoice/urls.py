from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.InvoiceListView.as_view(),name='invoice_list'),
    path('<int:pk>/', views.InvoiceDetailView.as_view(),name='invoice_detail'),
    path('create/', views.InvoiceCreateView.as_view(),name='invoice_create'), 
    path('update/<int:pk>/', views.InvoiceUpdateView.as_view(),name='invoice_update'), 
    path('delete/<int:pk>/', views.InvoiceDeleteView.as_view(),name='invoice_delete'), 
] 
