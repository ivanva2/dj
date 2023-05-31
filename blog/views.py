from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
# Create your views here.
from blog.models import Post
class PostListView(ListView):
     queryset = Post.objects.filter(status=Post.PostStatus.PUBLISHED)
     context_object_name = 'posts'
     paginate_by = 5
     template_name = 'blog/post/list.html'

def post_detail(request, year, month,day, post):
    post= get_object_or_404(Post, slug= post,
                            status='published',
                            publish__year=year,
                            publish__month= month,
                            publish__day=day   )
    return render(request, 'blog/post/detail.html', {'post': post} )