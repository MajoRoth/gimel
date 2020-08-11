from django.urls import path, include
from Orders import views

app_name = 'Order'

urlpatterns = [
    path('Wcreate/', views.WorderCreateView.as_view(), name='CreateWorder'),

]