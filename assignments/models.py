from django.db import models

# Create your models here.


class About(models.Model):
    about_heading = models.CharField(max_length = 30)
    about_description = models.TextField(max_length=500)

    def __str__(self):
        return self.about_heading
    

class Social_Media_Links(models.Model):
    social_media_name = models.CharField(max_length = 50)
    social_media_link = models.URLField(max_length = 200)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.social_media_name