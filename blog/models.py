from django.db import models

class Article(models.Model):
	title = models.CharField(max_length=32, default='title')
	content = models.CharField(max_length=10000, null=True)

	def  __unicode__(self):
		return self.title