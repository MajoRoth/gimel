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

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'Segment/index.html'
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        today = timezone.datetime.today()
        context = super().get_context_data(**kwargs)
        context['segment'] = Segment.objects.filter(user=self.request.user).filter(Active=True).filter(date__year=today.year, date__month=today.month, date__day=today.day)
        print(context['segment'])
        return context


class AllSegmentsView(PermissionRequiredMixin, TemplateView):
    permission_required = 'Segment.view_segment'
    template_name = 'Segment/view.html'

    def get_context_data(self, **kwargs):
        today = timezone.datetime.today()
        context = super().get_context_data(**kwargs)
        context['segments'] = Segment.objects.filter(date__year=today.year, date__month=today.month, date__day=today.day).filter(Active=True)
        return context


class CreateSegmentView(PermissionRequiredMixin, CreateView):
    permission_required = 'Segment.add_segment'
    form_class = forms.SegmentForm
    model = Segment
    template_name = 'Segment/admin.html'

    def get_context_data(self, **kwargs):
        today = timezone.datetime.today()
        context = super().get_context_data(**kwargs)
        context['segments'] = Segment.objects.filter(date__year=today.year, date__month=today.month, date__day=today.day).filter(Active=True)
        #  ---LISTS---
        all_users = User.objects.filter(is_staff=False)
        all_users = set(list(all_users))
        users_segments = set()
        for seg in context['segments']:
            users_segments.add(seg.user)

        all_segments = {i for i in Segment.SegmentChoices.labels}
        assigned_segments = {i.get_segment_display() for i in context['segments']}

        print(all_segments, assigned_segments)
        context['user_list'] = all_users - users_segments  # difference of sets
        context['segment_list'] = all_segments - assigned_segments
        print(context['segment_list'])
        return context


@permission_required('Segment.add_segment')
def approveSegment(request, seg_pk):
    segment = Segment.objects.get(pk=seg_pk)
    segment.approve()
    return HttpResponseRedirect(reverse('Segment:admin'))

@permission_required('Segment.add_segment')
def disapproveSegment(request, seg_pk):
    segment = Segment.objects.get(pk=seg_pk)
    segment.disapprove()
    return HttpResponseRedirect(reverse('Segment:admin'))

@permission_required('Segment.add_segment')
def disactiveSegment(request, seg_pk):
    segment = Segment.objects.get(pk=seg_pk)
    segment.disactive()
    return HttpResponseRedirect(reverse('Segment:admin'))






