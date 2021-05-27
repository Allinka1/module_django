from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, CreateView
from user.models import UserProfile

from user.forms import UserRegistrationForm


class UserRegistrationView(CreateView):
    template_name = "auth/registration.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        user = form.save()
        print(user.id)
        UserProfile.objects.create(wallet=10000, user_id=user.id)
        return super().form_valid(form)





class UserLoginView(LoginView):
    template_name = "auth/login.html"

    def get_success_url(self):

        return self.request.GET.get("next") or reverse_lazy("home")


class UserLogoutView(View):

    def get(self, *args, **kwargs):

        logout(self.request)

        redirect_url = reverse_lazy("home")
        return HttpResponseRedirect(redirect_url)


class UserProfileView(TemplateView):

    template_name = "user/profile.html"
