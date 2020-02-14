# coding: utf-8

"""
    LocationIQ

    LocationIQ provides flexible enterprise-grade location based solutions. We work with developers, startups and enterprises worldwide serving billions of requests everyday. This page provides an overview of the technical aspects of our API and will help you get started.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.directions_api import DirectionsApi  # noqa: E501
from openapi_client.rest import ApiException


class TestDirectionsApi(unittest.TestCase):
    """DirectionsApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.directions_api.DirectionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_directions(self):
        """Test case for directions

        Directions Service  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
