from itertools import repeat



class Tablette(object):

    def __init__(self, columns, data, mapping=None):
        self.columns = columns
        self.data = data
        self.mapping = mapping

        self.pos_to_name = {}
        for i, column in enumerate(columns):
            column_name = self.get_name(column)
            if column_name:
                self.pos_to_name[i] = column_name

        self.groups = []
        intervals = self.pos_to_name.keys() + [len(self.columns)]
        self.groups = zip(intervals, intervals[1:])
        self.last_dicts = list(repeat(None, len(self.pos_to_name.keys())))


    def get_name(self, column):
        name = None
        if self.mapping and column in self.mapping:
            name = self.mapping[column]
        elif column.endswith('id'):
            name = column.replace('id', 'list')
        return name


    def process_group(self, row, group, parent):
        begin, end = self.groups[group]
        current = self.last_dicts[group]

        try:
            child_name = self.pos_to_name[end]
        except KeyError:
            child_name = None

        if not current:
            current = self.last_dicts[group] = dict(zip(
                      self.columns[begin:end], row[begin:end]))
            if child_name:
                current[child_name] = []
            parent.append(current)

        if group + 1 < len(self.groups):
            self.process_group(row, group + 1, current[child_name])

        return current


    def process(self):
        acc = []

        for row in self.data:
            reset = False
            for i, (begin, _) in enumerate(self.groups):
                key = self.columns[begin]
                last_dict = self.last_dicts[i]
                if reset or (last_dict and row[begin] != last_dict[key]):
                    reset = True
                    self.last_dicts[i] = None
            self.process_group(row, 0, acc)

        root_elem = self.pos_to_name[self.groups[0][0]]
        return {root_elem: acc}


def tablette(columns, data, mapping=None):
    return Tablette(columns, data, mapping).process()



if __name__ == '__main__':
    columns = ['id', 'username', 'url_id', 'url', 'tag_id', 'tag']
    data = [
            [ 1, 'albi', 1, 'http://python.org/', 1, 'programming language' ],
            [ 1, 'albi', 1, 'http://python.org/', 2, 'open source' ],
            [ 1, 'albi', 2, 'http://php.net/', 2, 'open source' ],
            [ 1, 'albi', 2, 'http://php.net/', 3, 'web' ],
            [ 2, 'karl', 3, 'http://reddit.com/', 4, 'lol' ],
            [ 2, 'karl', 3, 'http://reddit.com/', 5, 'wtf' ]
        ]


    from pprint import pprint
    t = tablette(columns, data)
    pprint(t)
