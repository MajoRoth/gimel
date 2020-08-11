from django.urls import path, include
from Orders import views

app_name = 'Order'

urlpatterns = [
    path('Wcreate/', views.WorderCreateView.as_view(), name='CreateWorder'),
    path('Tcreate/', views.TorderCreateView.as_view(), name='CreateTorder'),
    path('Acreate/', views.AorderCreateView.as_view(), name='CreateAorder'),
    path('', views.OrderIndexView.as_view(), name='index'),

]