import bleach

from markdown.postprocessors import Postprocessor
from markdown import Extension


class LinkifyPostprocessor(Postprocessor):
    def run(self, text):
        text = bleach.linkify(text, callbacks=[])
        return text


class LinkifyExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        md.postprocessors.add("linkify", LinkifyPostprocessor(md), "_begin")


def makeExtension(configs=None):
    return LinkifyExtension(configs=configs)
