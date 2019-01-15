from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
	author=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title=models.CharField(max_length=200)
	text=models.TextField()
	created_date=models.DateTimeField(default=timezone.now)
	published_date=models.DateTimeField(blank=True,null=True)

	def publish(self):
		self.published_date=timezone.now()
		self.save()
	def __str__(self):
		return self.title

class Comment(models.Model):
	post=models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
	user=models.CharField(max_length=200)
	email=models.EmailField()
	text=models.TextField(max_length=500)
	created_date = models.DateTimeField(default=timezone.now())
	approved_comments=models.BooleanField(default=False)


	def approve(self):
		self.approved_comments=True
		self.save()

	def __str__(self):	

		return self.text



    
