from django.db import models
class Event(models.Model):  #наследование
	event_image = models.ImageField(upload_to='event_images/')
	event_text = models.CharField(max_length=300)	
		
	