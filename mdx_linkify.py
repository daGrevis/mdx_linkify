# -*- coding: utf-8 -*-
import string

from urlparse import urlparse

from markdown.preprocessors import Preprocessor
from markdown import Extension


class LinkifyPreprocessor(Preprocessor):
    def run(self, lines):
        new_lines = []
        for line in lines:
            new_words = []
            for word in line.split(" "):
                if word == "":
                    continue
                if word[0] not in string.ascii_letters:
                    new_words.append(word)
                    continue
                parsed_url = urlparse(word)
                if parsed_url.scheme not in ["http", "https"]:
                    new_words.append(word)
                    continue
                link = "[{}]({})".format(word, word)
                new_words.append(link)
            new_lines.append(" ".join(new_words))
        return new_lines


class LinkifyExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        md.preprocessors.add("linkify", LinkifyPreprocessor(md), "_begin")


def makeExtension(configs=None):
    return LinkifyExtension(configs=configs)
