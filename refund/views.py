from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from refund.forms import RefundCreateForm
from refund.models import Refund
from django.contrib import messages
import pdb
from datetime import datetime, timedelta, timezone


class RefundCreateView(LoginRequiredMixin, CreateView):

    model = Refund
    form_class = RefundCreateForm

    def form_valid(self, form):
        order_datetime = form.instance.order.created_at
        expiry_period = datetime.now(timezone.utc) - order_datetime
        if expiry_period > timedelta(minutes=3):
            message_text = 'Refund time expired'
            messages.add_message(self.request, messages.WARNING, message_text)
            redirect_url = reverse_lazy("order:detail", kwargs={"pk": form.instance.order.id})
            return HttpResponseRedirect(redirect_url)
        else:
            return super(RefundCreateView, self).form_valid(form)


class RefundListView(LoginRequiredMixin, ListView):

    model = Refund
    template_name = "refund_list.html"

    def get_queryset(self):
        queryset = super(RefundListView, self).get_queryset()

        return queryset.select_related('order').filter(order__customer=self.request.user)
