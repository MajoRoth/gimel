from django.urls import path
from Segment import views

app_name = 'Segment'

urlpatterns = [
    path('admin/', views.CreateSegmentView.as_view(), name='admin'),
    path('view/', views.AllSegmentsView.as_view(), name='view'),
    path('segment_approve/<int:seg_pk>/', views.approveSegment, name='ApproveSegment'),
    path('segment_disapprove/<int:seg_pk>/', views.disapproveSegment, name='disApproveSegment'),
    path('segment_disactive/<int:seg_pk>/', views.disactiveSegment, name='disactiveSegment'),

]