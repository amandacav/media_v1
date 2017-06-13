from django.shortcuts import render
## from nameform 
from .forms import NameForm
from django.http import HttpResponseRedirect



def index(request):
    return render (request, "store/base.html")

def login(request):
    return render (request, "store/login.html")

def get_services(request):
	result_set = []

## from nameform

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'store/name.html', {'form': form})

