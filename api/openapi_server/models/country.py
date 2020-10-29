# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Country(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, country: List[str]=None):  # noqa: E501
        """Country - a model defined in OpenAPI

        :param country: The country of this Country.  # noqa: E501
        :type country: List[str]
        """
        self.openapi_types = {
            'country': List[str]
        }

        self.attribute_map = {
            'country': 'country'
        }

        self._country = country

    @classmethod
    def from_dict(cls, dikt) -> 'Country':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The country of this Country.  # noqa: E501
        :rtype: Country
        """
        return util.deserialize_model(dikt, cls)

    @property
    def country(self) -> List[str]:
        """Gets the country of this Country.


        :return: The country of this Country.
        :rtype: List[str]
        """
        return self._country

    @country.setter
    def country(self, country: List[str]):
        """Sets the country of this Country.


        :param country: The country of this Country.
        :type country: List[str]
        """

        self._country = country