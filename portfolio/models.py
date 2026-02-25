from django.db import models

# Create your models here.


class Experience(models.Model):
    designation = models.CharField(max_length = 100)
    company = models.CharField(max_length = 150)
    work_duration = models.CharField(max_length = 100)
    work_detail = models.TextField(max_length = 500, default='None')

    def __str__(self):
        return self.company
    


class Project(models.Model):
    project_name = models.CharField(max_length = 100)
    company = models.CharField(max_length = 100)
    techstack = models.CharField(max_length = 2000)
    live = models.URLField(max_length = 200, blank = True)
    codebase = models.URLField(max_length = 200, blank = True)
    duration = models.CharField(max_length = 100)
    short_description = models.CharField(max_length=500)
    project_description = models.TextField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.project_name 
    

class Skills(models.Model):
    skiller = models.CharField(max_length=100, default="Karan's Skills")
    ai = models.CharField(max_length = 300)
    frontend = models.CharField(max_length = 300)
    backend = models.CharField(max_length = 300)
    tools = models.CharField(max_length = 300)
    deployment = models.CharField(max_length = 300)

    class Meta:
        verbose_name_plural = "Skills"
    def __str__(self):
        return self.skiller



