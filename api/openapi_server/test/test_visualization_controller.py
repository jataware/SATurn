# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from openapi_server.models.ids import Ids  # noqa: E501
from openapi_server.test import BaseTestCase


class TestVisualizationController(BaseTestCase):
    """VisualizationController integration test stubs"""

    def test_visualization_post(self):
        """Test case for visualization_post

        Plot selected timeseries
        """
        body = Ids()
        response = self.client.open(
            '/visualization',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
