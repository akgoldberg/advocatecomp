from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response, redirect
from .models import Contact, Post # '.' signifies the current directory
from django.db.models import ForeignKey

from django_tables2 import RequestConfig, SingleTableView
from tables import ContactTable
from filters import ContactFilter
from forms import ContactFormHelper

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import PasswordChangeForm


class LoggedInMixin(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoggedInMixin, self).dispatch(*args, **kwargs)

@login_required
def updates(request):
	template_name = 'updates.html'
	latest_news_list = Post.objects.all().order_by('-pub_date')[:20]
	context = {'latest_news_list': latest_news_list}
	return render(request, template_name, context)

@login_required
def profile(request, contact_id):
	template_name = 'profile.html'
	c = get_object_or_404(Contact, pk=contact_id)
	context = {'contact': c}
	return render(request, template_name, context)

def model_to_dict(instance):
    data = {}
    for field in instance._meta.fields:
        data[field.name] = field.value_from_object(instance)
        if isinstance(field, ForeignKey):
            data[field.name] = field.rel.to.objects.get(pk=data[field.name])
    return data

@login_required
def edit_user(request):
    # change the password
    user=request.user
    success = False
    form = PasswordChangeForm(user)
    template_name = 'edit_profile.html'
    fields = model_to_dict(user.contact)
    if request.method == 'POST':
        form = PasswordChangeForm(user=user, data=request.POST)
        if form.is_valid():
            form.save()
            success = True
    context = {'form': form, 'user' : user, 'success':success, 'fields':fields}
    return render(request, template_name, context)


# Used http://stackoverflow.com/questions/21449563/handle-django-filter-form-with-split-fields-using-django-crispy-forms
class FilteredSingleTableView(LoggedInMixin, SingleTableView):
    model = Contact
    table_class = ContactTable
    filter_class = ContactFilter
    helper_class = ContactFormHelper
    formhelper_class = ContactFormHelper
    context_filter_name = 'filter'

    def get_queryset(self, **kwargs):
        qs = super(FilteredSingleTableView, self).get_queryset()
        self.filter = self.filter_class(self.request.GET, queryset=qs)
        self.filter.form.helper = self.formhelper_class()
        return self.filter.qs

    def get_context_data(self, **kwargs):
        context = super(FilteredSingleTableView, self).get_context_data(**kwargs)
        context[self.context_filter_name] = self.filter
        return context