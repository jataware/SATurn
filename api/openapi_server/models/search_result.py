# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class SearchResult(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, dataset_id: str=None, variable_id: str=None, name: str=None, description: str=None, score: float=None):  # noqa: E501
        """SearchResult - a model defined in OpenAPI

        :param dataset_id: The dataset_id of this SearchResult.  # noqa: E501
        :type dataset_id: str
        :param variable_id: The variable_id of this SearchResult.  # noqa: E501
        :type variable_id: str
        :param name: The name of this SearchResult.  # noqa: E501
        :type name: str
        :param description: The description of this SearchResult.  # noqa: E501
        :type description: str
        :param score: The score of this SearchResult.  # noqa: E501
        :type score: float
        """
        self.openapi_types = {
            'dataset_id': str,
            'variable_id': str,
            'name': str,
            'description': str,
            'score': float
        }

        self.attribute_map = {
            'dataset_id': 'dataset_id',
            'variable_id': 'variable_id',
            'name': 'name',
            'description': 'description',
            'score': 'score'
        }

        self._dataset_id = dataset_id
        self._variable_id = variable_id
        self._name = name
        self._description = description
        self._score = score

    @classmethod
    def from_dict(cls, dikt) -> 'SearchResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The search_result of this SearchResult.  # noqa: E501
        :rtype: SearchResult
        """
        return util.deserialize_model(dikt, cls)

    @property
    def dataset_id(self) -> str:
        """Gets the dataset_id of this SearchResult.

        The id of the dataset or variable within the data location  # noqa: E501

        :return: The dataset_id of this SearchResult.
        :rtype: str
        """
        return self._dataset_id

    @dataset_id.setter
    def dataset_id(self, dataset_id: str):
        """Sets the dataset_id of this SearchResult.

        The id of the dataset or variable within the data location  # noqa: E501

        :param dataset_id: The dataset_id of this SearchResult.
        :type dataset_id: str
        """
        if dataset_id is None:
            raise ValueError("Invalid value for `dataset_id`, must not be `None`")  # noqa: E501

        self._dataset_id = dataset_id

    @property
    def variable_id(self) -> str:
        """Gets the variable_id of this SearchResult.

        The id of the variable  # noqa: E501

        :return: The variable_id of this SearchResult.
        :rtype: str
        """
        return self._variable_id

    @variable_id.setter
    def variable_id(self, variable_id: str):
        """Sets the variable_id of this SearchResult.

        The id of the variable  # noqa: E501

        :param variable_id: The variable_id of this SearchResult.
        :type variable_id: str
        """
        if variable_id is None:
            raise ValueError("Invalid value for `variable_id`, must not be `None`")  # noqa: E501

        self._variable_id = variable_id

    @property
    def name(self) -> str:
        """Gets the name of this SearchResult.


        :return: The name of this SearchResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this SearchResult.


        :param name: The name of this SearchResult.
        :type name: str
        """

        self._name = name

    @property
    def description(self) -> str:
        """Gets the description of this SearchResult.


        :return: The description of this SearchResult.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this SearchResult.


        :param description: The description of this SearchResult.
        :type description: str
        """

        self._description = description

    @property
    def score(self) -> float:
        """Gets the score of this SearchResult.

        Ranking of the dataset or variable based on its  proximity to the search of interest.   # noqa: E501

        :return: The score of this SearchResult.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score: float):
        """Sets the score of this SearchResult.

        Ranking of the dataset or variable based on its  proximity to the search of interest.   # noqa: E501

        :param score: The score of this SearchResult.
        :type score: float
        """
        if score is None:
            raise ValueError("Invalid value for `score`, must not be `None`")  # noqa: E501

        self._score = score
