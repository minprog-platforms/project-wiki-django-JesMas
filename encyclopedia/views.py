from django.core.exceptions import ValidationError
import markdown2
from django import forms
from django.shortcuts import render
from django.http import HttpResponse

from . import util

def validate_entry(title):
    if title in util.list_entries():
        raise ValidationError("entry is already in wiki")

class NewEntry(forms.Form):
    title = forms.CharField(label="new_title", validators=[validate_entry])
    description = forms.CharField(label="new_description")

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def entry(request, TITLE):
    if util.get_entry(TITLE) == None:
        return render(request, "encyclopedia/error.html")
    return render(request, "encyclopedia/entry.html", {
        "entry": markdown2.markdown(util.get_entry(TITLE)),
        "title": TITLE
    })
def search(request):
    results = []
    entries = util.list_entries()
    query = request.GET.get('q')
    for entry in entries:
        if query == entry:
            return render(request, "encyclopedia/entry.html", {
                "entry": markdown2.markdown(util.get_entry(query)),
                "title": query
            })
        if entry.find(query) != -1:
            results.append(entry)
    return render(request, "encyclopedia/search.html", {
        "results": results
    })

def new(request):
    if request.method == "POST":
        form = NewEntry(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
        
            util.save_entry(title, description)

            return render(request, "encyclopedia/entry.html", {
                    "entry": markdown2.markdown(util.get_entry(title)),
                    "title": title
                })

        else:
            return HttpResponse(form.errors.values())
    else:
        return render(request, "encyclopedia/new.html", {
                    "form": NewEntry()
                })
