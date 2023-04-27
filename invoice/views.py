from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Invoice

class InvoiceListView(ListView):
    model = Invoice
    template_name = 'invoice/invoice_list.html'
    template_name = 'invoice/invoice_list.html'
    context_object_name = 'invoices'

class InvoiceDetailView(DetailView):
    model = Invoice
    template_name = 'invoice/invoice_detail.html'
    context_object_name = 'invoice'

class InvoiceCreateView(CreateView):
    model = Invoice
    template_name = 'invoice/invoice_create.html'
    fields = '__all__'
    success_url = reverse_lazy('invoice_create')

class InvoiceUpdateView(UpdateView):
    model = Invoice
    template_name = 'invoice/invoice_update.html'
    fields = '__all__'
    success_url = reverse_lazy('invoice_list')

class InvoiceDeleteView(DeleteView):
    model = Invoice
    template_name = 'invoice/invoice_delete.html'
    context_object_name = 'invoice'
    success_url = reverse_lazy('invoice_list')