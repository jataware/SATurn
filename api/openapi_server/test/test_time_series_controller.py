# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from openapi_server.models.ids import Ids  # noqa: E501
from openapi_server.test import BaseTestCase


class TestTimeSeriesController(BaseTestCase):
    """TimeSeriesController integration test stubs"""

    def test_timeseries_post(self):
        """Test case for timeseries_post

        Search over Datamarts
        """
        body = Ids()
        response = self.client.open(
            '/timeseries',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
