from django.db import models


# Create your models here.
class project(models.Model):
    namme = models.CharField(max_length=200)

    def __str__(self):
        return self.namme


class task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(project, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title + " - " + self.project.namme
