from django.shortcuts import render
from django.http import HttpResponse

posts = [
	{
		'author' : 'Nikhil',
		'title' : 'Blog 1',
		'content' : 'This is my first Blog',
		'date' : '3 July 2020'
	},
	{
		'author' : 'Alex',
		'title' : 'Blog 2',
		'content' : 'This is my second Blog',
		'date' : '5 July 2020'
	}
]

def home (request):
	context = {
	'posts' : posts
	}
	return render(request, 'blog/home.html', context)

def about (request):
	return render(request, 'blog/about.html')
