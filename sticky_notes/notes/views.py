from django.shortcuts import get_object_or_404, redirect, render

from .forms import StickyNoteForm
from .models import StickyNote


def note_list(request):
    notes = StickyNote.objects.all().order_by("-created_at")
    return render(request, "notes/note_list.html", {"notes": notes})


def note_detail(request, pk):
    note = get_object_or_404(StickyNote, pk=pk)
    return render(request, "notes/note_detail.html", {"note": note})


def note_create(request):
    if request.method == "POST":
        form = StickyNoteForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("note_list")

    else:
        form = StickyNoteForm()

    return render(request, "notes/note_form.html", {"form": form})


def note_update(request, pk):
    note = get_object_or_404(StickyNote, pk=pk)

    if request.method == "POST":
        form = StickyNoteForm(request.POST, instance=note)

        if form.is_valid():
            form.save()
            return redirect("note_detail", pk=note.pk)

    else:
        form = StickyNoteForm(instance=note)

    return render(request, "notes/note_form.html", {"form": form})


def note_delete(request, pk):
    note = get_object_or_404(StickyNote, pk=pk)
    note.delete()
    return redirect("note_list")
