from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from django.core import serializers
from django.http import HttpResponse
from .models import Question, Tag, Answer
from .forms import CreateQuestionForm
from braces.views import LoginRequiredMixin

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

class QuestionCreateView(LoginRequiredMixin, CreateView):
	model = Question
	form_class = CreateQuestionForm
	success_url = '/'
	login_url = '/'

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(QuestionCreateView, self).form_valid(form)

	def form_invalid(self, form):
		return super(QuestionCreateView, self).form_invalid(form)

class QuestionDetailView(DetailView):
	model = Question
	context_object_name = 'question'

	def get_answers(self, question):
		answers = Answer.objects.filter(question = question)
		return answers

	def get_context_data(self, **kwargs):
		context = super(QuestionDetailView, self).get_context_data(**kwargs)
		context['answers'] = self.get_answers(context['object'])
		return context

	def post(self, request, *args, **kwargs):
		answer = Answer()
		answer.user = request.user
		answer.description = request.POST['description']
		answer.question = Question.objects.get(slug = kwargs['slug'])
		answer.save()
		answers = self.get_answers(answer.question)
		return render(request, 'discuss/question_detail.html', 
			{'question': answer.question, 'answers':answers})


