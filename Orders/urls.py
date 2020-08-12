from django.urls import path, include
from Orders import views

app_name = 'Orders'

urlpatterns = [
    path('wcreate/', views.WorderCreateView.as_view(), name='CreateWorder'),
    path('tcreate/', views.TorderCreateView.as_view(), name='CreateTorder'),
    path('acreate/', views.AorderCreateView.as_view(), name='CreateAorder'),
    path('', views.OrderIndexView.as_view(), name='index'),

]