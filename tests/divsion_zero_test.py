"""Testing division with zero as denominator"""
from calc.calculations.division import Division


def test_calculation_division():
    """testing that our calculator returns 'error' when dividing by zer0"""
    #Arrange
    my_numbers = (4.0,0.0)
    division = Division(my_numbers)
    #Act
    #Assert
    assert division.get_result() == ZeroDivisionError
