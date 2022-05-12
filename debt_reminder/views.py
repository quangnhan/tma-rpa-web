from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Customer

class CustomerListView(ListView):
    model = Customer
    template_name = 'customer/customer_list.html'
    context_object_name = 'list_all_customer' 

    def get_queryset(self):
        cmnd = self.request.GET.get('cmnd', None)
        if cmnd:
            qs = Customer.objects.filter(CMND=cmnd)
            return qs
        return super().get_queryset()

class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customer/customer_detail.html'
    context_object_name = 'Customer' 

class CustomerCreateView(CreateView):
    model = Customer
    template_name = 'customer/customer_create.html'
    fields = '__all__'
    success_url = reverse_lazy('customer_create')

class CustomerUpdateView(UpdateView):
    model = Customer
    template_name = 'customer/customer_update.html'
    fields = '__all__'

class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'customer/customer_delete.html'
    context_object_name = 'Customer' 
    success_url = reverse_lazy('customer_list')