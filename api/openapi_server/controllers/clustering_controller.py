import connexion
import six

from openapi_server.models.ids import Ids  # noqa: E501
from openapi_server import util


def clustering_post(clusters, body):  # noqa: E501
    """Cluster given data into selected number of clusters

    K-means   # noqa: E501

    :param clusters: Number of clusters
    :type clusters: str
    :param body: _Must_ provide &#x60;dataset_ID&#x60; and &#x60;variable_ID&#x60;.  &#x60;admin&#x60; and &#x60;time&#x60; are optional.&lt;br&gt;

    :type body: 

    :rtype: file
    """
    return 'do some magic!'
