from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .models import Multiple_choice_trivia, UserAnswer
from django.contrib.auth.views import LoginView, LogoutView
from django import forms
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.db.models import Count, F


from . forms import UserRegistrationForm, UserLoginForm


def QuizPage(request):
    if request.method == 'POST':
        questions = Multiple_choice_trivia.objects.filter(question__in=request.POST.getlist('question_id'))
        score = 0

        for question in questions:
            selected_answer = request.POST.get(f'q-{question.question}')
            
            if selected_answer == 'A':
                selected_answer = 0
            if selected_answer == 'B':
                selected_answer = 1
            if selected_answer == 'C':
                selected_answer = 2
            if selected_answer == 'D':
                selected_answer = 3

            if selected_answer == question.answer:
                score += 1

            # Save the user's answer regardless of correctness
            UserAnswer.objects.create(
                trivia_question=question,
                selected_answer=selected_answer,
                user=request.user
            )
        
        message = get_score_message(score)
        
        return JsonResponse({'score': score, 'message': message})

    else:
        questions = Multiple_choice_trivia.objects.all().order_by('?')[:5]
        return render(request, 'quiz.html', {'questions': questions})


def get_score_message(score):
    if score == 5:
        return "By the shimmering stars of knowledge! 🌟 You’ve achieved a perfect score! 🌟 You, dear quizzing champion, have proven yourself a master of trivia magic! May your wand always point to wisdom!"
    elif score == 4:
        return "Ah, a splendid score indeed! ✨ Four out of five! ✨ You’re nearly a wizard of trivia yourself! Just a sprinkle more practice, and you shall join the ranks of the great Quizmasters!"
    elif score == 3:
        return "Aha! ✨ Three out of five! ✨ Not too shabby, my intrepid learner! With a bit more curiosity and perhaps a few more potions of knowledge, you’ll soon be conjuring up even greater scores!"
    elif score == 2:
        return "Oh dear, two out of five! Fear not, brave soul! Even the mightiest wizards had to start somewhere. Dust off those spellbooks and return for another round—your journey is just beginning!"
    else:
        return "Oh, my stars and moonbeams! A score of one—or perhaps none? Worry not, dear friend! Every great wizard stumbles before they soar. Gather your courage, for I sense a spark of potential waiting to ignite within you!"
    
    return render(request, 'quiz.html', context)


class HomePage(TemplateView):
    """
    Displays home page
    """
    # template_name = 'base.html'
    template_name = 'index.html'


class UserRegistrationView(CreateView):
    """
    Displays user registration page and handles user registration
    """
    form_class = UserRegistrationForm
    template_name = "accounts/registration/registration-user.html"
    success_url = reverse_lazy('user_registration_success')
    

class UserSuccessView(TemplateView):
    """
    Displays user registration success page
    """
    template_name = "accounts/registration/registration-success.html"

class UserLoginView(LoginView):
    """
    Displays login page
    """
    form_class = UserLoginForm
    template_name = 'accounts/login-user.html'
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return self.success_url

# logout
class UserLogoutView(LogoutView):
    next_page = reverse_lazy('home')


from django.views.generic import TemplateView
from django.db.models import Count, F, Case, When, FloatField
from django.contrib.auth import get_user_model

class ScoresPage(TemplateView):
    """
    Displays scores page
    """
    template_name = 'scores.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        CustomUser = get_user_model()  # Retrieve the custom user model

        # Calculate scores and percentages for the leaderboard
        scores = CustomUser.objects.annotate(
            correct_answers=Count('useranswer', filter=F('useranswer__is_correct')),
            total_answers=Count('useranswer'),
            percentage_correct=Case(
                When(total_answers=0, then=0),
                default=F('correct_answers') * 100.0 / F('total_answers'),
                output_field=FloatField()
            )
        ).order_by('-percentage_correct', '-correct_answers')[:5]  # Get top 5 users by percentage

        context['scores'] = scores  # Add scores to context
        return context


def quiz_answer(request, question_id):
    trivia_question = Multiple_choice_trivia.objects.get(id=question_id)
    
    if request.method == "POST":
        selected_answer = int(request.POST.get('answer'))
        user_answer = UserAnswer(trivia_question=trivia_question, selected_answer=selected_answer)
        user_answer.save()  # This will set is_correct automatically in the save method

        # Redirect to a results page or display a message
        return redirect('quiz_results')  # Adjust as needed
    
    return render(request, 'quiz/question.html', {'question': trivia_question})