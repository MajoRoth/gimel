from django.urls import path, include
from Orders import views

app_name = 'Orders'

urlpatterns = [
    path('wcreate/', views.WorderCreateView.as_view(), name='CreateWorder'),
    path('wdelete/<int:order_pk>/', views.deleteWorder, name='DeleteWorder'),
    path('tcreate/', views.TorderCreateView.as_view(), name='CreateTorder'),
    path('tdelete/<int:order_pk>/', views.deleteTorder, name='DeleteTorder'),
    path('acreate/', views.AorderCreateView.as_view(), name='CreateAorder'),
    path('adelete/<int:order_pk>/', views.deleteAorder, name='DeleteAorder'),
    path('', views.OrderIndexView.as_view(), name='index'),

    path('worderadmin/', views.WorderAdmin.as_view(), name='worderadmin'),
    path('worderadmin_approve/<int:order_pk>/', views.approveWorder, name='ApproveWorder'),
    path('worderadmin_disapprove/<int:order_pk>/', views.disapproveWorder, name='disApproveWorder'),
    path('worderadmin_collect/<int:order_pk>/', views.collectWorder, name='CollectWorder'),
    path('worderadmin_return/<int:order_pk>/', views.returnWorder, name='ReturnWorder'),

    path('torderadmin/', views.TorderAdmin.as_view(), name='torderadmin'),
    path('torderadmin_approve/<int:order_pk>/', views.approveTorder, name='ApproveTorder'),
    path('torderadmin_disapprove/<int:order_pk>/', views.disapproveTorder, name='disApproveTorder'),
    path('torderadmin_collect/<int:order_pk>/', views.collectTorder, name='CollectTorder'),
    path('torderadmin_return/<int:order_pk>/', views.returnTorder, name='ReturnTorder'),

    path('aorderadmin/', views.AorderAdmin.as_view(), name='aorderadmin'),
    path('aorderadmin_approve/<int:order_pk>/', views.approveAorder, name='ApproveAorder'),
    path('aorderadmin_disapprove/<int:order_pk>/', views.disapproveAorder, name='disApproveAorder'),

    path('worderadmin_comment/<int:order_pk>/', views.CommentWorder.as_view(), name='CommentWorder'),

]