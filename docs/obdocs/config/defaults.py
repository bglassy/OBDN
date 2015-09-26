from __future__ import unicode_literals

import six

from obdocs import utils
from obdocs.config import config_options

DEFAULT_SCHEMA = (

    # Reserved for internal use, stores the obdocs.yml config file.
    ('config_file_path', config_options.Type(six.string_types)),

    # The title to use for the documentation
    ('site_name', config_options.Type(six.string_types, required=True)),

    # Defines the structure of the navigation and which markdown files are
    # included in the build.
    ('pages', config_options.Pages()),

    # The full URL to where the documentation will be hosted
    ('site_url', config_options.URL()),

    # A description for the documentation project that will be added to the
    # HTML meta tags.
    ('site_description', config_options.Type(six.string_types)),
    # The name of the author to add to the HTML meta tags
    ('site_author', config_options.Type(six.string_types)),

    # The path to the favicon for a site
    ('site_favicon', config_options.Type(six.string_types)),

    # The theme for the documentation.
    ('theme', config_options.Theme(default='obdocs')),

    # The directory containing the documentation markdown.
    ('docs_dir', config_options.Dir(default='PATH_TO_GIT_CLONE/docs', exists=True)),

    # The directory where the site will be built to
    ('site_dir', config_options.SiteDir(default='PATH_TO_GIT_CLONE/site')),

    ('theme_dir', config_options.ThemeDir(exists=True)),

    # A copyright notice to add to the footer of documentation.
    ('copyright', config_options.Type(six.string_types)),

    # set of values for Google analytics containing the account IO and domain,
    # this should look like, ['UA-00000000-0', 'obdocs.org']
    ('google_analytics', config_options.Type(list, length=2)),

    # The address on which to serve the live reloading docs server.
    ('dev_addr', config_options.Type(
        six.string_types, default='127.0.0.1:8000')),

    # If `True`, use `<page_name>/index.hmtl` style files with hyperlinks to
    # the directory.If `False`, use `<page_name>.html style file with
    # hyperlinks to the file.
    # True generates nicer URLs, but False is useful if browsing the output on
    # a filesystem.
    ('use_directory_urls', config_options.Type(bool, default=True)),

    # Specify a link to the project source repo to be included
    # in the documentation pages.
    ('repo_url', config_options.RepoURL()),

    # A name to use for the link to the project source repo.
    # Default, If repo_url is unset then None, otherwise
    # "GitHub" or "Bitbucket" for known url or Hostname for unknown urls.
    ('repo_name', config_options.Type(six.string_types)),

    # Specify which css or javascript files from the docs directory should be
    # additionally included in the site. Default, List of all .css and .js
    # files in the docs dir.
    ('extra_css', config_options.Extras(file_match=utils.is_css_file)),
    ('extra_javascript', config_options.Extras(
        file_match=utils.is_javascript_file)),

    # Similar to the above, but each template (HTML or XML) will be build with
    # Jinja2 and the global context.
    ('extra_templates', config_options.Extras(
        file_match=utils.is_template_file)),

    ('include_nav', config_options.NumPages()),

    # PyMarkdown extension names.
    ('markdown_extensions', config_options.MarkdownExtensions(
        builtins=['meta', 'toc', 'tables', 'fenced_code'],
        configkey='mdx_configs', default=[])),

    # PyMarkdown Extension Configs. For internal use only.
    ('mdx_configs', config_options.Private()),

    # enabling strict mode causes obdocs to stop the build when a problem is
    # encountered rather than display an error.
    ('strict', config_options.Type(bool, default=False)),
)
