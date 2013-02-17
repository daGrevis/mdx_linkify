# Mdx Linkify

This extension for [Python Markdown](https://github.com/waylan/Python-Markdown) will convert all links to HTML anchors using [Python Bleach](https://github.com/jsocol/bleach).

There's an existing solution that tries to do the same. The main difference from mine extension is that it uses regexes to do that instead of a tool that's made for the job.

## An example

    >>> from markdown import markdown
    >>> text = "Hello, world! Here a [Markdown link](http://example.com/), but here's a plain link -- http://example.org/."
    >>> markdown(text)
    u'<p>Hello, world! Here a <a href="http://example.com/">Markdown link</a>, but here\'s a plain link -- http://example.org/.</p>'
    >>> markdown(text, extensions=["linkify"])
    u'<p>Hello, world! Here a <a href="http://example.com/">Markdown link</a>, but here\'s a plain link -- <a href="http://example.org/">http://example.org/</a>.</p>'

## Installation

    pip install git+https://github.com/daGrevis/mdx_linkify
