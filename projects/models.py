from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    tech = models.CharField(max_length=20)
    # define a FileField with a subfolder named project_images/.
    # That’s where Django should store the images when you upload them.
    image = models.FileField(upload_to="project_media/", blank=True)
