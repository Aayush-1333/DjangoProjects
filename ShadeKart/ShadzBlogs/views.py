from django.shortcuts import render
from .models import Blogpost
from django.http import HttpRequest


# Create your views here.
def index(request):
    """renders ShadzBlogs homepage"""
    return render(request, 'ShadzBlogs/siteIndex.html')


def about(request):
    """renders ShadzBlogs homepage"""
    return render(request, 'ShadzBlogs/about.html')


def officialPost1(request):
    """returns the view of official posts from the company"""
    return render(request, 'ShadzBlogs/official1.html')


def officialPost2(request):
    """returns the view of official posts from the company"""
    return render(request, 'ShadzBlogs/official2.html')


def searchMatch(query, posts):
    res = []
    for post in posts:
        if (query in post['writer'].lower() or query in post['writer']) \
                or (query in post['title'].lower() or query in post['title']):
            res.append(post)

    return res


def search(request):
    """Searches the blogs from the database according to user's query"""
    query = request.GET.get('search', '')
    articles = Blogpost.objects.values()
    searched_articles = searchMatch(query, articles)
    num_of_posts = len(searched_articles)
    if num_of_posts != 0:
        posts = [article for article in searched_articles]
    else:
        posts = []

    return render(request, 'ShadzBlogs/search.html', {'posts': posts, 'num_posts': num_of_posts})


def blogPost(request):
    """returns the posts that are there in the database"""
    articles = Blogpost.objects.values()
    posts = [article for article in articles]

    return render(request, 'ShadzBlogs/blogPost.html', {'posts': posts})


def submitPost(request):
    """returns submit your post page"""
    if request.method == 'POST':
        print(request.POST)
        writer = request.POST.get('name', '')
        email = request.POST.get('email', '')
        postTitle = request.POST.get('blogTitle', '')
        title0 = request.POST.get('title1', '')
        titleContent0 = request.POST.get('titleContent1', '')
        title1 = request.POST.get('title2', '')
        titleContent1 = request.POST.get('titleContent2', '')
        title2 = request.POST.get('title3', '')
        titleContent2 = request.POST.get('titleContent3', '')
        thumbnail = request.POST.FILES
        blogpost = Blogpost(writer=writer, email=email, title=postTitle, thumbnail="ShadzBlogs/images/" + thumbnail, head0=title0, content_head0=titleContent0,
                            head1=title1, content_head1=titleContent1, head2=title2, content_head2=titleContent2)
        blogpost.save()

    return render(request, 'ShadzBlogs/submitPost.html')


def postView(request, postId):
    """returns the page where user can view the posts on ShadzBlogs"""
    num_of_posts = len(Blogpost.objects.values())
    prev_post = Blogpost.objects.filter(post_id=postId - 1)
    prev_post_len = len(prev_post)
    post = Blogpost.objects.filter(post_id=postId)
    next_post = Blogpost.objects.filter(post_id=postId + 1)
    next_post_len = len(next_post)
    return render(request, 'ShadzBlogs/postView.html',
                  {'post': post[0], 'prev_post': prev_post, 'prev_len': prev_post_len,
                   'next_post': next_post, 'next_len': next_post_len, 'num_posts': num_of_posts})
