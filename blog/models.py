from django.db import models


class Blog(models.Model):
	title = models.CharField(max_length=30)
	text = models.TextField(max_length=300)
	date = models.DateTimeField()
	image = models.ImageField(upload_to='event_images/')

	def get_summary(self):
		return self.text[:70]

	def __str__(self):
		return self.title
