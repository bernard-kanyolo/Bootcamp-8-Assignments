import unittest
from noteapp import NotesApplication


class TestNoteAppClass(unittest.TestCase):
    """Testing the Notes Application class
    """

    def test_init_with_string(self):
        """test whether the right object is created when the
        constructor is called with a string
        """
        note_app = NotesApplication("")
        self.assertIsInstance(note_app, NotesApplication,
                              msg="init not working")

    def test_init_with_int(self):
        """test what happpens when an int is passed to constructor
        instead
        """
        note_app = NotesApplication(2)
        self.assertIsNone(note_app.author,
                          msg="init with int shouldn't set author variable")

    def test_init_with_dict(self):
        """test what happens when an dictionary is passed to the
        constructor instead
        """
        note_app = NotesApplication({})
        self.assertIsNone(note_app.author,
                          msg="init with dict shouldn't set author variable")

    def test_init_author_variable(self):
        """test whether the author instance variable is set properly
        """
        note_app = NotesApplication("Ben")
        self.assertEqual(note_app.author, "Ben",
                         msg="author attribute is incorrect")

    def test_init_notes_variable(self):
        """test if the notes list is created properly
        """
        note_app = NotesApplication("")
        self.assertListEqual(note_app.notes, [],
                             msg="notes attribute is incorrect")

    def test_create_with_string(self):
        """test whether adding a note works
        """
        note_app = NotesApplication("Ben")
        note_app.create("Note 0")

        self.assertEqual(len(note_app.notes), 1,
                         msg="notes not added correctly")

    def test_create_with_string2(self):
        """test if the notes list has the correct value
        """
        note_app = NotesApplication("Ben")
        note_app.create("Note 0")

        self.assertListEqual(note_app.notes, ["Note 0"],
                             msg="incorrect notes attribute after create")

    def test_create_with_int(self):
        """test if an int can be added as a note
        """
        note_app = NotesApplication("Ben")
        note_app.create(1)

        self.assertListEqual(note_app.notes, [1],
                             msg="incorrect notes attribute after create")

    def test_create_with_list(self):
        """test if a list can be used to create a note
        """
        note_app = NotesApplication("Ben")
        note_app.create([1, 2])

        self.assertListEqual(note_app.notes, [[1, 2]],
                             msg="incorrect notes attribute after create")

    def test_list(self):
        """Test print outs of the lists
        """
        note_app = NotesApplication("Ben")
        note_app.create("Note 0")

        note_app.list()

    def test_get_with_valid_index(self):
        """test normal get behaviour
        """
        note_app = NotesApplication("Ben")
        note_app.create("Note 0")

        self.assertEqual(note_app.get(0), "Note 0",
                         msg="Incorrect get method")

    def test_get_with_invalid_index(self):
        """test get with bad parameters
        """
        note_app = NotesApplication("Ben")
        note_app.create("Note 0")

        self.assertEqual(note_app.get(10), None,
                         msg="Invalid index should return None")

    def test_get_with_non_int_index(self):
        """test get with bad parameters
        """
        note_app = NotesApplication("Ben")
        note_app.create("Note 0")

        self.assertEqual(note_app.get(""), None,
                         msg="string index should return None")

    def test_search(self):
        """Test if search prints the right output"""
        note_app = NotesApplication("Ben")
        note_app.create("Note 0")

        note_app.search("Note")

    def test_edit_with_valid_parameters(self):
        """test for normal edit behaviour
        """
        note_app = NotesApplication("Ben")
        note_app.create("Note 0")

        self.assertTrue(note_app.edit(0, "New Note 0"),
                        msg="edit was unsuccessful")

    def test_edit_changes(self):
        """test if edit changes the right variable to the right
        value
        """
        note_app = NotesApplication("Ben")
        note_app.create("Note 0")
        note_app.edit(0, "New Note 0")

        self.assertEqual(note_app.notes[0], "New Note 0",
                         msg="edit value incorrect")

    def test_edit_changes_with_int(self):
        """test if edit changes the right variable to the right
        value
        """
        note_app = NotesApplication("Ben")
        note_app.create("Note 0")
        note_app.edit(0, 2)

        self.assertEqual(note_app.notes[0], 2,
                         msg="edit value incorrect")

    def test_edit_with_bad_index(self):
        """test if edit recongnizes bad indexes
        """
        note_app = NotesApplication("Ben")
        note_app.create("Note 0")

        self.assertFalse(note_app.edit(10, "New Note 0"),
                         msg="edit was unsuccessful")

    def test_edit_changes_with_list(self):
        """test if edit changes the right variable to the right
        value
        """
        note_app = NotesApplication("Ben")
        note_app.create("Note 0")
        note_app.edit(0, [1, 2])

        self.assertEqual(note_app.notes[0], [1, 2],
                         msg="edit value incorrect")

    def test_edit_changes_with_tuple(self):
        """test if edit changes the right variable to the right
        value
        """
        note_app = NotesApplication("Ben")
        note_app.create("Note 0")
        note_app.edit(0, (1, 2))

        self.assertEqual(note_app.notes[0], (1, 2),
                         msg="edit value incorrect")


if __name__ == '__main__':
    unittest.main()
