"""Book models test cases."""
from odoo.tests import common


class TestAuthor(common.TransactionCase):
    """Author model test cases."""

    def setUp(self, *args, **kwargs):
        super(TestAuthor, self).setUp(*args, **kwargs)

        user_data = {"login": "testuser"}
        self.user = self.env["res.users"].create(user_data)

        library_data = {
            "user": self.user.id,
            "name": "Test Library",
            "address": "Work",
            "library_type": "PUBLIC",
            "phone_number": "+254711234567",
            "email": "public@library.edu",
        }
        self.library = self.env["library"].create(library_data)

    def test_author_creation(self):
        """Verify successful creation of an author."""
        data = {"name": "Author Writer"}
        record = self.env["author"].create(data)
        self.assertEqual(record.name, "Author Writer")
