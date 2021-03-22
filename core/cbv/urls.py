from django.urls import path
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from cbv.views import Ex2View, PostPreloadTaskView, SinglePostView

app_name = 'cbv'

urlpatterns = [
    path('ex1', TemplateView.as_view(template_name='ex1.html', extra_context={'title': 'Custom title'})),
    path('ex2', Ex2View.as_view(), name='ex2'),
    path('rdt', RedirectView.as_view(url='https://youtu.be/ScteNE1jB4g'), name='go-to-youtube'),
    path('ex3/<int:pk>/', PostPreloadTaskView.as_view(), name='redirect-task'),
    path('ex4/<int:pk>/', SinglePostView.as_view(), name='singlepost')
]