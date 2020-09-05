from django.db import models
from django.forms import ModelForm, Textarea, DateField, TimeInput
from django import forms
from django.utils import timezone
from django.contrib.admin import widgets


class Task(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.TextField()
    info = models.TextField(blank=True)
    status = models.BooleanField(default=False)
    date = models.DateField()
    time_start = models.TimeField(blank=True, default=None, null=True)
    time_end = models.TimeField(blank=True, default=None, null=True)

    def add_task(self):
        self.save()
    
    def delete_task(self):
        self.delete()

    def __str__(self):
        return self.title

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'info', 'date')
        widgets = {
            'title': Textarea(attrs={'cols':50, 'rows':1}),
            'info': Textarea(attrs={'cols':50, 'rows':10}),
            'date': forms.SelectDateWidget()
        }







