import bleach

from markdown.postprocessors import Postprocessor
from markdown import Extension


class LinkifyPostprocessor(Postprocessor):
    def __init__(self, md, linkify_callbacks=[], linkify_parse_email=False):
        super(Postprocessor, self).__init__(md)
        self._callbacks = linkify_callbacks
        self._parse_email = linkify_parse_email

    def run(self, text):
        text = bleach.linkify(text,
                              parse_email=self._parse_email,
                              callbacks=self._callbacks,
                              skip_tags=['code'])
        return text


class LinkifyExtension(Extension):
    
    def __init__(self, **kwargs):
        self.config = {
            'linkify_callbacks': [[], 'Callbacks to send to bleach.linkify'],
            'linkify_parse_email': [False, 'Parse email addresses'],
        }
        super(LinkifyExtension, self).__init__(**kwargs)

    def extendMarkdown(self, md):
        md.postprocessors.register(
            LinkifyPostprocessor(md, self.getConfig('linkify_callbacks'), self.getConfig('linkify_parse_email')),
            "linkify",
            50)


def makeExtension(*args, **kwargs):
    return LinkifyExtension(*args, **kwargs)
