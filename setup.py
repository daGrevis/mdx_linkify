#!/usr/bin/env python2
from distutils.core import setup


setup(name="mdx_linkify",
      version="0.2",
      description="Link recognition for Python Markdown",
      author="Raitis (daGrevis) Stengrevics",
      author_email="dagrevis@gmail.com",
      url="https://github.com/daGrevis/mdx_linkify",
      packages=["mdx_linkify"],
      install_requires=["Markdown>=2.4", "bleach>=1.4"])
