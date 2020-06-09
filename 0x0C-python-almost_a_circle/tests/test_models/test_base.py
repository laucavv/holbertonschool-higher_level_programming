#!/usr/bin/python3
"""
    Tests for the Base class
"""

import unittest
import pep8
import json
import sys
import io
from models import base
from models.base import Base


class TestDocsB(unittest.TestCase):
    """ check for documentation """
    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(base.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(Base.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(Base):
            self.assertTrue(len(func.__doc__) > 0)


class TestPep8B(unittest.TestCase):
    """ check for pep8 validation """
    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/base.py'
        file2 = 'tests/test_models/test_base.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestClassBase(unittest.TestCase):
    """  Class containing functions to
        test on the Bass class
    """
    def setUp(self):
        """ Method to set the start point  """
        Base._Base__nb_objects = 0

    def test_b0(self):
        """
            Instance creation verification,
            with its respective id
        """
        base_0 = Base()
        base_1 = Base(23)
        base_2 = Base()

        self.assertEqual(base_0.id, 1)
        self.assertEqual(base_1.id, 23)
        self.assertEqual(base_2.id, 2)
