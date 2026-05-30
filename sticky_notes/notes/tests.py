from django.test import TestCase

from .models import StickyNote

from django.urls import reverse


class StickyNoteModelTest(TestCase):

    def setUp(self):

        StickyNote.objects.create(
            title="Shopping List",
            content="Milk and Bread"
        )

    def test_note_has_title(self):

        note = StickyNote.objects.get(id=1)

        self.assertEqual(
            note.title,
            "Shopping List"
        )

    def test_note_has_content(self):

        note = StickyNote.objects.get(id=1)

        self.assertEqual(
            note.content,
            "Milk and Bread"
        )


class StickyNoteViewTest(TestCase):

    def setUp(self):

        StickyNote.objects.create(
            title="Shopping List",
            content="Milk and Bread"
        )

    def test_note_list_view(self):

        response = self.client.get(
            reverse("note_list")
        )

        self.assertEqual(
            response.status_code,
            200
        )

        self.assertContains(
            response,
            "Shopping List"
        )

    def test_note_detail_view(self):

        note = StickyNote.objects.get(id=1)

        response = self.client.get(
            reverse(
                "note_detail",
                args=[str(note.id)]
            )
        )

        self.assertEqual(
            response.status_code,
            200
        )

        self.assertContains(
            response,
            "Shopping List"
        )

        self.assertContains(
            response,
            "Milk and Bread"
        )
