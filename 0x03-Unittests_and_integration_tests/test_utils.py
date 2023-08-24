#!/usr/bin/env python3
'''
Test module for utils
'''

import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized

from typing import (
    Dict,
    Mapping,
    Sequence,
    Union,
)

from utils import (
    access_nested_map
)


class TestAccessNestedMap(unittest.TestCase):
    '''
    Tests utils.access_nested_map function
    '''

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self,
            nested_map: Mapping,
            path: Sequence,
            expected: Union[Dict, int]
            ) -> None:
        '''
        Tests output of access_nested_map
        '''
        self.assertEqual(access_nested_map(nested_map, path), expected)
