from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from order.models import Order


class OrderListView(LoginRequiredMixin, ListView):

    model = Order
    template_name = "order_list.html"

    def get_queryset(self):
        queryset = super(OrderListView, self).get_queryset()

        return queryset.filter(customer=self.request.user)


class OrderDetailView(LoginRequiredMixin, DetailView):

    model = Order
    template_name = "order_detail.html"

    def get(self, *args, **kwargs):
        order = self.get_object()
        if order.customer != self.request.user:
            redirect_url = reverse_lazy("order:list")
            return HttpResponseRedirect(redirect_url)

        return super(OrderDetailView, self).get(*args, **kwargs)


class OrderCreateView(LoginRequiredMixin, CreateView):

    model = Order
    fields = ["product", "quantity"]

    def form_valid(self, form):
        form.instance.customer = self.request.user
        return super(OrderCreateView, self).form_valid(form)
