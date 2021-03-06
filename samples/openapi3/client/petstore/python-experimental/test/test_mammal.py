# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import petstore_api


class TestMammal(unittest.TestCase):
    """Mammal unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMammal(self):
        """Test Mammal"""

        # tests that we can make a BasquePig by traveling through descendant discriminator in Pig
        model = petstore_api.Mammal(class_name="BasquePig")
        assert isinstance(model, petstore_api.BasquePig)


if __name__ == '__main__':
    unittest.main()
