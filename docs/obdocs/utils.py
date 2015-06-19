# coding: utf-8


import os
import shutil

import markdown
import six

from obdocs import toc


def reduce_list(data_set):
   
    seen = set()
    return [item for item in data_set if item not in seen and not seen.add(item)]


def copy_file(source_path, output_path):
   
    output_dir = os.path.dirname(output_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    shutil.copy(source_path, output_path)


def write_file(content, output_path):
   
    output_dir = os.path.dirname(output_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    open(output_path, 'wb').write(content)


def clean_directory(directory):
   
    if not os.path.exists(directory):
        return

    for entry in os.listdir(directory):

        # Don't remove hidden files from the directory. We never copy files
        # that are hidden, so we shouldn't delete them either.
        if entry.startswith('.'):
            continue

        path = os.path.join(directory, entry)
        if os.path.isdir(path):
            shutil.rmtree(path, True)
        else:
            os.unlink(path)


def copy_media_files(from_dir, to_dir):
  
    for (source_dir, dirnames, filenames) in os.walk(from_dir):
        relative_path = os.path.relpath(source_dir, from_dir)
        output_dir = os.path.normpath(os.path.join(to_dir, relative_path))

        # Filter filenames starting with a '.'
        filenames = [f for f in filenames if not f.startswith('.')]

        # Filter the dirnames that start with a '.' and update the list in
        # place to prevent us walking these.
        dirnames[:] = [d for d in dirnames if not d.startswith('.')]

        for filename in filenames:
            if not is_markdown_file(filename) and not is_html_file(filename):
                source_path = os.path.join(source_dir, filename)
                output_path = os.path.join(output_dir, filename)
                copy_file(source_path, output_path)


def get_html_path(path):

    path = os.path.splitext(path)[0]
    if os.path.basename(path) == 'index':
        return path + '.html'
    return "/".join((path, 'index.html'))


def get_url_path(path, use_directory_urls=True):
   
    path = get_html_path(path)
    url = '/' + path.replace(os.path.sep, '/')
    if use_directory_urls:
        return url[:-len('index.html')]
    return url


def is_homepage(path):
    return os.path.splitext(path)[0] == 'index'


def is_markdown_file(path):
   
    ext = os.path.splitext(path)[1].lower()
    return ext in [
        '.markdown',
        '.mdown',
        '.mkdn',
        '.mkd',
        '.md',
    ]


def is_css_file(path):
   
    ext = os.path.splitext(path)[1].lower()
    return ext in [
        '.css',
    ]


def is_javascript_file(path):
    
    ext = os.path.splitext(path)[1].lower()
    return ext in [
        '.js',
        '.javascript'
    ]


def is_html_file(path):
  
    ext = os.path.splitext(path)[1].lower()
    return ext in [
        '.html',
        '.htm',
    ]


def is_template_file(path):
  
    ext = os.path.splitext(path)[1].lower()
    return ext in [
        '.html',
        '.htm',
        '.xml',
    ]


def create_media_urls(nav, path_list):
   
    final_urls = []

    for path in path_list:
        # Allow links to fully qualified URL's
        parsed = six.moves.urllib.parse.urlparse(path)
        if parsed.netloc:
            final_urls.append(path)
            continue
        # We must be looking at a local path.
        url = path_to_url(path)
        relative_url = '%s/%s' % (nav.url_context.make_relative('/'), url)
        final_urls.append(relative_url)

    return final_urls


def create_relative_media_url(nav, url):
   

    # Allow links to fully qualified URL's
    parsed = six.moves.urllib.parse.urlparse(url)
    if parsed.netloc:
        return url

    # If the URL we are looking at starts with a /, then it should be
    # considered as absolute and will be 'relative' to the root.
    if url.startswith('/'):
        base = '/'
        url = url[1:]
    else:
        base = nav.url_context.base_path

    relative_base = nav.url_context.make_relative(base)
    if relative_base == "." and url.startswith("./"):
        relative_url = url
    else:
        relative_url = '%s/%s' % (relative_base, url)

    # TODO: Fix this, this is a hack. Relative urls are not being calculated
    # correctly for images in the same directory as the markdown. I think this
    # is due to us moving it into a directory with index.html, but I'm not sure
    if (nav.file_context.current_file.endswith("/index.md") is False and
            nav.url_context.base_path is not '/' and
            relative_url.startswith("./")):
        relative_url = ".%s" % relative_url

    return relative_url


def path_to_url(path):
    """Convert a system path to a URL."""

    if os.path.sep == '/':
        return path

    return six.moves.urllib.request.pathname2url(path)


def convert_markdown(markdown_source, extensions=None, extension_configs=None):
   
    md = markdown.Markdown(
        extensions=extensions or [],
        extension_configs=extension_configs or {}
    )
    html_content = md.convert(markdown_source)

    # On completely blank markdown files, no Meta or tox properties are added
    # to the generated document.
    meta = getattr(md, 'Meta', {})
    toc_html = getattr(md, 'toc', '')

    # Post process the generated table of contents into a data structure
    table_of_contents = toc.TableOfContents(toc_html)

    return (html_content, table_of_contents, meta)


def get_theme_names():
 

    return os.listdir(os.path.join(os.path.dirname(__file__), 'themes'))


def filename_to_title(filename):

    title = os.path.splitext(filename)[0]
    title = title.replace('-', ' ').replace('_', ' ')
    # Capitalize if the filename was all lowercase, otherwise leave it as-is.
    if title.lower() == title:
        title = title.capitalize()

    return title


def find_or_create_node(branch, key):
  

    for node in branch:
        if not isinstance(node, dict):
            continue

        if key in node:
            return node[key]

    new_branch = []
    node = {key: new_branch}
    branch.append(node)
    return new_branch


def nest_paths(paths):
   
    nested = []

    for path in paths:

        if os.path.sep not in path:
            nested.append(path)
            continue

        directory, _ = os.path.split(path)
        parts = directory.split(os.path.sep)

        branch = nested
        for part in parts:
            part = filename_to_title(part)
            branch = find_or_create_node(branch, part)

        branch.append(path)

    return nested
