from django.shortcuts import render
import markdown2 as md

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def render_page(request, title):
    if util.get_entry(title):
        return render(request, "encyclopedia/article.html", {
            "title": title,
            "entry": md.markdown(util.get_entry(title))
        })
    return render(request, "encyclopedia/article_not_found.html", {
             "title": title
        })


