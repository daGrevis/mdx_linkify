import bleach

from markdown.postprocessors import Postprocessor
from markdown import Extension


class LinkifyPostprocessor(Postprocessor):
    def __init__(self, md, linkify_callbacks=[]):
        super(Postprocessor, self).__init__(md)
        self._callbacks = linkify_callbacks

    def run(self, text):
        text = bleach.linkify(text,
                              callbacks=self._callbacks)
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
