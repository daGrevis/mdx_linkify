from bleach.linkifier import URL_RE, Linker

from markdown.postprocessors import Postprocessor
from markdown import Extension


class LinkifyPostprocessor(Postprocessor):
    def __init__(
        self,
        md,
        linkify_callbacks=[],
        linkify_parse_email=False,
        linkify_url_re=URL_RE,
    ):
        super(Postprocessor, self).__init__(md)
        self._linker = Linker(
            parse_email=linkify_parse_email,
            callbacks=linkify_callbacks,
            url_re=linkify_url_re,
            skip_tags=['code'],
        )

    def run(self, text):
        return self._linker.linkify(text)


class LinkifyExtension(Extension):
    
    def __init__(self, **kwargs):
        self.config = {
            'linkify_callbacks': [[], 'Callbacks to send to bleach.linkify'],
            'linkify_parse_email': [False, 'Parse email addresses'],
            'linkify_url_re': [URL_RE, 'URL matching regex'],
        }
        super(LinkifyExtension, self).__init__(**kwargs)

    def extendMarkdown(self, md):
        md.postprocessors.register(
            LinkifyPostprocessor(
                md,
                self.getConfig('linkify_callbacks'),
                self.getConfig('linkify_parse_email'),
                self.getConfig('linkify_url_re'),
            ),
            "linkify",
            50,
        )


def makeExtension(*args, **kwargs):
    return LinkifyExtension(*args, **kwargs)
