# Mdx Linkify

[![Travis](https://img.shields.io/travis/daGrevis/mdx_linkify.svg)](https://travis-ci.org/daGrevis/mdx_linkify)
[![Coveralls](https://img.shields.io/coveralls/daGrevis/mdx_linkify.svg)](https://coveralls.io/r/daGrevis/mdx_linkify?branch=master)
[![PyPI](https://img.shields.io/pypi/v/mdx_linkify.svg)](https://pypi.python.org/pypi/mdx_linkify)
[![PyPI](https://img.shields.io/pypi/pyversions/mdx_linkify.svg)](https://pypi.python.org/pypi/mdx_linkify)

This extension for [Python Markdown](https://github.com/waylan/Python-Markdown)
will convert text that look like links to HTML anchors.

There's an alternative package that serves the same purpose called
[`markdown-urlize`](https://github.com/r0wb0t/markdown-urlize). The main
difference is that [`mdx_linkify`](https://github.com/daGrevis/mdx_linkify) is
utilizing the excellent [`bleach`](https://github.com/jsocol/bleach) for
searching links in text. :clap:

## Usage

### Minimal Example

```python
from markdown import markdown

markdown("minimal http://example.org/", extensions=["mdx_linkify"])
# Returns '<p>minimal <a href="http://example.org/">http://example.org/</a></p>'
```

### Linkify Callbacks

It's possible to omit links that match your custom filter with linkify
callbacks.

For example, to omit links that end with `.net` extension:

```python
from mdx_linkify.mdx_linkify import LinkifyExtension
from markdown import Markdown

def dont_linkify_net_extension(attrs, new=False):
    if attrs["_text"].endswith(".net"):
        return None

    return attrs

md = Markdown(
    extensions=[LinkifyExtension(linkify_callbacks=[dont_linkify_net_extension])],
)

assert md.convert("not_link.txt"), '<p>not_link.txt</p>'

expected = md.convert("example.com")
actual = '<p><a href="http://example.com">example.com</a></p>'
assert expected == actual
```

## Installation

The project is [on PyPI](https://pypi.python.org/pypi/mdx_linkify)!

    pip install mdx_linkify

If you want the bleeding-edge version (this includes unreleased-to-PyPI code),
you can always grab the master branch directly from Git.

    pip install git+git://github.com/daGrevis/mdx_linkify.git

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

## Releasing

_(more like a cheatsheet for me actually)_

- Change version in `setup.py`,
- Commit and tag it,
- Push it (including tag),
- Run `python setup.py register && python setup.py sdist upload`;
