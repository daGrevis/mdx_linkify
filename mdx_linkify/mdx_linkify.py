import bleach

from html5lib.sanitizer import HTMLSanitizer

from markdown.postprocessors import Postprocessor
from markdown import Extension


class MyTokenizer(HTMLSanitizer):
    def sanitize_token(self, token):
        return token


class LinkifyPostprocessor(Postprocessor):
    def __init__(self, md, linkify_callbacks=[]):
        super(Postprocessor, self).__init__(md)
        self._callbacks = linkify_callbacks

    def run(self, text):
        text = bleach.linkify(text,
                              callbacks=self._callbacks,
                              tokenizer=MyTokenizer)
        return text


class LinkifyExtension(Extension):
    config = {'linkify_callbacks': [[], 'Callbacks to send to bleach.linkify']}

    def extendMarkdown(self, md, md_globals):
        md.postprocessors.add(
            "linkify",
            LinkifyPostprocessor(md, self.getConfig('linkify_callbacks')),
            "_begin")


def makeExtension(*args, **kwargs):
    return LinkifyExtension(*args, **kwargs)
