from django.shortcuts import render
from markdown2 import markdown
from . import util
from random import randint
from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def render_page(request, title):
    if util.get_entry(title):
        return render(request, "encyclopedia/article.html", {
            "title": title,
            "entry": markdown(util.get_entry(title))
        })
    return render(request, "encyclopedia/article_not_found.html", {
             "title": title
        })


def random_entry(request):
    entries = util.list_entries()

    if entries:
        random_page = entries[randint(0, len(entries)) - 1]
        return HttpResponseRedirect(random_page)
    return HttpResponseRedirect(reverse("index"))

