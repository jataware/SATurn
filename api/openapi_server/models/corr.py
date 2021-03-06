# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Corr(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, correlators: List[str]=None):  # noqa: E501
        """Corr - a model defined in OpenAPI

        :param correlators: The correlators of this Corr.  # noqa: E501
        :type correlators: List[str]
        """
        self.openapi_types = {
            'correlators': List[str]
        }

        self.attribute_map = {
            'correlators': 'correlators'
        }

        self._correlators = correlators

    @classmethod
    def from_dict(cls, dikt) -> 'Corr':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The corr of this Corr.  # noqa: E501
        :rtype: Corr
        """
        return util.deserialize_model(dikt, cls)

    @property
    def correlators(self) -> List[str]:
        """Gets the correlators of this Corr.


        :return: The correlators of this Corr.
        :rtype: List[str]
        """
        return self._correlators

    @correlators.setter
    def correlators(self, correlators: List[str]):
        """Sets the correlators of this Corr.


        :param correlators: The correlators of this Corr.
        :type correlators: List[str]
        """
        if correlators is None:
            raise ValueError("Invalid value for `correlators`, must not be `None`")  # noqa: E501

        self._correlators = correlators
