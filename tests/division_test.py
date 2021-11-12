"""Testing division"""
from calc.calculations.division import Division


def test_calculation_division():
    """testing that our calculator has a static method for division"""
    #Arrange
    my_numbers = (4.0,2.0)
    division = Division(my_numbers)
    #Act
    #Assert
    assert division.get_result() == 2.0
