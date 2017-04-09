from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import Post
from .forms import PostForm
from urllib import quote_plus

# Create your views here.

def post_create(request):
     form = PostForm(request.POST or None, request.FILES or None)
     if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
        
     #if request.method == "POST" :
	    #print request.POST.get("title")
	    #print request.POST.get("content")
     context = {
	    "form" : form,
	 }
     return render(request, "post_form.html",context)
	 
	 
def post_detail(request, id):
     instance = get_object_or_404(Post, id=id)
     share_string = quote_plus(instance.content)
     context = {
          "instance" : instance,
          "title" : instance.title,
	 }
     return render(request, "post_detail.html",context)
	 
	 
def post_list(request):
    queryset_list = Post.objects.all().order_by("-timestamp")
    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(title__icontains=query)

    paginator = Paginator(queryset_list, 5) 
    page_request_var ="page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
		
    context = {
	      "object_list" : queryset,
	      "title" : "list",
		  "page_request_var":page_request_var
		  }
    return render(request, "post_list.html",context)
     #return HttpResponse("<h1>hello</h1>")
	
	 
	 
def post_update(request, id=None):
     instance = get_object_or_404(Post, id=id)
     form = PostForm(request.POST or None, request.FILES or None, instance=instance)
     if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "item saved" )
        return HttpResponseRedirect(instance.get_absolute_url())
     
        
     context = {
          "instance" : instance,
          "title" : instance.title,
		  "form" : form,
	 }
     return render(request, "post_form.html",context)
	 
	 
def post_delete(request, id=None):
     instance = get_object_or_404(Post, id=id)
     instance.delete()
     return render(request, "post_delete.html")
     
