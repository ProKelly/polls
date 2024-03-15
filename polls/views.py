from django.shortcuts import render, get_object_or_404, redirect
from polls.models import Question, Choice
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import F
from django.urls import reverse
from django.utils import timezone


from django.views import generic

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    queryset = Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]

    # def get_queryset(self):
    #     return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'










# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     output = ",".join([q.question_text for q in latest_question_list])
#     context = {"output": output, "latest_question_list": latest_question_list}
#     return render(request, 'polls/index.html', context)

# def detial(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     context = {'question': question}
#     return render(request, 'polls/detail.html', context)

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try: 
        selected_choice = question.choice_set.get(pk=request.POST.get("choice"))
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question': question, "error_message": "you didn't select a choice", }, )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
    return redirect('polls:results', question.id)





