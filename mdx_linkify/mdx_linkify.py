import bleach

from html5lib.sanitizer import HTMLSanitizer

from markdown.postprocessors import Postprocessor
from markdown import Extension


class MyTokenizer(HTMLSanitizer):
    def sanitize_token(self, token):
        return token


class LinkifyPostprocessor(Postprocessor):
    def __init__(self, md, linkifycallbacks=[]):
        super(Postprocessor, self).__init__(md)
        self._callbacks = linkifycallbacks

    def run(self, text):
        text = bleach.linkify(text,
                              callbacks=self._callbacks,
                              tokenizer=MyTokenizer)
        return text


class LinkifyExtension(Extension):
    config = {'linkifycallbacks': [[], 'Callbacks to send to bleach.linkify']}

    def extendMarkdown(self, md, md_globals):
        md.postprocessors.add(
            "linkify",
            LinkifyPostprocessor(md, self.getConfig('linkifycallbacks')),
            "_begin")


def makeExtension(configs=None):
    return LinkifyExtension(configs=configs)
