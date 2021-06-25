from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from .forms import NoteModelForm
from .models import Note


# Create your views here.
""" ------------------------------Note Views here------------------"""


@login_required
def note_view_list(request):
    obj = Note.objects.all()
    context = {
        "form": obj
    }
    template = "form_view_list.html"

    return render(request, template, context)


""" --------------------Note create ---------------------"""


@login_required
def note_create_view(request):
    if request.method == "POST":
        form = NoteModelForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            print("success upload")
            return HttpResponseRedirect("/notes/")
    else:
        form = NoteModelForm()
    return render(request, "form_create.html", {"form": form})


""" -------------Update Note--------------"""


@login_required
def note_update_view(request, id):
    obj = Note.objects.get(id=id)

    # print(obj.user)
    # print(request.user)

    """ -------------authentication-----------------"""
    # if obj.user is not request.user:
    #     raise Http404("Operation is not allowed")

    if request.method == "POST":
        form = NoteModelForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            print("success updated!!")
            return HttpResponseRedirect("/notes/")
        else:
            print(form.errors)
    else:
        form = NoteModelForm(instance=obj)
    context = {
        "form": form
    }
    return render(request, "form_update.html", context)


"""---------------- Delete notes ----------"""


def note_delete_view(request, id):
    obj = Note.objects.get(id=id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/notes/")

    template = "form_delete.html"
    context = {
        "object": obj
    }
    return render(request, template, context)
