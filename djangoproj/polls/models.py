import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    """Represent Question in poll
    
    Attributes: 
        question_text (str): Question text.
        pub_date (datetime): Date when published.
    """

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    """Represent Choice for question in poll

    Attributes: 
        question (Question): Used as foreign key.
        choice_text (str): Choice text.
        votes (int): Vote tally.
    """
    
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text