# -*- coding: utf-8 -*-
import os
from textwrap import fill


def wrap(text):
    filled = fill(str(text[1]), width=120, initial_indent='# ' + text[0] + ': ', subsequent_indent='# ')
    return '\n' + filled + '\n'


class ToPython(object):

    def process_item(self, item, spider):
        if spider.path:
            path = os.path.expanduser(spider.path)
            if os.path.exists(path):
                new_path = path + '/%i-%s.py' % (item.pop('number'), item.pop('title'))
                with open(new_path, 'w+') as f:
                    f.write('# -*- coding: utf-8 -*-\n')
                    for formatted in [wrap(x) for x in item.items()]:
                        f.write(formatted)
            print("\033[31mThis file doesn't exists: %s\033[m" % spider.path)
        return item
