from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, AbstractUser

# Birthdate field for user registration
class CustomUserModel(AbstractUser):
    birthdate = models.DateField(null=True, blank=True)

# Question model
STATUS = ((0, "General Knowledge"), (1, "Sport"), (2, "History"), (3, "Science & Nature"), (4, "Music & Media"), (5, "Past adventure"))

class Question(models.Model):
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="blog_stamps", null=True)
    question = models.CharField(max_length=500, unique=True)
    answer = models.CharField(max_length=500, unique=False)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return f"{self.category} question by {self.user}"


OPTIONS = ((0, "A"), (1, "B"), (2, "C"), (3, "D"))

# Multiple choice question model
class Multiple_choice_trivia(models.Model):
    question = models.CharField(max_length=256, unique=True)
    option_a = models.CharField(max_length=100, unique=False)
    option_b = models.CharField(max_length=100, unique=False)
    option_c = models.CharField(max_length=100, unique=False)
    option_d = models.CharField(max_length=100, unique=False)
    answer = models.IntegerField(choices=OPTIONS, default=0)

    def __str__(self):
        return f"{self.question}"

# User answer model
class UserAnswer(models.Model):
    trivia_question = models.ForeignKey(Multiple_choice_trivia, on_delete=models.CASCADE)
    selected_answer = models.IntegerField(choices=OPTIONS)
    is_correct = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.is_correct = (self.selected_answer == self.trivia_question.answer)
        super().save(*args, **kwargs)