# Mdx Linkify

[![Build Status](https://travis-ci.org/daGrevis/mdx_linkify.png?branch=master)](https://travis-ci.org/daGrevis/mdx_linkify)
[![Coverage Status](https://coveralls.io/repos/daGrevis/mdx_linkify/badge.png?branch=master)](https://coveralls.io/r/daGrevis/mdx_linkify?branch=master)
[![PyPI Downloads](https://pypip.in/d/mdx_linkify/badge.png)](https://pypi.python.org/pypi/mdx_linkify)
[![PyPI Version](https://pypip.in/v/mdx_linkify/badge.png)](https://pypi.python.org/pypi/mdx_linkify)

This extension for [Python Markdown](https://github.com/waylan/Python-Markdown)
will convert all links to HTML anchors.

There's [an existing solution](https://github.com/r0wb0t/markdown-urlize) for
parsing links with regexes. Mdx Linkify is a bit smarter and asks
[Bleach](https://github.com/jsocol/bleach) to parse them. :clap:

## Usage

### Basic Example

By default, if you add `linkify` extension to `markdown` extensions...

```python
from markdown import markdown


text = "http://example.org/"

assert markdown(text) == "<p>http://example.org/</p>"

expected = markdown(text, extensions=["linkify"])
actual = '<p><a href="http://example.org/">http://example.org/</a></p>'
assert expected == actual
```

...it will automatically convert all links to HTML anchors.

### Linkify Callbacks

If you need callbacks, you can specify them by passing `LinkifyExtension` to
`Markdown`...

```python
from mdx_linkify.mdx_linkify import LinkifyExtension
from markdown import Markdown


def dont_linkify_txt_extension(attrs, new=False):
    if attrs["_text"].endswith(".txt"):
        return None

    return attrs

configs = {
    "linkify_callbacks": [[dont_linkify_txt_extension], ""]
}
linkify_extension = LinkifyExtension(configs=configs)
md = Markdown(extensions=[linkify_extension])

assert md.convert("not_link.txt"), '<p>not_link.txt</p>'

expected = md.convert("example.com")
actual = '<p><a href="http://example.com">example.com</a></p>'
assert expected == actual
```

...here, we only convert links that do **not** end with `.txt` extension.

## Installation

The project is [on PyPI](https://pypi.python.org/pypi/mdx_linkify)!

    pip install mdx_linkify

## Development

```
git clone git@github.com:daGrevis/mdx_linkify.git
virtualenv mdx_linkify/
cd mdx_linkify/
source bin/activate
python setup.py install
python setup.py test
```

Pull requests are much welcome! :+1:
