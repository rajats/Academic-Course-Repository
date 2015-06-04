from django.shortcuts import render_to_response, RequestContext, Http404,HttpResponseRedirect
from django.contrib.contenttypes.models import ContentType
from django.db.models import Count

def home(request):
	return render_to_response("home.html", locals(), context_instance=RequestContext(request))


