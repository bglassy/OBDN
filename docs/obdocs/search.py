from __future__ import unicode_literals

import json
import six


class SearchIndex(object):
   

    def __init__(self):
        self._entries = []

    def _find_toc_by_id(self, toc, id_):
        
        for toc_item in toc:
            if toc_item.url[1:] == id_:
                return toc_item
            for toc_sub_item in toc_item.children:
                if toc_sub_item.url[1:] == id_:
                    return toc_sub_item

    def _add_entry(self, title, text, loc):
        
        self._entries.append({
            'title': title,
            'text': six.text_type(text.strip().encode('utf-8'), encoding='utf-8'),
            'location': loc
        })

    def add_entry_from_context(self, page, content, toc):
       

        # Create the content parser and feed in the HTML for the
        # full page. This handles all the parsing and prepares
        # us to iterate through it.
        parser = ContentParser()
        parser.feed(content)

        # Get the absolute URL for the page, this is then
        # prepended to the urls of the sections
        abs_url = page.abs_url

        # Create an entry for the full page.
        self._add_entry(
            title=page.title,
            text=self.strip_tags(content).rstrip('\n'),
            loc=abs_url
        )

        for section in parser.data:
            self.create_entry_for_section(section, toc, abs_url)

    def create_entry_for_section(self, section, toc, abs_url):
       

        toc_item = self._find_toc_by_id(toc, section.id)

        if toc_item is not None:
            self._add_entry(
                title=toc_item.title,
                text=u" ".join(section.text),
                loc=abs_url + toc_item.url
            )

    def generate_search_index(self):
        """python to json conversion"""
        page_dicts = {
            'docs': self._entries,
        }
        return json.dumps(page_dicts, sort_keys=True, indent=4)

    def strip_tags(self, html):
        """strip html tags from data"""
        s = HTMLStripper()
        s.feed(html)
        return s.get_data()


class HTMLStripper(six.moves.html_parser.HTMLParser):
   

    def __init__(self, *args, **kwargs):
        # HTMLParser is a old-style class in Python 2, so
        # super() wont work here.
        six.moves.html_parser.HTMLParser.__init__(self, *args, **kwargs)

        self.data = []

    def handle_data(self, d):
       
        self.data.append(d)

    def get_data(self):
        return '\n'.join(self.data)


class ContentSection(object):
  

    def __init__(self, text=None, id_=None, title=None):
        self.text = text or []
        self.id = id_
        self.title = title

    def __eq__(self, other):
        return all([
            self.text == other.text,
            self.id == other.id,
            self.title == other.title
        ])


class ContentParser(six.moves.html_parser.HTMLParser):
  

    def __init__(self, *args, **kwargs):

        # HTMLParser is a old-style class in Python 2, so
        # super() wont work here.
        six.moves.html_parser.HTMLParser.__init__(self, *args, **kwargs)

        self.data = []
        self.section = None
        self.is_header_tag = False

    def handle_starttag(self, tag, attrs):
        """Called at the start of every HTML tag."""

        # We only care about the opening tag for H1 and H2.
        if tag not in ("h1", "h2"):
            return

        # We are dealing with a new header, create a new section
        # for it and assign the ID if it has one.
        self.is_header_tag = True
        self.section = ContentSection()
        self.data.append(self.section)

        for attr in attrs:
            if attr[0] == "id":
                self.section.id = attr[1]

    def handle_endtag(self, tag):
        """Called at the end of every HTML tag."""

        # We only care about the opening tag for H1 and H2.
        if tag not in ("h1", "h2"):
            return

        self.is_header_tag = False

    def handle_data(self, data):
        """
        Called for the text contents of each tag.
        """

        if self.section is None:
            # This means we have some content at the start of the
            # HTML before we reach a H1 or H2. We don't actually
            # care about that content as it will be added to the
            # overall page entry in the search. So just skip it.
            return

        # If this is a header, then the data is the title.
        # Otherwise it is content of something under that header
        # section.
        if self.is_header_tag:
            self.section.title = data
        else:
            self.section.text.append(data.rstrip('\n'))
