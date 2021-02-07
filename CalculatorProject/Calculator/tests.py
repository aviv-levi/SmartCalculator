import pytest
from calculator import Calculator
from operationsHelper import OperationsHelper
from validator import Validator


def test_syntax1():
    # Arrange
    operations = OperationsHelper()
    validator = Validator(operations)
    expression = '3^*2'
    # Act
    expression = validator.validationCheck(expression)
    # Assert
    assert expression is None


def test_syntax2():
    # Arrange
    operations = OperationsHelper()
    validator = Validator(operations)
    expression = '5//2^4'
    # Act
    expression = validator.validationCheck(expression)
    # Assert
    assert expression is None


def test_syntax3():
    # Arrange
    operations = OperationsHelper()
    expression = '5..2 * 4'
    validator = Validator(operations)
    # Act
    expression = validator.validationCheck(expression)
    # Assert
    assert expression is None


def test_syntax4():
    # Arrange
    operations = OperationsHelper()
    expression = '4.4.4+5.5.5'
    validator = Validator(operations)
    # Act
    expression = validator.validationCheck(expression)
    # Assert
    assert expression is None


def test_syntax5():
    # Arrange
    operations = OperationsHelper()
    expression = '!5+2*4'
    validator = Validator(operations)
    # Act
    expression = validator.validationCheck(expression)
    # Assert
    assert expression is None


def test_syntax6():
    # Arrange
    operations = OperationsHelper()
    expression = '(+(5-7))'
    validator = Validator(operations)
    # Act
    expression = validator.validationCheck(expression)
    # Assert
    assert expression is None


def test_syntax7():
    # Arrange
    operations = OperationsHelper()
    expression = '78(8+8)'
    validator = Validator(operations)
    # Act
    expression = validator.validationCheck(expression)
    # Assert
    assert expression is None


def test_gibberish():
    # Arrange
    operations = OperationsHelper()
    expression = '5+sfdfdsgh454543*/*/**/'
    validator = Validator(operations)
    # Act
    expression = validator.validationCheck(expression)
    # Assert
    assert expression is None


def test_empty():
    # Arrange
    operations = OperationsHelper()
    expression = '      '
    validator = Validator(operations)
    # Act
    expression = validator.validationCheck(expression)
    # Assert
    assert expression is None


def test_divideByZero():
    # Arrange
    expression = '5 / (10-10)'
    calculator = Calculator()
    # Act
    result = calculator.evaluate(expression)
    # Assert
    assert result == 'cant divide by zero'


def test_negativeFactorial():
    # Arrange
    expression = '(-5)!'
    calculator = Calculator()
    # Act
    result = calculator.evaluate(expression)
    # Assert
    assert result == 'cant factorial a negative number'


def test_noIntegerFactorial():
    # Arrange
    expression = '(5/2)!'
    calculator = Calculator()
    # Act
    result = calculator.evaluate(expression)
    # Assert
    assert result == 'cant factorial a non-integer number'


def test_veryBigResult():
    # Arrange
    expression = '1000^1000'
    calculator = Calculator()
    # Act
    result = calculator.evaluate(expression)
    # Assert
    assert result == 'result is too big'


def test_complexNumber():
    # Arrange
    expression = '(-5) ^ 0.5'
    calculator = Calculator()
    # Act
    result = calculator.evaluate(expression)
    # Assert
    assert result == 'this calculator is not support complex numbers'


def test_easy1():
    # Arrange
    expression = '11+55-33+7'
    calculator = Calculator()
    # Act
    result = calculator.evaluate(expression)
    # Assert
    assert result == 40


def test_easy2():
    # Arrange
    expression = '5*4/2'
    calculator = Calculator()
    # Act
    result = calculator.evaluate(expression)
    # Assert
    assert result == 10


def test_easy3():
    # Arrange
    expression = '5^2%7'
    calculator = Calculator()
    # Act
    result = calculator.evaluate(expression)
    # Assert
    assert result == 25


def test_easy4():
    # Arrange
    expression = '4*---7'
    calculator = Calculator()
    # Act
    result = calculator.evaluate(expression)
    # Assert
    assert result == -28


def test_easy5():
    # Arrange
    expression = '~5--~-4!'
    calculator = Calculator()
    # Act
    result = calculator.evaluate(expression)
    # Assert
    assert result == 19


def test_easy6():
    # Arrange
    expression = '5-(---(3)!)'
    calculator = Calculator()
    # Act
    result = calculator.evaluate(expression)
    # Assert
    assert result == 11


def test_easy7():
    # Arrange
    expression = '((8*(8+79*(8))-0)-0)'
    calculator = Calculator()
    # Act
    result = calculator.evaluate(expression)
    # Assert
    assert result == 5120


def test_easy8():
    # Arrange
    expression = '((90-98)+(8))'
    calculator = Calculator()
    # Act
    result = calculator.evaluate(expression)
    # Assert
    assert result == 0


def test_easy9():
    # Arrange
    expression = '700/4%3*3!'
    calculator = Calculator()
    # Act
    result = calculator.evaluate(expression)
    # Assert
    assert result == 4200


def test_easy10():
    # Arrange
    expression = '4^(3! *     2) - 10^5'
    calculator = Calculator()
    # Act
    result = calculator.evaluate(expression)
    # Assert
    assert result == 16677216


def test_easy11():
    # Arrange
    expression = '1+2-3*4/6'
    calculator = Calculator()
    # Act
    result = calculator.evaluate(expression)
    # Assert
    assert result == 1


def test_easy12():
    # Arrange
    expression = '(1+(2-(3*(4/(5+7)))))'
    calculator = Calculator()
    # Act
    result = calculator.evaluate(expression)
    # Assert
    assert result == 2


