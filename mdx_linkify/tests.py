import unittest

from markdown import markdown


class LinkifyTest(unittest.TestCase):
    def test_link(self):
        expected = '<p><a href="http://example.com">http://example.com</a></p>'
        actual = markdown("http://example.com", extensions=["linkify"])
        self.assertEqual(expected, actual)

    def test_https_link(self):
        link = "https://example.com"
        expected = '<p><a href="{link}">{link}</a></p>'.format(link=link)
        actual = markdown(link, extensions=["linkify"])
        self.assertEqual(expected, actual)

    def test_complex_link(self):
        link = "http://spam.cheese.bacon.eggs.io/?monty=Python#im_loving_it"
        expected = '<p><a href="{link}">{link}</a></p>'.format(link=link)
        actual = markdown(link, extensions=["linkify"])
        self.assertEqual(expected, actual)

    def test_no_link(self):
        expected = '<p>foo.bar</p>'
        actual = markdown("foo.bar", extensions=["linkify"])
        self.assertEqual(expected, actual)

    def test_links(self):
        expected = ('<p><a href="http://example.com">http://example.com</a> '
                    '<a href="http://example.org">http://example.org</a></p>')
        actual = markdown("http://example.com http://example.org",
                          extensions=["linkify"])
        self.assertEqual(expected, actual)

    def test_links_with_text_between(self):
        expected = ('<p><a href="http://example.com">http://example.com</a> '
                    'foo <a href="http://example.org">http://example.org'
                    '</a></p>')
        actual = markdown("http://example.com foo http://example.org",
                          extensions=["linkify"])
        self.assertEqual(expected, actual)

    def test_existing_link(self):
        expected = '<p><a href="http://example.com">http://example.com</a></p>'
        actual = markdown("[http://example.com](http://example.com)",
                          extensions=["linkify"])
        self.assertEqual(expected, actual)

    def test_image_that_has_link_in_it(self):
        link = "http://example.com/monty.jpg"
        expected = '<p><img alt="Monty" src="{0}"></p>'.format(link)
        actual = markdown("![Monty]({0})".format(link), extensions=["linkify"])
        self.assertEqual(expected, actual)

    def test_no_escape(self):
        expected = '<script>alert(1)</script>'
        actual = markdown(expected, extensions=["linkify"])
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
