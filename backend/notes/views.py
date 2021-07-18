# from django.shortcuts import render
# from django.http import HttpResponseRedirect, Http404
# from django.contrib.auth.decorators import login_required
# from .forms import NoteModelForm
# from .models import Note
#


from django.core import serializers
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from .forms import NoteModelForm
from .models import Note


# Create your views here.
def notes_view_list(request):
    obj = Note.objects.all()
    template = 'notes/notes_list_view.html'
    print(obj)
    context = {
        "form": obj
    }
    return render(request, template, context)


# create note
def notes(request):
    obj1 = Note.objects.all()
    template = "notes/notes_create_view.html"
    if request.method == 'POST':
        form = NoteModelForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()

            return HttpResponseRedirect('/notes/create/')
    else:
        form = NoteModelForm()
        context = {
            "form": form,
            "fetchData": obj1
        }

    return render(request, template, context)


# delete note
def notes_delete_view(request):
    if request.method == "POST":
        id = request.POST.get('nId')
        if id is not None:
            note = Note.objects.get(id=id)
        note.delete()
        return JsonResponse({"status": 1})
    else:
        return JsonResponse({"status": 0})


# edit note get data
def notes_edit_view(request):
    if request.method == "POST":
        id = request.POST.get("nId")
        note = Note.objects.get(id=id)
        noteData = {"id": note.id, "title": note.title, "semester": note.semester, "subject": note.subject, "file":
            note.file.name, "description": note.description}
        # noteData = serializers.serialize('json', [note, ])
        return JsonResponse({"note": noteData}, status=200)


# edit note save
def notes_edit_save_view(request):
    if request.method == "POST":
        filename = request.FILES.get('file')
        id = request.POST.get('noteId')

        title = request.POST.get('title')
        semester = request.POST.get('semester')
        subject = request.POST.get('subject')
        description = request.POST.get('description')

        note_obj = Note.objects.get(id=id)
        note_form = NoteModelForm(request.POST, request.FILES, instance=note_obj)
        if note_form.is_valid():
            note_form.save()
            note_all = Note.objects.values()

        if filename is None:
            print(note_obj.file)
            print(note_obj.timestamp)
            note = Note(id=id, user=request.user, title=title, semester=semester, subject=subject,
                                      file=note_obj.file, description=description, timestamp=note_obj.timestamp)
            note.save()
            note_all = Note.objects.values()

        note_all_data = list(note_all)

        return JsonResponse({"status": 200, 'noteData': note_all_data})


def note_details(request):
    obj = Note.objects.all()
    template = "notes/note_details_view.html"
    context = {
        "file": obj[0].file
    }

    return render(request, template, context)





































#
# # Create your views here.
# """ ------------------------------Note Views here------------------"""
#
#
# @login_required
# def note_view_list(request):
#     obj = Note.objects.all()
#     context = {
#         "form": obj
#     }
#     template = "form_view_list.html"
#
#     return render(request, template, context)
#
#
# """ --------------------Note create ---------------------"""
#
#
# @login_required
# def note_create_view(request):
#     if request.method == "POST":
#         form = NoteModelForm(request.POST, request.FILES)
#         if form.is_valid():
#             note = form.save(commit=False)
#             note.user = request.user
#             note.save()
#             print("success upload")
#             return HttpResponseRedirect("/notes/")
#     else:
#         form = NoteModelForm()
#     return render(request, "form_create.html", {"form": form})
#
#
# """ -------------Update Note--------------"""
#
#
# @login_required
# def note_update_view(request, id):
#     obj = Note.objects.get(id=id)
#
#     # print(obj.user)
#     # print(request.user)
#
#     """ -------------authentication-----------------"""
#     # if obj.user is not request.user:
#     #     raise Http404("Operation is not allowed")
#
#     if request.method == "POST":
#         form = NoteModelForm(request.POST, request.FILES, instance=obj)
#         if form.is_valid():
#             form.save()
#             print("success updated!!")
#             return HttpResponseRedirect("/notes/")
#         else:
#             print(form.errors)
#     else:
#         form = NoteModelForm(instance=obj)
#     context = {
#         "form": form
#     }
#     return render(request, "form_update.html", context)
#
#
# """---------------- Delete notes ----------"""
#
#
# def note_delete_view(request, id):
#     obj = Note.objects.get(id=id)
#     if request.method == "POST":
#         obj.delete()
#         return HttpResponseRedirect("/notes/")
#
#     template = "form_delete.html"
#     context = {
#         "object": obj
#     }
#     return render(request, template, context)
