from django.shortcuts import render
from django.utils import timezone
from .models import Post
from administration.models import Page
from administration.models import Slider
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    sliders = Slider.objects.all().order_by('position')
    page = request.GET.get('page',1)
    paginator = Paginator(posts,2) #Show 6 element for page
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
        
    return render(request, 'blog/post_list.html',{'posts':posts,'sliders':sliders})

def post_detail(request, pk):
    content = get_object_or_404(Post, pk=pk)
    sourse = "post"
    return render(request, 'blog/post_detail.html', {'content': content,'sourse':sourse})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def page_detail(request, pk):
    content = get_object_or_404(Page, pk=pk)
    sourse = "page"
    return render(request, 'blog/post_detail.html', {'content': content,'sourse':sourse})