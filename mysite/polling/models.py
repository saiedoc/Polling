from django.db import models

# Create your models here.

class User(models.Model):

    username = models.CharField(null=False,max_length=30)

    def get_username(self):
        return self.username

class Question(models.Model):

    question_title = models.CharField(null = False,max_length=100)
    creation_date = models.DateTimeField(null = False)
    creator = models.ForeignKey(User,on_delete=models.CASCADE)

    def get_question_title(self):
        return self.question_title
    def get_creation_date(self):
        return self.creation_date
    def get_creator(self):
        return self.creator

class Option(models.Model):

    option_title = models.CharField(null=False,max_length=100)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)

    def get_option_title(self):
        return self.option_title
    def get_question(self):
        return self.question

class answer(models.Model):

    option = models.ForeignKey(Option,on_delete=models.CASCADE)
    user  = models.ForeignKey(User,on_delete=models.CASCADE)
    answer_date = models.DateTimeField(null = False)

    def get_option(self):
        return self.option
    def get_user(self):
        return self.user
    def get_answer_date(self):
        return self.answer_date