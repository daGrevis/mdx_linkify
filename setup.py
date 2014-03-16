import os.path as path
from setuptools import setup


def get_readme(filename):
    with open(path.join(path.dirname(__file__), filename)) as readme:
        content = readme.read()
    return content

setup(name="mdx_linkify",
      version="0.4",
      author="Raitis (daGrevis) Stengrevics",
      author_email="dagrevis@gmail.com",
      description="Link recognition for Python Markdown",
      license="MIT",
      keywords="markdown links",
      url="https://github.com/daGrevis/mdx_linkify",
      packages=["mdx_linkify"],
      long_description=get_readme("README.md"),
      classifiers=[
          "Topic :: Text Processing :: Markup",
          "Topic :: Utilities",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3.3",
          "Programming Language :: Python :: Implementation :: PyPy",
          "Development Status :: 4 - Beta",
          "License :: OSI Approved :: MIT License",
      ],
      install_requires=["Markdown>=2.4", "bleach>=1.4"],
      test_suite="mdx_linkify.tests")
