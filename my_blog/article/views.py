from django.shortcuts import render,render_to_response

from django.http import HttpResponse
from django.template import RequestContext
from datetime import datetime
from django.http import Http404
from article.models import Article as Article_Mode

# Create your views here.
# def home(request):
#     return HttpResponse("Hello World, Django")
# def detail(request, my_args):
#     return HttpResponse("You're looking at my_args %s." % my_args
# def detail(request, my_args):
# 	post = Article_Mode.objects.all()[int(my_args)]
# 	str = ("title = %s, category = %s, date_time = %s, content = %s" % (post.title, post.category, post.date_time, post.content))
# 	return HttpResponse(str)


# Create your views here.
def home(request):
    post_list = Article_Mode.objects.all()

    return render_to_response('home.html', {'post_list' : post_list},context_instance=RequestContext(request))
def detail(request):
	id=request.GET.get('id')

	try:
		post = Article_Mode.objects.filter(id=id).get
		print post
	except Article_Mode.DoesNotExist:
		raise Http404
	return render_to_response('post.html', {'post' : post},context_instance=RequestContext(request))
