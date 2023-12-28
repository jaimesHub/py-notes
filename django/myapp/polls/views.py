from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, Http404

# Create your views here.
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    
    # template = loader.get_template("polls/index.html")
    # context = {
    #     "latest_question_list": latest_question_list
    # }
    
    # return HttpResponse(template.render(context=context, request=request))

    # Django provides a shorcut
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context=context)


def greeting(request):
    
    return HttpResponse("Hello, world")

# def index(request):
#     
#     return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist!")
    # return render(request, "polls/detail.html", {"question": question})

    # Django provides a shortcut
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

    # return HttpResponse("You're looking at question %s" % question_id)

def results(question, question_id):
    response = "Your're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
