from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Classroom(models.Model):
    name = models.CharField(max_length=120)
    subject = models.CharField(max_length=120)
    year = models.IntegerField()
    teacher = models.ForeignKey(
        User, on_delete=models.CASCADE,  null=True, blank=True)

    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        return reverse('classroom-detail', kwargs={'classroom_id': self.id})


# Gender Choices
MALE = 'Male'
FEMALE = 'Female'
GENDER_CHOICES = ((MALE, 'Male'), (FEMALE, 'Female'),)


class Student(models.Model):

	name = models.CharField(max_length=120)
	date_of_birth = models.DateField()
	gender = models.CharField(max_length=20,choices=GENDER_CHOICES, default=MALE)
	exam_grade = models.CharField(max_length=120)
	classroom = models.ForeignKey(Classroom,on_delete=models.CASCADE,blank= False, null = False)

	def __str__(self):
		return self.name