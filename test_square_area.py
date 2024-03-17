# test_square_area.py

import pytest
from square import calculate_area

def test_calculate_area():
    assert calculate_area(5) == 25  # Example unit test
    assert calculate_area(57) == 6241  # Intentional failure, incorrect expected output

# Run the tests if this script is executed directly
if __name__ == "__main__":
    pytest.main()
