from __future__ import absolute_import
import unittest

from markdown import markdown, Markdown

from mdx_linkify.mdx_linkify import LinkifyExtension


class LinkifyTest(unittest.TestCase):
    def test_link(self):
        expected = '<p><a href="http://example.com">http://example.com</a></p>'
        actual = markdown("http://example.com", extensions=["mdx_linkify"])
        self.assertEqual(expected, actual)

    def test_https_link(self):
        link = "https://example.com"
        expected = '<p><a href="{link}">{link}</a></p>'.format(link=link)
        actual = markdown(link, extensions=["mdx_linkify"])
        self.assertEqual(expected, actual)

    def test_complex_link(self):
        link = "http://spam.cheese.bacon.eggs.io/?monty=Python#im_loving_it"
        expected = '<p><a href="{link}">{link}</a></p>'.format(link=link)
        actual = markdown(link, extensions=["mdx_linkify"])
        self.assertEqual(expected, actual)

    def test_no_link(self):
        expected = '<p>foo.bar</p>'
        actual = markdown("foo.bar", extensions=["mdx_linkify"])
        self.assertEqual(expected, actual)

    def test_links(self):
        expected = ('<p><a href="http://example.com">http://example.com</a> '
                    '<a href="http://example.org">http://example.org</a></p>')
        actual = markdown("http://example.com http://example.org",
                          extensions=["mdx_linkify"])
        self.assertEqual(expected, actual)

    def test_links_with_text_between(self):
        expected = ('<p><a href="http://example.com">http://example.com</a> '
                    'foo <a href="http://example.org">http://example.org'
                    '</a></p>')
        actual = markdown("http://example.com foo http://example.org",
                          extensions=["mdx_linkify"])
        self.assertEqual(expected, actual)

    def test_existing_link(self):
        expected = '<p><a href="http://example.com">http://example.com</a></p>'
        actual = markdown("[http://example.com](http://example.com)",
                          extensions=["mdx_linkify"])
        self.assertEqual(expected, actual)

    def test_backticks_link(self):
        expected = '<p><code>example.com</code></p>'
        actual = markdown("`example.com`",
                          extensions=["mdx_linkify"])
        self.assertEqual(expected, actual)

    def test_image_that_has_link_in_it(self):
        src = "http://example.com/monty.jpg"
        alt = "Monty"

        # Order is not guaranteed so we check for substring existence.
        actual = markdown("![Monty]({})".format(src), extensions=["mdx_linkify"])
        self.assertIn(src, actual)
        self.assertIn(alt, actual)

    def test_no_escape(self):
        expected = '<script>alert(1)</script>'
        actual = markdown(expected, extensions=["mdx_linkify"])
        self.assertEqual(expected, actual)

    def test_callbacks(self):
        def dont_linkify_net_extension(attrs, new=False):
            if attrs["_text"].endswith(".net"):
                return None

            return attrs

        # assert expected behavior WITHOUT our callback
        actual = markdown("https://linked.net",
                          extensions=["mdx_linkify"])
        expected = '<p><a href="https://linked.net">https://linked.net</a></p>'
        self.assertEqual(actual, expected)

        md = Markdown(
            extensions=[LinkifyExtension(linkify_callbacks=[dont_linkify_net_extension])],
        )

        # assert .net no longer works
        actual = md.convert("https://not-linked.net")
        expected = '<p>https://not-linked.net</p>'
        self.assertEqual(actual, expected)

        # assert other links still work
        actual = md.convert("example.com")
        expected = '<p><a href="http://example.com">example.com</a></p>'
        self.assertEqual(actual, expected)

        # assert that configuration parameters can be over-ridden at run time
        # https://python-markdown.github.io/extensions/api/#configsettings 
        expected = '<p><a href="https://not-linked.net">https://not-linked.net</a></p>'
        actual = markdown("https://not-linked.net",
                          extensions=["mdx_linkify"])
        self.assertEqual(expected, actual)

    def test_no_schema(self):
        expected = '<p><a href="http://example.com">example.com</a></p>'
        actual = markdown("example.com",
                          extensions=["mdx_linkify"])
        self.assertEqual(expected, actual)

    def test_email(self):
        expected = '<p><a href="mailto:contact@example.com">contact@example.com</a></p>'
        actual = markdown("contact@example.com", extensions=[LinkifyExtension(linkify_parse_email=True)])
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
