from django.shortcuts import render
from django.views.generic import ListView
from django.core import serializers
from django.http import HttpResponse
from .models import Question, Tag

class QuestionListView(ListView):
	
	model = Question
	context_object_name = 'questions'

	def get_context_data(self, **kwargs):
	    context = super(QuestionListView, self).get_context_data(**kwargs)
	    context['tags'] = Tag.objects.all()
	    return context


def BuscarAjax(request):
	tag = Tag.objects.get(id = request.GET['id'])
	questions = Question.objects.filter(tag = tag)
	data = serializers.serialize('json', questions, fields = {'title','description','modified'})
	return HttpResponse(data, content_type = 'aplication/json')
