import sys


is_python3 = sys.version_info >= (3, 0)

if is_python3:
    from mdx_linkify.mdx_linkify import makeExtension
else:
    from mdx_linkify import makeExtension


assert makeExtension  # Silences pep8.
