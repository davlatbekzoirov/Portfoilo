from django.shortcuts import render, get_object_or_404
from .models import Blog, Portfolio

def index(request):
    blog = Blog.objects.all()
    portfolio = Portfolio.objects.all()
  
    context = {
        "blogs": blog,
        "portfolios": portfolio
    }

    return render(request, 'index.html', context)

def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'blog.html', {'blog': blog})

def portfolio_detail(request, slug):
    portfolio = get_object_or_404(Portfolio, slug=slug)
    return render(request, 'portfolio_detail.html', {'portfolio': portfolio})


def two(request):
    return render(request, '404.html')