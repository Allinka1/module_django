from django.urls import path
from refund.views import RefundCreateView, RefundListView

app_name = "refund"
urlpatterns = [
    path("create/", RefundCreateView.as_view(), name="create"),
    path("", RefundListView.as_view(), name="refund_list"),
]
