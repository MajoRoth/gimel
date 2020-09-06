from django.views.generic import CreateView, TemplateView
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.utils import timezone
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.models import User

from Segment import forms
from Segment.models import Segment


# Create your views here.


class CreateSegmentView(PermissionRequiredMixin, CreateView):
    permission_required = 'Segment.create_segment'
    form_class = forms.SegmentForm
    model = Segment
    template_name = 'Segment/admin.html'

    def get_context_data(self, **kwargs):
        today = timezone.datetime.today()
        context = super().get_context_data(**kwargs)
        context['segments'] = Segment.objects.filter(date__year=today.year, date__month=today.month, date__day=today.day)
        #  ---LISTS---
        all_users = User.objects.all()
        all_users = set(list(all_users))
        users_segments = set()
        for seg in context['segments']:
            users_segments.add(seg.user)

        all_segments = {'TU', 'JU', 'CO', 'TR'}
        assigned_segments = set()
        for seg in context['segments']:
            assigned_segments.add(seg.segment)

        context['user_list'] = all_users - users_segments  # difference of sets
        context['segment_list'] = all_segments - assigned_segments
        return context




@permission_required('Segment.change_aorder')
def approveSegment(request, seg_pk):
    segment = Segment.objects.get(pk=seg_pk)
    segment.approve()
    return HttpResponseRedirect(reverse('Segment:admin'))

@permission_required('Segment.change_aorder')
def disapproveSegment(request, seg_pk):
    segment = Segment.objects.get(pk=seg_pk)
    segment.disapprove()
    return HttpResponseRedirect(reverse('Segment:admin'))

@permission_required('Segment.change_aorder')
def disactiveSegment(request, seg_pk):
    segment = Segment.objects.get(pk=seg_pk)
    segment.disactive()
    return HttpResponseRedirect(reverse('Segment:admin'))






