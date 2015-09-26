from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from models import *

# Create your views here.
def updates(request):
	template_name = 'updates.html'
	latest_news_list = Post.objects.all().order_by('-pub_date')[:20]
	context = {'latest_news_list': latest_news_list}
	return render(request, template_name, context)

def profile(request, user_id):
	u = get_object_or_404(User, pk=user_id)
	return render(request, 'profile.html', {'user': u})