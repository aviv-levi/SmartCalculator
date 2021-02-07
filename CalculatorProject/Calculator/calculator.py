import formatting
from exceptions import *
from solver import Solver
from validator import Validator
from operationsHelper import OperationsHelper
from operationsHelper import Position

# This class represent the calculator


class Calculator:

    def __init__(self):
        self.operations = OperationsHelper()
        self.validator = Validator(self.operations)
        self.solver = Solver(self.operations)

    def evaluate(self, expression):
        expression = self.validator.validationCheck(expression)
        if expression is not None:
            try:
                return self.solver.solve(expression)
            except ZeroDivisionError:
                return 'cant divide by zero'
            except OverflowError:
                return 'result is too big'
            except RecursionError:
                return 'expression is too long'
            except NegativeFactorialError:
                return 'cant factorial a negative number'
            except NoIntegerFactorialError:
                return 'cant factorial a non-integer number'
            except ComplexNumberError:
                return 'this calculator is not support complex numbers'

    def addOperator(self, operator, method, rank, position):
        self.operations.addOperator(operator, method, rank, position)
