from markdown.inlinepatterns import Pattern
from markdown.util import etree, AtomicString
from markdown import Extension


URL_RE = r"\b(([\w-]+://?|www[.])[^\s()<>]+(?:\([\w\d]+\)|([^[:punct:]\s]|/)))"
# http://daringfireball.net/2009/11/liberal_regex_for_matching_urls


class LinkifyPattern(Pattern):
    def handleMatch(self, match):
        match = match.group(0)
        el = etree.Element("a")
        el.set("href", match)
        el.text = AtomicString(match)
        return el


class LinkifyExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        md.inlinePatterns["autolink"] = LinkifyPattern(URL_RE, md)


def makeExtension(configs=None):
    return LinkifyExtension(configs=configs)
