from django.shortcuts import render
from .models import Post
# Create your views here.
def home(request):
    allPosts = Post.objects.order_by('-TimeStamp')
    context = {'allPosts':allPosts}
    return render(request, 'blog/home.html', context)

def blogPost(request, slug):
    post = Post.objects.filter(Slug=slug).first()#or in place of .first() [0]
    context = {"post": post}
    return render(request, 'blog/blogPost.html', context)

def searchBlog(request):
    query=request.GET['query']
    if len(query) > 50:
        searchPosts=Post.objects.none()
    else:
        searchPostsTitle = Post.objects.filter(Title__icontains=query)
        searchPostsBody = Post.objects.filter(Body__icontains=query)
        searchPosts = searchPostsTitle.union(searchPostsBody)
    context = {'searchPosts':searchPosts, 'query': query}
    return render(request, 'blog/search.html', context)