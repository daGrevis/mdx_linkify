# Mdx Linkify

[![Build Status](https://travis-ci.org/daGrevis/mdx_linkify.png?branch=master)](https://travis-ci.org/daGrevis/mdx_linkify)

This extension for [Python Markdown](https://github.com/waylan/Python-Markdown) will convert all links to HTML anchors.

There's [an existing solution](https://github.com/r0wb0t/markdown-urlize) for parsing links with regexes. Mdx Linkify is a bit smarter and asks [Bleach](https://github.com/jsocol/bleach) to parse them. :clap:

## An Example

    >>> from markdown import markdown
    >>> text = "http://example.org/"
    >>> markdown(text)
    u'<p>http://example.org/</p>'
    >>> markdown(text, extensions=["linkify"])
    u'<p><a href="http://example.org/">http://example.org/</a></p>'

## Installation

Simple installation on current environment:

    pip install git+https://github.com/daGrevis/mdx_linkify@0.3

You can add it to `requirements.txt` too:

    echo 'git+https://github.com/daGrevis/mdx_linkify@0.3' >> requirements.txt

**P.S. Pay attention to `@0.3`. It's the version number!**

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
