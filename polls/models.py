from __future__ import unicode_literals

import datetime

from django.db import models

from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class Question(models.Model):

    def __str__(self):
        return self.question_text


    def was_published_recently(self):
      now = timezone.now()
      return now - datetime.timedelta(days=1) <= self.pub_date <= now
    datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'



    question_text = models.CharField(max_length=250)
    pub_date = models.DateTimeField('published date')

@python_2_unicode_compatible
class Decision(models.Model):

    def __str__(self):
        return self.decision_text


    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=250)
    votes = models.IntegerField(default=0)

