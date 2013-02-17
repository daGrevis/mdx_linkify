#!/usr/bin/env python2
from distutils.core import setup


setup(name="mdx_linkify",
      version="0.1",
      description="Link recognition for Python Markdown",
      author="Raitis (daGrevis) Stengrevics",
      author_email="dagrevis@gmail.com",
      url="https://github.com/daGrevis/mdx_linkify",
      packages=["mdx_linkify"],
      requires=["Markdown (>=2.2.1)", "bleach (>=1.2)"])
