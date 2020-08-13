from django.urls import path, include
from Orders import views

app_name = 'Orders'

urlpatterns = [
    path('wcreate/', views.WorderCreateView.as_view(), name='CreateWorder'),
    path('tcreate/', views.TorderCreateView.as_view(), name='CreateTorder'),
    path('acreate/', views.AorderCreateView.as_view(), name='CreateAorder'),
    path('', views.OrderIndexView.as_view(), name='index'),
    path('worderadmin/', views.WorderAdmin.as_view(), name='worderadmin'),
    path('worderadmin_approve/<int:order_pk>/', views.approveWorder, name='ApproveWorder'),
    path('worderadmin_disapprove/<int:order_pk>/', views.disapproveWorder, name='disApproveWorder'),
    path('torderadmin/', views.TorderAdmin.as_view(), name='torderadmin'),
    path('torderadmin_approve/<int:order_pk>/', views.approveTorder, name='ApproveTorder'),
    path('torderadmin_disapprove/<int:order_pk>/', views.disapproveTorder, name='disApproveTorder'),
    path('aorderadmin/', views.AorderAdmin.as_view(), name='aorderadmin'),
    path('aorderadmin_approve/<int:order_pk>/', views.approveAorder, name='ApproveAorder'),
    path('aorderadmin_disapprove/<int:order_pk>/', views.disapproveAorder, name='disApproveAorder')

]