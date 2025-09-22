from django.db import models
from django.contrib.auth.models import User

class LibraryNote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

from django.db import models
from django.contrib.auth.models import User

class StudentProfile(models.Model):
    USER_TYPE_CHOICES = [
        ("school", "School"),
        ("college", "College"),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    grade = models.CharField(max_length=20, blank=True, null=True)
    year = models.CharField(max_length=20, blank=True, null=True)
    school_name = models.CharField(max_length=255, blank=True, null=True)
    college_name = models.CharField(max_length=255, blank=True, null=True)
    course = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=15)
    student_id = models.CharField(max_length=50)
    age = models.IntegerField()
    dob = models.DateField()

    def __str__(self):
        return self.user.first_name
