from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from myapp.models import Document
from myapp.forms import DocumentForm

def home(request):
    return render_to_response('home.html')

def club(request):
    return render_to_response('clubs.html')
def about(request):
    return render_to_response('about.html')

def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('myproject.myapp.views.list'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'list_0.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )

# def index(request):
#     return render_to_response('index2.html')