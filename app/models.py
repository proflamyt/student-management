from django.urls import reverse 

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    name =  models.CharField(max_length=30)
    course_code = models.CharField(max_length=30)
    co_lecturer = models.CharField(max_length=30)
    no_of_students = models.IntegerField()
    class Meta:
        ordering = ["name"]
        verbose_name_plural = "course"
    def __str__(self):
        return self.name

class Attendance(models.Model):
    no_of_classes = models.IntegerField()
    course =models.ForeignKey(
        Course,
        null=True,
        blank=True,
        on_delete = models.CASCADE
    )
    def __str__(self):
        return f"Attendance list of {self.course.name}" 

    


class ClassMember(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    department = models.CharField(max_length=30, blank=True, null=True) #change to choicefield
    matric_number = models.CharField(max_length=11)
    attendance = models.ForeignKey(
        Attendance,
        on_delete=models.CASCADE,
    )
    attended =  models.IntegerField(
        
        default=0
    )
    course = models.ForeignKey(Course,  null=True,
        blank=True,
        on_delete = models.CASCADE)
    def get_absolute_url(self):      
        return reverse('member', args=[str(self.id)])
    

    def __str__(self):
        return self.matric_number