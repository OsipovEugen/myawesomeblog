from django.db import models


class Blog(models.Model):
	title = models.CharField(max_length=30)
	text = models.TextField(max_length=300)
	date = models.DateTimeField()
	image = models.ImageField(upload_to='event_images/')

# Create your models here.
