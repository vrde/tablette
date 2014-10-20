from tablette import tablette
import unittest
import json



def dumps(d):
    return json.dumps(d, sort_keys=True)


class TestSimpleTable(unittest.TestCase):


    def test_simple_default_grouping(self):
        columns = ['id', 'username', 'email_id', 'email']
        data = [
                [ 1, 'albi', 1, 'albi@example.org'],
                [ 2, 'karl', 2, 'karl@example.org']]

        self.assertEqual({
            'list': [{
                'id': 1,
                'username': 'albi',
                'email_list': [{
                    'email_id': 1,
                    'email': 'albi@example.org'
                    }]
                }, {
                    'id': 2,
                    'username': 'karl',
                    'email_list': [{
                        'email_id': 2,
                        'email': 'karl@example.org'
                        }]
                    }]
                }, tablette(columns, data))


    def test_complex_defaultt_grouping(self):
        columns = ['id', 'username', 'url_id', 'url', 'tag_id', 'tag']
        data = [
                [ 1, 'albi', 1, 'http://python.org/', 1, 'programming language' ],
                [ 1, 'albi', 1, 'http://python.org/', 2, 'open source' ],
                [ 1, 'albi', 2, 'http://php.net/', 2, 'open source' ],
                [ 1, 'albi', 2, 'http://php.net/', 3, 'web' ],
                [ 2, 'karl', 3, 'http://reddit.com/', 4, 'lol' ],
                [ 2, 'karl', 3, 'http://reddit.com/', 5, 'wtf' ]]

        self.assertEqual({
            'list': [{
                'id': 1,
                'username': 'albi',
                'url_list': [{
                    'url_id': 1,
                    'url': 'http://python.org/',
                    'tag_list': [
                        { 'tag_id': 1, 'tag': 'programming language' },
                        { 'tag_id': 2, 'tag': 'open source' }
                        ],
                    }, {
                        'url_id': 2,
                        'url': 'http://php.net/',
                        'tag_list': [
                            { 'tag_id': 2, 'tag': 'open source' },
                            { 'tag_id': 3, 'tag': 'web' }
                            ]
                        }]
                    }, {
                        'id': 2,
                        'username': 'karl',
                        'url_list': [{
                            'url_id': 3,
                            'url': 'http://reddit.com/',
                            'tag_list': [
                                { 'tag_id': 4, 'tag': 'lol' },
                                { 'tag_id': 5, 'tag': 'wtf' }
                                ]}
                            ]
                        }
                    ]
            }, tablette(columns, data))

    def test_simple_named_grouping(self):
        groups = {'id': 'users', 'email_uid': 'email_list'}
        columns = ['id', 'username', 'email_uid', 'email']
        data = [
                [ 1, 'albi', 1, 'albi@example.org'],
                [ 2, 'karl', 2, 'karl@example.org']]

        self.assertEqual({
            'users': [{
                'id': 1,
                'username': 'albi',
                'email_list': [{
                    'email_uid': 1,
                    'email': 'albi@example.org'
                    }]
                }, {
                    'id': 2,
                    'username': 'karl',
                    'email_list': [{
                        'email_uid': 2,
                        'email': 'karl@example.org'
                        }]
                    }]
                }, tablette(columns, data, groups))

