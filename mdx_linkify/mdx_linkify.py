from bleach.linkifier import Linker

from markdown.postprocessors import Postprocessor
from markdown.extensions import Extension


class LinkifyExtension(Extension):

    def __init__(self, **kwargs):
        self.config = {
            'linker_options': [{}, 'Options for bleach.linkifier.Linker'],
        }
        super(LinkifyExtension, self).__init__(**kwargs)

    def extendMarkdown(self, md):
        md.postprocessors.register(
            LinkifyPostprocessor(
                md,
                self.getConfig('linker_options'),
            ),
            "linkify",
            50,
        )


class LinkifyPostprocessor(Postprocessor):

    def __init__(self, md, linker_options):
        super(LinkifyPostprocessor, self).__init__(md)
        linker_options.setdefault("skip_tags", ["code"])
        self._linker = Linker(**linker_options)

    def run(self, text):
        return self._linker.linkify(text)


def makeExtension(*args, **kwargs):
    return LinkifyExtension(*args, **kwargs)
