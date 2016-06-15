import unittest
from noteapp import NotesApplication


class TestNoteAppClass(unittest.TestCase):

    def setUp(self):
        self.note_app = NotesApplication("Ben")

    def test_init(self):
        self.assertEqual(self.note_app.author, 'Ben',
                         msg="author attribute is incorrect")
        self.assertEqual(self.note_app.notes, [],
                         msg="notes attribute is incorrect")

    def test_create(self):
        self.note_app.create("Note 0")
        self.assertEqual(len(self.note_app.notes), 1,
                         msg="notes not added correctly")

    def test_list(self):
        sample_out = "Note ID: 0\nNote 0\n\nBy Author Ben\n"
        self.assertEqual(self.note_app.list(), sample_out,
                         msg="notes not listed correctly")

if __name__ == '__main__':
    unittest.main()
