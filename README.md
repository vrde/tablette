Introduction
============

**Tablette** is a micro Python module to transform tabular data to nested
lists of dicts.


Why
===

The purpose of the module is to make it easy to create JSON data starting
from a database cursor. Yes. A database cursor, do you remember that? :)


How it works
============

As an example, consider this dataset:

```python
columns = ['id', 'username', 'url_id', 'url', 'tag_id', 'tag']
data = [
        [ 1, 'albi', 1, 'http://python.org/', 1, 'programming language' ],
        [ 1, 'albi', 1, 'http://python.org/', 2, 'open source' ],
        [ 1, 'albi', 2, 'http://php.net/', 2, 'open source' ],
        [ 1, 'albi', 2, 'http://php.net/', 3, 'web' ],
        [ 2, 'karl', 3, 'http://reddit.com/', 4, 'lol' ],
        [ 2, 'karl', 3, 'http://reddit.com/', 5, 'wtf' ]
    ]
```

If you import tablette and feed it with the columns and data:

```python
t = tablette(columns, data)
```

Then you'll get this nice data structure:

```python
{
    'list': [{
        'id': 1,
        'username': 'albi'
        'url_list': [{
            'url': 'http://python.org/',
            'url_id': 1
            'tag_list': [{
                'tag': 'programming language',
                'tag_id': 1
            }, {
                'tag': 'open source',
                'tag_id': 2
            }],
        }, {
            'url': 'http://php.net/',
            'url_id': 2
            'tag_list': [{
                'tag': 'open source',
                'tag_id': 2
            }, {
                'tag': 'web',
                'tag_id': 3
            }],
        }],
    }, {
        'id': 2,
        'username': 'karl'
        'url_list': [{
            'url': 'http://reddit.com/',
            'url_id': 3
            'tag_list': [{
                'tag': 'lol',
                'tag_id': 4
            }, {
                'tag': 'wtf',
                'tag_id': 5
            }],
        }],
    }
]}
```

Pretty cool, no?


How grouping works
------------------

By default, **tablette** groups using the fields ending by `id`. This is the
normal behaviour, and it works for simple cases. **tablette** then substitutes
the `id` part of the name with `list`.
But it's more likely that you need something more advanced. That's why you can
pass a third parameter named `mapping` to the parsing function.
In the previous example, a better and more semantic mapping would have been:

```python
mapping = { 'id': 'users', 'url_id': 'urls', 'tag_id': 'tags' }
```

Leading to the following dict (please note how the root element is now
named `users`, `url_list` is now `urls`, and `tag_list` is now `tags`)

```python
{
    'users': [{
        'id': 1,
        'username': 'albi'
        'urls': [{
            'url': 'http://python.org/',
            'url_id': 1
            'tags': [{
                'tag': 'programming language',
                'tag_id': 1
            [ ... ]
```
