from django.test import TestCase

from .models import Note


class NoteModelTests(TestCase):
    def test_repr_returns_string(self):
        note = Note.objects.create(title="Test", content="Sample content")

        representation = repr(note)

        self.assertEqual(representation, "Test")
