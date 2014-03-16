# Mdx Linkify

[![Build Status](https://travis-ci.org/daGrevis/mdx_linkify.png?branch=master)](https://travis-ci.org/daGrevis/mdx_linkify)
[![Coverage Status](https://coveralls.io/repos/daGrevis/mdx_linkify/badge.png?branch=master)](https://coveralls.io/r/daGrevis/mdx_linkify?branch=master)

This extension for [Python Markdown](https://github.com/waylan/Python-Markdown) will convert all links to HTML anchors.

There's [an existing solution](https://github.com/r0wb0t/markdown-urlize) for parsing links with regexes. Mdx Linkify is a bit smarter and asks [Bleach](https://github.com/jsocol/bleach) to parse them. :clap:

## An Example

### Basic Usage

    >>> from markdown import markdown
    >>> text = "http://example.org/"
    >>> markdown(text)
    u'<p>http://example.org/</p>'
    >>> markdown(text, extensions=["linkify"])
    u'<p><a href="http://example.org/">http://example.org/</a></p>'

### Linkify Callbacks

    >>> from markdown import Markdown
    >>> text = "http://example.org/"
    >>> def dont_linkify_py_tld(attrs, new=False):
    >>>     if not new:  # This is an existing <a> tag, leave it be.
    >>>         return attrs
    >>>
    >>>     # If the TLD is '.py', make sure it starts with http: or https:
    >>>     text = attrs['_text']
    >>>     if (text.endswith('.py') and
    >>>         not text.startswith(('www.', 'http:', 'https:'))):
    >>>         # This looks like a Python file, not a URL. Don't make a link.
    >>>         return None
    >>>
    >>>     # Everything checks out, keep going to the next callback.
    >>>     return attrs
    >>> configs = {
    >>>     'linkify_callbacks': [[dont_linkify_py_tld], '']
    >>> }
    >>> linkify_extension = LinkifyExtension(configs=configs)
    >>> md = Markdown(extensions=[linkify_extension])
    >>> md.convert("https://setup.py")
    u'<p><a href="https://setup.py">https://setup.py</a></p>'
    >>> md.convert("setup.py")
    u'<p>setup.py</p>'

## Installation

Simple installation on current environment:

    pip install mdx_linkify

You can add it to `requirements.txt` too:

    echo 'mdx_linkify' >> requirements.txt

## Development

1. Fork repo,
2. Clone repo,
3. Create `virtualenv`,
4. Execute `python setup.py install`,
5. Add some awesome feature,
6. Check tests with `python setup.py test`,
7. Check `pep8`,
8. Add commit and push to forked repo,
9. Ask for a merge request,
10. Stay awesome! :+1:
