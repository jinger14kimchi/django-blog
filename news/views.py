from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import News
# from .forms import PostForm
from django.shortcuts import redirect

def news_list(request):
    news = News.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'news/news_list.html', {'news': news})


def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    return render(request, 'news/news_detail.html', {'news': news})
