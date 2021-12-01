import markdown2
from django.shortcuts import render

from . import util


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
