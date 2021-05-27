from django.urls import path
from user.views import UserRegistrationView, UserLoginView, UserLogoutView, UserProfileView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    # path('change_password/', change_password, name='change_password'),
    # path('interview/', interview, name='interview'),
]
