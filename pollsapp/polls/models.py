from django.db import models
from django.utils import timezone


# Create your models here.
class Track(models.Model):
    track_text = models.CharField(max_length=200)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


# purpose of this model is to store each question with choice and answer type weather it is correct or wrong
class UserChoice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)
