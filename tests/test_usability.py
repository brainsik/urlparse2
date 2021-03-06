# encoding: utf-8
import urlparse2
from unittest import TestCase


class TestUsability(TestCase):

    def test_scheme_is_mutable(self):
        url = 'http://www.cwi.nl:80/%7Eguido/Python.html'
        expect = 'https://www.cwi.nl:80/%7Eguido/Python.html'

        result = urlparse2.urlparse(url)
        result.scheme = 'https'

        joined = urlparse2.urlunparse(result)
        self.assertEquals(joined, expect)

    def test_flexible_schema(self):
        url = 'zzyzx://chub'

        result = urlparse2.urlparse(url)
        joined = urlparse2.urlunparse(result)
        self.assertEquals(joined, url)

    def test_protocolless_urlprefix(self):
        prefix = 'domain.com'
        path = 'path/to/file'

        self.assertRaises(ValueError, urlparse2.urljoin, prefix, path)

    def test_protocolfull_urlprefix(self):
        prefix = 'http://domain.com'
        path = 'path/to/file'
        expect = 'http://domain.com/path/to/file'

        result = urlparse2.urljoin(prefix, path)
        self.assertEquals(result, expect)
