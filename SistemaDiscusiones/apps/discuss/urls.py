from django.conf.urls import patterns, include, url
from .views import QuestionListView


urlpatterns = patterns('',
	url(r'^preguntas/$', QuestionListView.as_view(), name='questions'),
	url(r'^buscar-ajax/$', 'apps.discuss.views.BuscarAjax', name='buscar'),
	)
