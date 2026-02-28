from django.db import models

# Create your models here.


class Course(models.Model):

    name=models.CharField(max_length=255)
    techers=models.CharField(max_length=255)
    date=models.DateField(null=True , blank=True)
    description=models.TextField()
    imag=models.ImageField(upload_to="course/", blank=True)



class lesson(models.Model):
    course_name=models.ForeignKey(Course , on_delete=models.CASCADE)
    day=models.DateField()
    time=models.DateTimeField()
    description=models.TextField()






