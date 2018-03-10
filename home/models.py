# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Article(models.Model):
	title = models.CharField(max_length=150, null=False)
	intro = models.CharField(max_length=150, null=True)
	content = models.CharField(max_length=20000, null=False)
	time = models.CharField(max_length=20, null=False)
	author = models.CharField(max_length=20, null=True)
	view = models.IntegerField(default=0)

	def __str__(self):
		return self.title