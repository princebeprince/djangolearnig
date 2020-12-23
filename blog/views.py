from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from . import models

# Create your views here.
def bloghome(request):
    blogs = models.blog.objects.order_by('-date')
    return render(request,'blog/bloghome.html',{"blogs": blogs})

def details(request , blog_id):
    blog = get_object_or_404(models.blog , pk=blog_id)
    return render(request,'blog/details.html',{"blog":blog})