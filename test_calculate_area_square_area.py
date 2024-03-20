# test_calculate_area_square.py
import pytest
from calculate_area_square import calculate_area_square

def test_calculate_area_square():
    length = 57  # You can use any arbitrary number here
    expected_area = 3251  # Changed the expected area to make the test fail
    assert calculate_area_square(length) == expected_area
