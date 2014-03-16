import sys
import unittest

from markdown import markdown, Markdown

is_python3 = sys.version_info >= (3, 0)

if is_python3:
    from mdx_linkify.mdx_linkify import LinkifyExtension
else:
    from mdx_linkify import LinkifyExtension


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
        src = "http://example.com/monty.jpg"
        alt = "Monty"

        # Order is not guaranteed so we check both possibilities.
        expected_1 = '<p><img src="{}" alt="{}"></p>'.format(src, alt)
        expected_2 = '<p><img alt="{}" src="{}"></p>'.format(alt, src)
        actual = markdown("![Monty]({})".format(src), extensions=["linkify"])
        try:
            self.assertEqual(expected_1, actual)
        except AssertionError:
            self.assertEqual(expected_2, actual)

    def test_no_escape(self):
        expected = '<script>alert(1)</script>'
        actual = markdown(expected, extensions=["linkify"])
        self.assertEqual(expected, actual)

    def test_callbacks(self):
        def dont_linkify_py_tld(attrs, new=False):
            if not new:  # This is an existing <a> tag, leave it be.
                return attrs

            # If the TLD is '.py', make sure it starts with http: or https:
            text = attrs['_text']
            if (text.endswith('.py') and
                not text.startswith(('www.', 'http:', 'https:'))):
                # This looks like a Python file, not a URL. Don't make a link.
                return None

            # Everything checks out, keep going to the next callback.
            return attrs

        configs = {
            'linkify_callbacks': [[dont_linkify_py_tld], '']
        }
        linkify_extension = LinkifyExtension(configs=configs)
        md = Markdown(extensions=[linkify_extension])

        text = "setup.com www.setup.py http://setup.py setup.py"
        expected = ('<p><a href="http://setup.com">setup.com</a> '
                    '<a href="http://www.setup.py">www.setup.py</a> '
                    '<a href="http://setup.py">http://setup.py</a> '
                    'setup.py</p>')
        actual = md.convert(text)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
