from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post, PostCategory, Tag

def index(request):
    posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 6) # 6 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/blog.html', {'page_obj': page_obj})

def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    
    # Increment views count
    post.views_count += 1
    post.save(update_fields=['views_count'])
    
    # Get 3 random posts
    similar_posts = Post.objects.exclude(id=post.id).order_by('?')[:3]
    
    # Get all categories and tags
    categories = PostCategory.objects.all()
    tags = Tag.objects.all()
    
    return render(request, 'blog/blog_detail.html', {
        'post': post, 
        'similar_posts': similar_posts,
        'categories': categories,
        'tags': tags
    })
