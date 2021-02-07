from enum import Enum
from exceptions import *


class Position(Enum):
    LEFT = 0
    MIDDLE = 1
    RIGHT = 2

# This class responsible to the operations in the calculator


class OperationsHelper:

    def __init__(self):
        # dict of operators,
        # for each operator(key) there is a tuple value
        # the tuple have pointer to function of operator and operator rank
        self.operators = {
            '+': (self._Add, 1, Position.MIDDLE),
            '-': (self._Sub, 1, Position.MIDDLE),
            '*': (self._Mul, 2, Position.MIDDLE),
            '/': (self._Div, 2, Position.MIDDLE),
            '^': (self._Pow, 3, Position.MIDDLE),
            '~': (self._Negate, 6, Position.LEFT),
            '%': (self._Modulo, 4, Position.MIDDLE),
            '!': (self._Factorial, 6, Position.RIGHT),
            '@': (self._Avarage, 5, Position.MIDDLE),
            '$': (self._Max, 5, Position.MIDDLE),
            '&': (self._Min, 5, Position.MIDDLE)
        }

    def addOperator(self, operator, method, rank, position):
        """
        Insert operation to dict
        :param operator: given operator
        :param method: method that operator represent
        :param rank: rank of operator
        :param position: position of operator related to the operand/s
        """
        if operator in self.operators.keys():
            print('operator with that sign is already exists, try other sign.')
            return False
        self.operators[operator] = (method, rank, position)
        return True

    def hasOperator(self, expression):
        """
        :param expression: given expression
        :return: True if expression have at least one operator,False if not
        """
        for expressionElement in expression:
            if expressionElement in self.operators.keys():
                return True
        return False

    def isOperator(self, sign):
        """
        :param sign: given sign
        :return: True if sign is operator,False if not
        """
        # check if sign is an key in operators dict
        return sign in self.operators

    def isDigit(self, sign):
        """
            This method check if the given sign is a digit
        :param sign: given sign
        :return:
        """
        # checks if the ascii value of the sign is between the ascii value og zero and nine
        return ord('0') <= ord(sign) <= ord('9')

    def isNegativeSign(self, expression, expression_element_index):
        """
            This method checks if the given element is a negative sign minus
        :param expression: given expression
        :param expression_element_index: given index of element
        :return: true if the element is negative sign minus, false if not
        """
        expressionLength = len(expression)
        expressionElement = expression[expression_element_index]
        # if element is not minus
        if expressionElement != '-':
            return False
        if expression_element_index > 0:
            # if before the element it is open parentheses or left operator or middle operator
            beforeExpressionElement = expression[expression_element_index - 1]
            if beforeExpressionElement != '(':
                if not (self.isOperator(beforeExpressionElement) and self.getPosition(
                        beforeExpressionElement) != Position.RIGHT):
                    return False
        if expression_element_index < expressionLength - 1:
            afterExpressionElement = expression[expression_element_index + 1]
            # if after the element it is open parentheses or left operator or digit
            if afterExpressionElement != '(':
                if not (self.isOperator(afterExpressionElement) and self.getPosition(
                        afterExpressionElement) == Position.LEFT):
                    if not self.isDigit(afterExpressionElement):
                        return False
        return True

    def operate(self, operator):
        """
        :param operator: given operator
        :return: Function that the operator represents
        """
        # get the value (function,rank) of given operator as key in dict
        # return first value of tuple (function)
        return self.operators[operator][0]

    def getRank(self, operator):
        """
        :param operator:  given operator
        :return: Rank of function that the operator represents
        """
        # get the value (function,rank) of given operator as key in dict
        # return second value of tuple (rank)
        return self.operators[operator][1]

    def getHighestRank(self):
        # get operators dictionary as list of tuple (key , value)
        operatorsAsList = self.operators.items()
        # compare every element by their rank (the value is tuple, the rank is value in the tuple)
        compareBy = lambda operator: operator[1][1]
        # get the operator with the biggest rank
        maxOperatorElement = max(operatorsAsList, key=compareBy)
        # return this operator rank
        return maxOperatorElement[1][1]

    def getPosition(self, operator):
        """
        :param operator:  given operator
        :return: Rank of function that the operator represents
        """
        # get the value (function,rank) of given operator as key in dict
        # return second value of tuple (rank)
        return self.operators[operator][2]

    def _Add(self, num1, num2):
        """
        :param num1: first argument
        :param num2: second argument
        :return: sum of them.
        """
        return num1 + num2

    def _Sub(self, num1, num2):
        """
        :param num1: first argument
        :param num2: second argument
        :return: subtraction of them.
        """
        return num1 - num2

    def _Div(self, num1, num2):
        """
       :param num1: first argument
       :param num2: second argument
       :return: division of them.
       """
        return num1 / num2

    def _Mul(self, num1, num2):
        """
       :param num1: first argument
       :param num2: second argument
       :return: multiplication of them.
       """
        return num1 * num2

    def _Avarage(self, num1, num2):
        """
       :param num1: first argument
       :param num2: second argument
       :return: avarage of them.
       """
        return (num1 + num2) / 2

    def _Pow(self, num1, num2):
        """
       :param num1: first argument
       :param num2: second argument
       :return: first powered by second
       """
        return num1 ** num2

    def _Negate(self, val):
        """
      :param val: given value
      :return: negative of that given value
      """
        return val * -1

    def _Modulo(self, num1, num2):
        """
       :param num1: first argument
       :param num2: second argument
       :return: first modulo second.
       """
        return num1 % num2

    def _Factorial(self, num):

        # check if number is negative
        if num < 0:
            raise NegativeFactorialError()
        # check if number is not-integer
        length = int(num)
        if num != length:
            raise NoIntegerFactorialError()
        # calculate the factorial of the number
        res = 1
        for num in range(length, 1, -1):
            res *= num
        return res

    def _Max(self, num1, num2):
        """
       :param num1: first argument
       :param num2: second argument
       :return: bigger argument of them
       """
        return num1 if num1 > num2 else num2

    def _Min(self, num1, num2):
        """
       :param num1: first argument
       :param num2: second argument
       :return: smaller argument of them
       """
        return num1 if num1 < num2 else num2
