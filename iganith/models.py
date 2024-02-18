from django.db import models

from django.contrib.auth.models import User

# Create your models here.

from django.core.validators import MinValueValidator, MaxValueValidator

class Question(models.Model):
    question_id = models.IntegerField(unique=True)
    question_image = models.ImageField(upload_to = "iganithquestion" , default="")
    correct_answer = models.CharField(max_length=200 , null=True)


class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=[('N', "NotStarted"), ('S', "Started"), ('E', "Ended")], default='N')
    score = models.IntegerField(null=True, default=0)
    chance = models.IntegerField(null=True ,default=4)
    answered = models.ManyToManyField(Question, null=True , related_name = "correctanswered")
    just_answered = models.ManyToManyField(Question, null=True ,related_name = "only_answered")
    startTime = models.DateTimeField(null=True)
    endTime = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return self.user.username