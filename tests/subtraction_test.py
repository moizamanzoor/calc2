"""Testing Subtraction"""
from calc.calculations.subtraction import Subtraction

def test_calculation_subtraction():
    """testing that our calculator has a static method for addition"""
    #Arrange
    my_numbers = (2.0,1.0)
    subtraction = Subtraction(my_numbers)
    #Act
    #Assert
    assert subtraction.get_result() == 1



