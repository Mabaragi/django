from django.shortcuts import render, redirect
from .forms import ArticleForm
from .models import Article

# Create your views here.

def index(request):
    articles = Article.objects.all()

    context = {
        'articles' : articles,
    }

    return render(request, 'articles/index.html', context)

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            article = Article(title=title, content=content)
            article.save()
            return redirect('articles:detail', pk=article.pk)
    elif request.method =='GET':
        form = ArticleForm()
    context = {
    'form': form
    }
    return render(request, 'articles/create.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', pk=article.pk)
    elif request.method =='GET':
        form = ArticleForm(instance=article)
    context = {
    'form': form,
    'article': article,
    }
    return render(request, 'articles/update.html', context)