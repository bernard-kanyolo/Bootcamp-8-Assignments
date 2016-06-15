import unittest
from noteapp import NotesApplication


class TestNoteAppClass(unittest.TestCase):
    """Testing the Notes Application class
    """

    def setUp(self):
        """Instantiate the class
        """
        self.note_app = NotesApplication("Ben")
        self.note_app.create("Note 0")

    def test_init(self):
        """Test whether creating the class does the correct thing
        and the instance variables are correct
        """
        self.assertEqual(self.note_app.author, 'Ben',
                         msg="author attribute is incorrect")
        self.assertEqual(self.note_app.notes, ["Note 0"],
                         msg="notes attribute is incorrect")

    def test_create(self):
        """Test adding of notes
        """
        self.assertEqual(len(self.note_app.notes), 1,
                         msg="notes not added correctly")

    def test_list(self):
        """Test print outs of the lists
        """
        self.note_app.list()

    def test_get(self):
        """Test if get returns the correct value regardless of the
        note_id
        """
        self.assertEqual(self.note_app.get(0), "Note 0",
                         msg="Incorrect get method")
        self.assertEqual(self.note_app.get(-1), None,
                         msg="invalid index should return None")


if __name__ == '__main__':
    unittest.main()
