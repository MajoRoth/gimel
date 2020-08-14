from django.urls import path
from Accounts import views
from django.contrib.auth.views import LogoutView, LoginView

app_name = 'Accounts'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='Accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    ]


