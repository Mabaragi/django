from django.shortcuts import render, redirect
from .models import Articles

# Create your views here.
def index(request):
    articles = Articles.objects.all()
    context = {
        'articles': articles,
    }

    return render(request, 'articles/index.html', context)

def detail(request, pk):
    article = Articles.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    article = Articles()
    article.title=title
    article.content=content
    article.save()

    context = {
        'article': article
    }

    return redirect('articles:detail', pk=article.pk)

def edit(request, pk):
    article = Articles.objects.get(pk=pk)
    context = {
        'article': article,
    }

    return render(request, 'articles/edit.html', context)

def update(request, pk):
    title = request.POST.get('title')
    content = request.POST.get('content')
    article = Articles.objects.get(pk=pk)
    article.title=title
    article.content=content
    article.save()
    return redirect('articles:detail', pk=article.pk)

def delete(request, pk):
    article = Articles.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')