# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from openapi_server.test import BaseTestCase


class TestDownloadController(BaseTestCase):
    """DownloadController integration test stubs"""

    def test_download_variables_data_location_dataset_id_post(self):
        """Test case for download_variables_data_location_dataset_id_post

        Download ISI variables
        """
        error_unknown = None
        response = self.client.open(
            '/download_variables/{dataset_id}'.format(dataset_id='None'),
            method='POST',
            data=json.dumps(error_unknown),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
