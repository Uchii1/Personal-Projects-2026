from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.generic import TemplateView
from .models import StudyModel
from .models import * 
from django.http import HttpResponse
import random
from django.contrib.auth.decorators import login_required
import json
from itertools import groupby # to group the quiz links neatly.

import json
from django.db import transaction
from django.views.decorators.http import require_POST
from .models import QuizAttempt, AnswerRecord

from . import stats
from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

# importing guessing game
from . import guess_game


# User Creation form (in views.py)
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"



def get_quiz(request):
    try:
        question_objs = Question.objects.all()
        
        if request.GET.get('gfg'):
            question_objs = question_objs.filter(gfg__gfg_name__iexact = request.GET.get('gfg')) # locates quiz using iexact, not icontains
            
        question_objs = list(question_objs)
        data = []
        random.shuffle(question_objs)
        
        
        for question_obj in question_objs:
            
            data.append({
                "uid" : question_obj.uid,
                "gfg": question_obj.gfg.gfg_name,
                "question": question_obj.question,
                "question_image": question_obj.question_image.url if question_obj.question_image else None,
                "answer" : question_obj.get_answers(),
                "explanation": question_obj.explanation,
                "explanation_image": question_obj.explanation_image.url if question_obj.explanation_image else None,
            })

        payload = {'status': True, 'data': data}
        
        return JsonResponse(payload)  # Return JsonResponse
        
    except Exception as e:
        print(e)
        return HttpResponse("Something went wrong")


def quiz(request):
    gfg_name = request.GET.get('gfg', '')
    gfg_obj = Topic.objects.filter(gfg_name=gfg_name).first()
    context = {'gfg': gfg_name, 'gfg_id': gfg_obj.uid if gfg_obj else None}
    return render(request, 'gfg_site_app/quiz.html', context)

"""
# This view is to save results of the attempt.
@login_required
def submit_quiz(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        QuizAttempt.objects.create(
            user=request.user,
            gfg_id=data['gfg_id'],
            score=data['score'],
            total=data['total']
        )
        return JsonResponse({'status': True})
"""


# Post for attempt recording
@require_POST
def submit_quiz(request):
    if not request.user.is_authenticated:
        return JsonResponse({'status': False, 'error': 'login required'}, status=401)
    try:
        data = json.loads(request.body)
        with transaction.atomic():
            attempt = QuizAttempt.objects.create(
                user=request.user,
                gfg_id=data['gfg_id'],
                score=data['score'],
                total=data['total'],
                seconds_taken=data.get('seconds_taken', 0),
            )
            AnswerRecord.objects.bulk_create([
                AnswerRecord(
                    attempt=attempt,
                    question_id=a['uid'],
                    is_correct=a['is_correct'],
                    seconds_taken=a.get('seconds_taken', 0),
                )
                for a in data.get('answers', [])
            ])
        return JsonResponse({'status': True})
    except Exception as e:
        print(e)
        return JsonResponse({'status': False, 'error': str(e)}, status=400)

    
# This groups the quiz links. Regular quizes for each topic is shown beside the advanced version
def home(request):
    studies = StudyModel.objects.order_by("pair_id", "is_advanced")
    pairs = [list(group) for _, group in groupby(studies, key=lambda s: s.pair_id)]
    categories = Topic.objects.all()
    context = {
        'pairs': pairs,
        'categories': categories,
        'show_cookie': request.session.pop("show_cookie", False),
    }
    return render(request, 'gfg_site_app/home.html', context=context)

# views for each page
from django.shortcuts import render

def geometric_formulas(request):
    return render(request, "geometric_formulas.html")

def pomodoro_timer(request):
    return render(request, "pomodoro_timer.html")

def break_resources(request):
    return render(request, "break_resources.html")



def about(request):
    return render(request, "about.html")

@login_required
def progress(request):
    return render(request, 'gfg_site_app/progress.html', {
        'summary': stats.summary(request.user),
        #'weakest': stats.weakest_questions(request.user), # this line is not used anymore causes error
        #'revise': stats.revision_tags(request.user),# not used anymore. cuases erroor
    })

def progress_data(request):
    if not request.user.is_authenticated:
        return JsonResponse({'status': False, 'error': 'login required'}, status=401)
    return JsonResponse({
        'status': True,
        'over_time': stats.score_over_time(request.user),
        'by_tag': stats.accuracy_by_tag(request.user, limit= 8), # shows the 8 skills  with lowest scores
        'by_type': stats.accuracy_by_type(request.user),
    })


from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST

from . import guess_game

MAX_GUESSES = 10

def guess_game_page(request):
    """Render the page and start a fresh game."""
    request.session["special_number"] = guess_game.new_game()
    request.session["guesses"] = 0
    return render(request, "quiz/guess_game.html")


@require_POST
def guess_game_guess(request):
    """Check a guess and return the result as JSON."""
    special_number = request.session.get("special_number")
    if special_number is None:
        return JsonResponse(
            {"status": "expired", "message": "Game expired. Please reload the page."},
            status=400,
        )

    status, message = guess_game.check_guess(request.POST.get("guess"), special_number)

    if status != "invalid":
        request.session["guesses"] = request.session.get("guesses", 0) + 1

    guesses = request.session.get("guesses", 0)
    if status in ("high", "low") and guesses >= MAX_GUESSES:
        message += f" Out of guesses! The number was {special_number}."
        status = "lost"
        del request.session["special_number"]

    return JsonResponse({
        "status": status,
        "message": message,
        "guesses": guesses,
    })

class PlaceholderView(TemplateView):
    template_name = "placeholder.html"
    page_title = "Coming soon"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = self.page_title
        return context
    
def syllabus(request):
    return render(request, "syllabus.html")

def contact(request):
    return render(request, "contact.html")

def privacy(request):
    return render(request, "privacy.html")

def accessibility(request):
    return render(request, "accessibility.html")

class FontForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["font"]

@login_required
def choose_font(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    form = FontForm(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        return redirect("choose_font")
    return render(request, "choose_font.html", {"form": form})