def test_easy13():
    # Arrange
    expression = '9--9*--7/--4+3'
    calculator = Calculator()
    # Act
    result = calculator.evaluate(expression)
    # Assert
    assert result == 27.75


def test_easy14():
    # Arrange
    expression = '7.2*4.3-8.8+1.47'
    calculator = Calculator()
    # Act
    result = calculator.evaluate(expression)
    # Assert
    assert result == 23.63


def test_easy15():
    # Arrange
    expression = '2^10 - 2^9 - 2^8'
    calculator = Calculator()
    # Act
    result = calculator.evaluate(expression)
    # Assert
    assert result == 256


def test_hard1():
    # Arrange
    expression = '(-1--1-1-1-1)--2-24/(4*2)+3.100+4!+(~1)'
    calculator = Calculator()
    # Act
    result = calculator.evaluate(expression)
    # Assert
    assert result == 22.1


def test_hard2():
    # Arrange
    expression = '((1+1)!^2)*5$6+(21&-(1+4)^3)'
    calculator = Calculator()
    # Act
    result = calculator.evaluate(expression)
    # Assert
    assert result == -101


def test_hard3():
    # Arrange
    expression = '3^4%5&6$7@~8'
    calculator = Calculator()
    # Act
    result = calculator.evaluate(expression)
    # Assert
    assert result == 1


def test_hard4():
    # Arrange
    expression = '~(123@((145*2/4%6-6/7)@(3^5-9000)))'
    calculator = Calculator()
    # Act
    result = calculator.evaluate(expression)
    # Assert
    assert result == 2109.839285714286


def test_hard5():
    # Arrange
    expression = '--((1+2@3$3$5$3)%4%3%2%1%-0.5%9)'
    calculator = Calculator()
    # Act
    result = calculator.evaluate(expression)
    # Assert
    assert result == 0


def test_hard6():
    # Arrange
    expression = '24%12^2-7*9&(2+3-4+6$22--8--~((9+8)!))'
    calculator = Calculator()
    # Act
    result = calculator.evaluate(expression)
    # Assert
    assert result == 2489811996671783.0


def test_hard7():
    # Arrange
    expression = '7&8*22^3!-7^3+((22%2 * 7)+3$5^3&~7)'
    calculator = Calculator()
    # Act
    result = calculator.evaluate(expression)
    # Assert
    assert result == 793658985.0000128


def test_hard8():
    # Arrange
    expression = '(123 @ ((145*2/4%6-6/7) @ ~(3^5 - 9000)))'
    calculator = Calculator()
    # Act
    result = calculator.evaluate(expression)
    # Assert
    assert result == 2268.660714285714


def test_hard9():
    # Arrange
    expression = '87^3%2&66@45%((22%4$2^2)+7*6!)^~2 *6'
    calculator = Calculator()
    # Act
    result = calculator.evaluate(expression)
    # Assert
    assert result == 1.3836802264343499e-11


def test_hard10():
    # Arrange
    expression = '4+((6*7)/2-4^0.5)--4%2'
    calculator = Calculator()
    # Act
    result = calculator.evaluate(expression)
    # Assert
    assert result == 23


def test_hard11():
    # Arrange
    expression = '---6&22%(2+6-5)^2-2&21$221@0'
    calculator = Calculator()
    # Act
    result = calculator.evaluate(expression)
    # Assert
    assert result == -110.5


def test_hard12():
    # Arrange
    expression = '5!-52&5 * 2-((2 * 2)+45^0.5+~2)'
    calculator = Calculator()
    # Act
    result = calculator.evaluate(expression)
    # Assert
    assert result == 101.29179606750063


def test_hard13():
    # Arrange
    expression = '----~4+67 * 2-4522/221+(2&23 * 22%3^2)-7*2@4'
    calculator = Calculator()
    # Act
    result = calculator.evaluate(expression)
    # Assert
    assert result == 90.53846153846155


def test_hard14():
    # Arrange
    expression = '24%12^2-7*9&(2+3-4+6$22--8--~9+8!)'
    calculator = Calculator()
    # Act
    result = calculator.evaluate(expression)
    # Assert
    assert result == -63


def test_hard15():
    # Arrange
    expression = '005*2^2&2-7&88+224@26-(43-44+66&2----45*(321&2))'
    calculator = Calculator()
    # Act
    result = calculator.evaluate(expression)
    # Assert
    assert result == 47


def test_hard16():
    # Arrange
    expression = '9*~(6+6)+2^2'
    calculator = Calculator()
    # Act
    result = calculator.evaluate(expression)
    # Assert
    assert result == -104.0


def test_hard17():
    # Arrange
    expression = '----~4+67*2-4522/221+(2&23*22%3^2)-7*2@4'
    calculator = Calculator()
    # Act
    result = calculator.evaluate(expression)
    # Assert
    assert result == 90.53846153846155


def test_hard18():
    # Arrange
    expression = '18-6^2+5%4$3+2+4+5+6-------9+7&5/3.2%4.2'
    calculator = Calculator()
    # Act
    result = calculator.evaluate(expression)
    # Assert
    assert result == -7.4375


def test_hard19():
    # Arrange
    expression = '5235^2-7 * 22%(3!+45-7 * (44$2@12))'
    calculator = Calculator()
    # Act
    result = calculator.evaluate(expression)
    # Assert
    assert result == 27406086


def test_hard20():
    # Arrange
    expression = '52 / (93----98---15*2+3!) % 89.12'
    calculator = Calculator()
    # Act
    result = calculator.evaluate(expression)
    # Assert
    assert result == 0.6676938880328711
