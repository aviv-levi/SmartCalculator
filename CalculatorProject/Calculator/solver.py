from operationsHelper import Position
from exceptions import *

# This class responsible to the solving part of the calculator


class Solver:

    def __init__(self, operations):
        self._operations = operations

    def solve(self, expression):
        """
            Solve function. calls to the recursion method.
        :param expression:
        :return:
        """

        # calls to the recursion method.
        result = self.solve_expression(expression)
        # if it is complex , raise error
        if type(result) == complex:
            raise ComplexNumberError()
        return result

    def _findLowestRankingOperator(self, expression):
        """
            Finding the operator with the lowest rank.
        :param expression: current expression.
        :return: the lowest ranking operator.
        """

        # const of the extra value of rank because of the parentheses
        EXTRA = self._operations.getHighestRank() + 1

        # lowest rank of operator ,start from the biggest it can be
        minimumRank = float('inf')
        # index of lowest ranking operator
        lowestRankingOperatorIndex = None

        # extra to rank , changes by the parentheses
        rankExtra = 0

        expressionLength = len(expression)
        for expressionElementIndex in range(expressionLength):
            expressionElement = expression[expressionElementIndex]
            # open parentheses will increase the extra , close will decrease
            if expressionElement == '(':
                rankExtra += EXTRA
            elif expressionElement == ')':
                rankExtra -= EXTRA
            elif self._operations.isOperator(expressionElement):
                if self._operations.isNegativeSign(expression, expressionElementIndex):
                    # if negative sign on expression it is like left operator on the expression
                    # have same rank as regular minus
                    # else it is negative sign on simple operand, we wouldn't want to choose that
                    # because at the convert to float it will be evaluate
                    if expressionElementIndex == 0 or expression[expressionElementIndex - 1] == '(':
                        current_rank = rankExtra + self._operations.getRank(expressionElement)
                    else:
                        current_rank = EXTRA + rankExtra
                    # compression between operands
                    if current_rank <= minimumRank:
                        minimumRank = current_rank
                        lowestRankingOperatorIndex = expressionElementIndex
                else:
                    leftOperatorsCompression = False
                    current_rank = self._operations.getRank(expressionElement) + rankExtra
                    if lowestRankingOperatorIndex is not None:
                        lowestRankingOperator = expression[lowestRankingOperatorIndex]
                        lowestRankingOperatorPosition = self._operations.getPosition(lowestRankingOperator)
                        currentPosition = self._operations.getPosition(expressionElement)
                        if currentPosition == lowestRankingOperatorPosition == Position.LEFT:
                            # in case of left operators compression , when left operator from left is stronger
                            leftOperatorsCompression = True
                    # in case of left operators compression , we will prefer the one at left (if same)
                    if leftOperatorsCompression:
                        if current_rank < minimumRank:
                            minimumRank = current_rank
                            lowestRankingOperatorIndex = expressionElementIndex
                    else:
                        if current_rank <= minimumRank:
                            minimumRank = current_rank
                            lowestRankingOperatorIndex = expressionElementIndex

        return lowestRankingOperatorIndex

    def solve_expression(self, expression):
        """
            Solving the expression. Recursive method.
        :param expression: given expression
        :return: value of the expression
        """

        expressionLength = len(expression)
        # if it have no operators (operand) or minus and have no operators (negative operand)
        if not self._operations.hasOperator(expression) or (expression[0] == '-' and not self._operations.hasOperator(expression[1:])):
            # if it has parentheses wraps it , we move forward without them
            if expression[0] == '(':
                rightToOpenParentheses = expression[1:]
                return self.solve_expression(rightToOpenParentheses)
            # if it has minus sign at the start and have no operators after it
            # we will move forward without it and multiply the result by negative one
            if expression[0] == '-':
                rightToOperator = expression[1:]
                return -1 * self.solve_expression(rightToOperator)
            if expression[expressionLength - 1] == ')':
                leftToCloseParentheses = expression[:expressionLength - 1]
                return self.solve_expression(leftToCloseParentheses)
            # if it not wrap with something we will return the value of the operand
            return float(expression)

        # get the lowest ranking operator
        lowestRankingOperatorIndex = self._findLowestRankingOperator(expression)
        lowestRankingOperator = expression[lowestRankingOperatorIndex]
        # if it negative minus , move forward multiply negative one
        if self._operations.isNegativeSign(expression, lowestRankingOperatorIndex):
            rightToOperator = expression[lowestRankingOperatorIndex + 1:]
            result = self.solve_expression(rightToOperator)
            return -1 * result
        else:

            operatorPosition = self._operations.getPosition(lowestRankingOperator)
            # if it is a left operator
            if operatorPosition == Position.LEFT:
                rightToOperator = expression[lowestRankingOperatorIndex + 1:]
                # move forward with right side
                result = self.solve_expression(rightToOperator)
                # checks it is not complex
                if type(result) == complex:
                    raise ComplexNumberError()
                # return his operation
                return self._operations.operate(lowestRankingOperator)(result)
            # if it is a middle operator
            elif operatorPosition == Position.MIDDLE:
                leftToOperator = expression[:lowestRankingOperatorIndex]
                rightToOperator = expression[lowestRankingOperatorIndex + 1:]
                # move forward with left side
                resultFromLeft = self.solve_expression(leftToOperator)
                # move forward with right side
                resultFromRight = self.solve_expression(rightToOperator)
                # checks it is not complex
                if type(resultFromLeft) == complex or type(resultFromRight) == complex:
                    raise ComplexNumberError()
                # return his operation
                return self._operations.operate(lowestRankingOperator)(resultFromLeft, resultFromRight)
            # if it is a right operator
            elif operatorPosition == Position.RIGHT:
                leftToOperator = expression[:lowestRankingOperatorIndex]
                # move forward with left side
                result = self.solve_expression(leftToOperator)
                # checks it is not complex
                if type(result) == complex:
                    raise ComplexNumberError()
                # return his operation
                return self._operations.operate(lowestRankingOperator)(result)
