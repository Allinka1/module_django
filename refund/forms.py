from django.forms import ModelForm, HiddenInput
from django.views.generic import CreateView
from refund.models import Refund


class RefundCreateForm(ModelForm):

    class Meta:
        model = Refund
        fields = ['order']
        widgets = {'order': HiddenInput()}
