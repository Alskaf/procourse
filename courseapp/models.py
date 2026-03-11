from django.db import models



class Course(models.Model):

    name=models.CharField(max_length=255)
    techers=models.CharField(max_length=255)
    date=models.DateField(null=True , blank=True)
    price=models.FloatField(null=True , blank=True)
    description=models.TextField()
    imag=models.ImageField(upload_to="course/", blank=True)



class Lesson(models.Model):
    DAY_CHOICES = [
        ("sat", "Saturday"),
        ("sun", "Sunday"),
        ("mon", "Monday"),
        ("tue", "Tuesday"),
        ("wed", "Wednesday"),
        ("thu", "Thursday"),
        ("fri", "Friday"),
    ]
    course_name=models.ForeignKey(Course , on_delete=models.CASCADE)
    day=models.CharField(max_length=255 , choices=DAY_CHOICES, null=True)
    time=models.DateTimeField(null=True , blank=True)
    description=models.TextField(null=True , blank=True)






