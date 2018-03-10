# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from . import models

# Create your views here.

def index(reuqest):
	temp = models.Article.objects.all()
	articles = list(reversed(temp))[:3]
	return render(reuqest, 'home/index.html', {'articles': articles})

def allpost(reuqest):
	temp = models.Article.objects.all()
	articles = list(reversed(temp))
	return render(reuqest, 'home/allpost.html', {'articles': articles})

def post(reuqest, article_id):
	article = models.Article.objects.get(pk=article_id)
	return render(reuqest, 'home/post.html', {'article': article})

def about(reuqest):
	return render(reuqest, 'home/about.html')

def contact(reuqest):
	return render(reuqest, 'home/contact.html')
