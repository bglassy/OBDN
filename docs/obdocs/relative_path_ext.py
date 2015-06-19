import logging

from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor
import six

from obdocs import utils
from obdocs.exceptions import MarkdownNotFound

log = logging.getLogger(__name__)


def _iter(node):
    # TODO: Remove when dropping Python 2.6. Replace this
    # function call with note.iter()
    return [node] + node.findall('.//*')


def path_to_url(url, nav, strict):

    scheme, netloc, path, params, query, fragment = (
        six.moves.urllib.parse.urlparse(url))

    if scheme or netloc or not path:
        # Ignore URLs unless they are a relative link to a markdown file.
        return url

    if nav and not utils.is_markdown_file(path):
        path = utils.create_relative_media_url(nav, path)
    elif nav:
        # If the site navigation has been provided, then validate
        # the internal hyperlink, making sure the target actually exists.
        target_file = nav.file_context.make_absolute(path)
        if target_file not in nav.source_files:
            source_file = nav.file_context.current_file
            msg = (
                'The page "%s" contained a hyperlink to "%s" which '
                'is not listed in the "pages" configuration.'
            ) % (source_file, target_file)

            # In strict mode raise an error at this point.
            if strict:
                raise MarkdownNotFound(msg)
            # Otherwise, when strict mode isn't enabled, log a warning
            # to the user and leave the URL as it is.
            log.warning(msg)
            return url
        path = utils.get_url_path(target_file, nav.use_directory_urls)
        path = nav.url_context.make_relative(path)
    else:
        path = utils.get_url_path(path).lstrip('/')

    # Convert the .md hyperlink to a relative hyperlink to the HTML page.
    fragments = (scheme, netloc, path, params, query, fragment)
    url = six.moves.urllib.parse.urlunparse(fragments)
    return url


class RelativePathTreeprocessor(Treeprocessor):

    def __init__(self, site_navigation, strict):
        self.site_navigation = site_navigation
        self.strict = strict

    def run(self, root):
       

        for element in _iter(root):

            if element.tag == 'a':
                key = 'href'
            elif element.tag == 'img':
                key = 'src'
            else:
                continue

            url = element.get(key)
            new_url = path_to_url(url, self.site_navigation, self.strict)
            element.set(key, new_url)

        return root


class RelativePathExtension(Extension):
  

    def __init__(self, site_navigation, strict):
        self.site_navigation = site_navigation
        self.strict = strict

    def extendMarkdown(self, md, md_globals):
        relpath = RelativePathTreeprocessor(self.site_navigation, self.strict)
        md.treeprocessors.add("relpath", relpath, "_end")
