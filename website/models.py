from django.db import models


class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    major = models.CharField(max_length=200)
    department = models.CharField(max_length=50)
    class_level = models.CharField(max_length=50)
    gpa = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
