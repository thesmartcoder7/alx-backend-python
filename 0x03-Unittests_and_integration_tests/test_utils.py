#!/usr/bin/env python3
"""
Test suite for utils.py
"""

import unittest
from unittest.mock import patch
from typing import Mapping, Sequence, Any

from parameterized import parameterized

from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(
        self, nested_map: Mapping, path: Sequence, expected: Any
    ):
        """Test access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([({}, ("a",)), ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(
        self, nested_map: Mapping, path: Sequence
    ) -> None:
        """Test access_nested_map exception"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test get_json"""

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    @patch("utils.requests.get")
    def test_get_json(self, test_url: str, test_payload: dict, mock_get: Any):
        """Test get_json"""
        mock_get.return_value.json.return_value = test_payload
        self.assertEqual(get_json(test_url), test_payload)
        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """
        Test the memoization decorator, memoize
    """

    def test_memoize(self):
        """
            Test that utils.memoize decorator works as intended
        """
        class TestClass:

            def a_method(self):
                """Test method"""
                return 42

            @memoize
            def a_property(self):
                """Test property"""
                return self.a_method()

        with patch.object(TestClass, "a_method") as mock_method:
            test = TestClass()
            test.a_property
            test.a_property
            mock_method.assert_called_once()
