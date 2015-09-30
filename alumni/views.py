from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from models import *
from django_tables2 import RequestConfig
from tables import UserTable
from filters import UserFilter

# Create your views here.
def updates(request):
	template_name = 'updates.html'
	latest_news_list = Post.objects.all().order_by('-pub_date')[:20]
	context = {'latest_news_list': latest_news_list}
	return render(request, template_name, context)

def profile(request, user_id):
	template_name = 'profile.html'
	u = get_object_or_404(User, pk=user_id)
	context = {'user': u}
	return render(request, template_name, context)

def alumnidb(request):
	template_name = 'alumni.html'
	queryset = User.objects.all()
	f = UserFilter(request.GET, queryset=queryset)
	table = UserTable(f.qs)
	RequestConfig(request, paginate={"per_page": 25, "page": 1}).configure(table)
	return render(request, template_name, {'table': table, 'filter': f})