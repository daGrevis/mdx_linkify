# -*- coding: utf-8 -*-
import re

from urlparse import urlparse
from tldextract import extract as tld_extract

from markdown.preprocessors import Preprocessor
from markdown import Extension


class LinkifyPreprocessor(Preprocessor):
    def run(self, lines):
        new_lines = []
        for line in lines:
            new_words = []
            for word in line.split():
                # Do nothing if the word is empty.
                if not word:
                    new_words.append(word)
                    continue
                # Checks that it's not in Markdown format.
                if re.match(r"!?\(.+\)\[.+\]", word):
                    new_words.append(word)
                    continue
                # Checks that it has correct scheme.
                parsed_url = urlparse(word)
                if parsed_url.scheme not in ["http", "https"]:
                    new_words.append(word)
                    continue
                # Checks that it has a netloc.
                if not parsed_url.netloc:
                    new_words.append(word)
                    continue
                # Checks that it has valid TLD.
                if not tld_extract(word).tld:
                    new_words.append(word)
                    continue
                link = "[{0}]({1})".format(word, word)
                new_words.append(link)
            new_lines.append(" ".join(new_words))
        return new_lines


class LinkifyExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        md.preprocessors.add("linkify", LinkifyPreprocessor(md), "_begin")


def makeExtension(configs=None):
    return LinkifyExtension(configs=configs)
