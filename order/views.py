from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from refund.forms import RefundCreateForm
from order.models import Order
from refund.models import Refund
from django.contrib import messages


class OrderListView(LoginRequiredMixin, ListView):

    model = Order
    template_name = "order_list.html"

    def get_queryset(self):
        queryset = super(OrderListView, self).get_queryset()

        return queryset.filter(customer=self.request.user)


class OrderDetailView(LoginRequiredMixin, DetailView):

    model = Order

    def get(self, *args, **kwargs):
        order = self.get_object()
        if order.customer != self.request.user:
            redirect_url = reverse_lazy("order:list")
            return HttpResponseRedirect(redirect_url)

        return super(OrderDetailView, self).get(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(OrderDetailView, self).get_context_data(**kwargs)
        refund_form = RefundCreateForm()
        context['refund_form'] = refund_form
        return context


class OrderCreateView(LoginRequiredMixin, CreateView):

    model = Order
    fields = ["product", "quantity"]

    def form_valid(self, form):
        form.instance.customer = self.request.user
        total_price = form.instance.product.price * form.instance.quantity
        user_wallet = form.instance.customer.userprofile.wallet
        if total_price > user_wallet:
            message_text = 'There is not enough funds in your wallet to pay for this purchase'
            messages.add_message(self.request, messages.WARNING, message_text)
            redirect_url = reverse_lazy("products_list")
            return HttpResponseRedirect(redirect_url)
        elif form.instance.quantity > form.instance.product.quantity:
            messages.add_message(self.request, messages.WARNING, "Not enough products in stock")
            redirect_url = reverse_lazy("products_list")
            return HttpResponseRedirect(redirect_url)
        return super(OrderCreateView, self).form_valid(form)
