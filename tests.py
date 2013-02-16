import unittest

from markdown import markdown


class LinkifyTest(unittest.TestCase):
    def test_link(self):
        expected = '<p><a href="http://example.org/">http://example.org/</a></p>'
        actual = markdown("http://example.org/", extensions=["linkify"])
        self.assertEqual(expected, actual)

    def test_no_link(self):
        expected = '<p>example.org</p>'
        actual = markdown("example.org", extensions=["linkify"])
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
