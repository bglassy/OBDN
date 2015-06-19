# coding: utf-8


import six


class TableOfContents(object):
    
    def __init__(self, html):
        self.items = _parse_html_table_of_contents(html)

    def __iter__(self):
        return iter(self.items)

    def __str__(self):
        return ''.join([str(item) for item in self])


class AnchorLink(object):
   
    def __init__(self, title, url):
        self.title, self.url = title, url
        self.children = []

    def __str__(self):
        return self.indent_print()

    def indent_print(self, depth=0):
        indent = '    ' * depth
        ret = '%s%s - %s\n' % (indent, self.title, self.url)
        for item in self.children:
            ret += item.indent_print(depth + 1)
        return ret


class TOCParser(six.moves.html_parser.HTMLParser):

    def __init__(self):
        six.moves.html_parser.HTMLParser.__init__(self)
        self.links = []

        self.in_anchor = False
        self.attrs = None
        self.title = ''

    def handle_starttag(self, tag, attrs):

        if not self.in_anchor:
            if tag == 'a':
                self.in_anchor = True
                self.attrs = dict(attrs)

    def handle_endtag(self, tag):
        if tag == 'a':
            self.in_anchor = False

    def handle_data(self, data):

        if self.in_anchor:
            self.title += data


def _parse_html_table_of_contents(html):
   
    lines = html.splitlines()[2:-2]
    parents = []
    ret = []
    for line in lines:
        parser = TOCParser()
        parser.feed(line)
        if parser.title:
            try:
                href = parser.attrs['href']
            except KeyError:
                continue
            title = parser.title
            nav = AnchorLink(title, href)
            # Add the item to its parent if required.  If it is a topmost
            # item then instead append it to our return value.
            if parents:
                parents[-1].children.append(nav)
            else:
                ret.append(nav)
            # If this item has children, store it as the current parent
            if line.endswith('<ul>'):
                parents.append(nav)
        elif line.startswith('</ul>'):
            if parents:
                parents.pop()

    # For the table of contents, always mark the first element as active
    if ret:
        ret[0].active = True

    return ret
