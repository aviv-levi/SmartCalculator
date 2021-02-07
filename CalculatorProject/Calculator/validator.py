import formatting
from operationsHelper import Position


# This class responsible to the validation of the expression

class Validator:

    def __init__(self, operations):
        self.operations = operations

    def validationCheck(self, expression):
        """
            This method checks the validation of the given expression
        :param expression: given expression
        :return: expression after formatting if expression is valid , None if not.
        """
        # remove white spaces from the given expression
        expression = formatting.removeWhiteCharacter(expression)
        # first validation checks, without our minuses formatting
        if self._emptyCheck(expression) and self._elementsTypeValidation(expression) and self._dotsValidation(
                expression) and self._parenthesesValidation(expression):
            # after first validation checks, we will format the expression minuses sequences
            expression = formatting.compressMinuses(self.operations, expression)
            # if we passed the second validation check, we'll return the expression after formatting
            if self._missingValidation(expression) and self._concatenationValidation(expression):
                return expression
        # if validation didn't complete successfully ,we'll return None
        return None

    def _emptyCheck(self, expression):
        """
            This method checks if the given expression is empty.
        :param expression: given expression.
        :return: true if expression is not empty , false if it is
        """

        # split function convert the given expression to list
        expressionAsList = expression.split()
        # split don't take empty spaces as elements in the list
        # so if the given expression is empty the length of the list would be zero
        lengthOfExpressionAsList = len(expressionAsList)
        if lengthOfExpressionAsList == 0:
            print('empty expression')
            return False
        return True

    def _parenthesesValidation(self, expression):
        """
            This method checks the validation of the parentheses in the given expression.
        :param expression: given expression
        :return: true if parentheses are valid, false if not
        """

        # the function push the expression the stack , when we meet close parentheses we will
        # pop every element until we meet an open parentheses, if we not have elements between
        # those parentheses it is too much parentheses
        # if we meet close parentheses and we are not have an open parentheses in the stack, the
        # parentheses are not opened , and if at the end we still have open parentheses, the
        # parentheses are not closed

        # stack of the given expression elements
        expressionElementsStack = []
        expressionLength = len(expression)
        for expressionElementIndex in range(expressionLength):
            expressionElement = expression[expressionElementIndex]
            # if expression element is close parentheses
            if expressionElement == ')':
                # and we not have an open parentheses
                if '(' not in expressionElementsStack:
                    print('parentheses are not opened')
                    return False
                # head of the stack
                expressionElementsStackTop = expressionElementsStack.pop()
                # if between the parentheses we not have elements it is too much parentheses
                if expressionElementsStackTop == '(':
                    print('too much parentheses')
                    return False
                # popping out from the stack the elements between the parentheses
                while expressionElementsStackTop is not '(':
                    expressionElementsStackTop = expressionElementsStack.pop()
            else:
                # if it is an expression element
                expressionElementsStack.append(expressionElement)
        # if at the end we still have open parentheses, the parentheses are not closed
        if '(' in expressionElementsStack:
            print('parentheses are not closed')
            return False
        return True

    def _dotsValidation(self, expression):
        """
            This method checks the validation of the dots in the given expression.
        :param expression: given expression
        :return: true if the dots are valid , false if not

        """

        # first condition for dot to being valid is that before the dot and after the dots
        # will be digit
        # second condition for dots to being valid is that every single dot will be between operators

        # when we meet a dot the counter is increased by one, and when we meet an operator we will check the counter
        dotsBetweenOperatorsCounter = 0
        expressionLength = len(expression)
        for expressionElementIndex in range(expressionLength):
            expressionElement = expression[expressionElementIndex]
            # when the element is a dot
            if expressionElement == '.':
                # counter increased by one
                dotsBetweenOperatorsCounter += 1
                # checking our first condition ,if between the dot we don't have digits the dot is not valid
                if expressionElementIndex == 0 or expressionElementIndex == expressionLength - 1:
                    print('dots arent valid')
                    return False
                elementBeforeDot = expression[expressionElementIndex - 1]
                elementAfterDot = expression[expressionElementIndex + 1]
                if not (self.operations.isDigit(elementBeforeDot) and self.operations.isDigit(elementAfterDot)):
                    print('dots arent valid')
                    return False
            # when we meet and operator, we check that counter is not bigger then one, so the is no more then one
            # dot in an operand
            elif self.operations.isOperator(expressionElement):
                if dotsBetweenOperatorsCounter > 1:
                    print('dots arent valid')
                    return False
                # restart the counter to the next check
                dotsBetweenOperatorsCounter = 0
        # checking last time the dots
        if dotsBetweenOperatorsCounter > 1:
            print('dots arent valid')
            return False
        return True

    def _elementsTypeValidation(self, expression):
        """
            This method checks the validation of the elements type in the given expression.
        :param expression: given expression
        :return: true if elements type is valid, false if not
        """

        # for every element in the expression
        for expressionElement in expression:
            # element can be an operator , digit , dot , open parentheses and close parentheses
            if not self.operations.isOperator(expressionElement):
                if not self.operations.isDigit(expressionElement):
                    if expressionElement != '.' and expressionElement != '(' and expressionElement != ')':
                        print(expressionElement, 'is not valid')
                        return False
        return True

    def _concatenationValidation(self, expression):
        """
             This method checks the validation of concatenation between operators.
        :param expression: given expression
        :return: true if concatenations are valid, false if not
        """

        # the big problem with concatenation is the situation when there is a concatenation
        # between two operators and the one with the smaller rank is closer to the operand
        # in that situation the higher ranked operator make his operation on operator and operand instead of
        # only operand like it should be for every operation

        expressionLength = len(expression)
        for expressionElementIndex in range(expressionLength):
            if 0 < expressionElementIndex < expressionLength - 1:
                expressionElement = expression[expressionElementIndex]
                if self.operations.isOperator(expressionElement):
                    # if element is left operator
                    if self.operations.getPosition(expressionElement) == Position.LEFT:
                        expressionElementBefore = expression[expressionElementIndex - 1]
                        if self.operations.isOperator(expressionElementBefore):
                            # and if element before is left operator
                            if self.operations.getPosition(expressionElementBefore) == Position.LEFT:
                                expressionElementRank = self.operations.getRank(expressionElement)
                                expressionElementBeforeRank = self.operations.getRank(expressionElementBefore)
                                # if the element before is higher ranked then the current element
                                # and they both left operator is the problem i discover earlier
                                if expressionElementBeforeRank > expressionElementRank:
                                    print(expressionElementBefore, 'cant be before', expressionElement)
                                    return False
                    # if element is right operator
                    elif self.operations.getPosition(expressionElement) == Position.RIGHT:
                        expressionElementAfter = expression[expressionElementIndex + 1]
                        if self.operations.isOperator(expressionElementAfter):
                            # and if the element after is right operator
                            if self.operations.getPosition(expressionElementAfter) == Position.RIGHT:
                                expressionElementRank = self.operations.getRank(expressionElement)
                                expressionElementAfterRank = self.operations.getRank(expressionElementAfter)
                                # if the element after is higher ranked then the current element
                                # and they both right operator is the problem i discover earlier
                                if expressionElementAfterRank > expressionElementRank:
                                    print(expressionElementAfter, 'cant be after', expressionElement)
                                    return False
        return True

    def _missingValidation(self, expression):
        """
            This method checks the validation of the operators in the given string
        :param expression: given expression
        :return: true if no operand or operator is missing, false if not
        """
        expressionLength = len(expression)
        for expressionElementIndex in range(expressionLength):
            expressionElement = expression[expressionElementIndex]
            if self.operations.isOperator(expressionElement):
                expressionElementPosition = self.operations.getPosition(expressionElement)
                # if is left operator, so we will check left operator validation
                if expressionElementPosition == Position.LEFT:
                    if not self._leftOperatorValidation(expression, expressionElementIndex):
                        return False
                elif expressionElementPosition == Position.MIDDLE:
                    # if is middle operator, and it is not negative sign ,so we will check
                    # middle operator validation
                    if not self.operations.isNegativeSign(expression, expressionElementIndex):
                        if not self._middleOperatorValidation(expression, expressionElementIndex):
                            return False
                # if is right operator, so we will check right operator validation
                elif expressionElementPosition == Position.RIGHT:
                    if not self._rightOperatorValidation(expression, expressionElementIndex):
                        return False
            # if it is open parentheses , it can have before only open parentheses or operator
            elif expressionElement == '(':
                if expressionElementIndex > 0:
                    beforeExpressionElement = expression[expressionElementIndex - 1]
                    if beforeExpressionElement != '(':
                        if not self.operations.isOperator(beforeExpressionElement):
                            print('missing operator')
                            return False
            # if it is close parentheses , it can have after only close parentheses or operator
            elif expressionElement == ')':
                if expressionElementIndex < expressionLength - 1:
                    afterExpressionElement = expression[expressionElementIndex + 1]
                    if afterExpressionElement != ')':
                        if not self.operations.isOperator(afterExpressionElement):
                            print('missing operator')
                            return False
        return True

    def _leftOperatorValidation(self, expression, left_operator_index):
        """
            This method checks the validation of the left operator in the given string
        :param expression: given expression
        :param left_operator_index: index of the operator
        :return: true if left operator is valid
        """

        expressionLength = len(expression)
        # left operator at the end of the expression don't have an operand to make his operation with
        if left_operator_index == expressionLength - 1:
            print('missing operand')
            return False
        # if after the left operator he has open parentheses or digit or negative_sign or another left operator
        expressionElementAfter = expression[left_operator_index + 1]
        if not self.operations.isDigit(expressionElementAfter):
            if expressionElementAfter is not '(':
                if not self.operations.isNegativeSign(expression, left_operator_index + 1):
                    if self.operations.isOperator(expressionElementAfter):
                        if self.operations.getPosition(expressionElementAfter) != Position.LEFT:
                            print('missing operand')
                            return False
                    else:
                        print('missing operand')
                        return False
        if left_operator_index > 0:
            # if before the left operator he has open parentheses or operator
            expressionElementBefore = expression[left_operator_index - 1]
            if not self.operations.isOperator(expressionElementBefore):
                if expressionElementBefore is not '(':
                    print('missing operator')
                    return False
        return True

    def _rightOperatorValidation(self, expression, right_operator_index):
        """
            This method checks the validation of the right operator in the given string
        :param expression: given expression
        :param right_operator_index: index of the operator
        :return: true if right operator is valid
        """

        expressionLength = len(expression)
        # right operator at the start of the expression don't have an operand to make his operation with
        if right_operator_index == 0:
            print('missing operand')
            return False
        # if before the right operator he has close parentheses or digit or another right operator
        expressionElementBefore = expression[right_operator_index - 1]
        if not self.operations.isDigit(expressionElementBefore):
            if expressionElementBefore is not ')':
                if self.operations.isOperator(expressionElementBefore):
                    if self.operations.getPosition(expressionElementBefore) != Position.RIGHT:
                        print('missing operand')
                        return False
                else:
                    print('missing operand')
                    return False
        if right_operator_index < expressionLength - 1:
            expressionElementAfter = expression[right_operator_index + 1]
            # if after the right operator he has close parentheses or operator
            if not self.operations.isOperator(expressionElementAfter):
                if expressionElementAfter is not ')':
                    print('missing operator')
                    return False
        return True

    def _middleOperatorValidation(self, expression, middle_operator_index):

        """
            This method checks the validation of the middle operator in the given string
        :param expression: given expression
        :param middle_operator_index: index of the operator
        :return: true if middle operator is valid
        """
        expressionLength = len(expression)
        # middle operator at the start of the expression or at the end don't have an operand to make his operation with
        if middle_operator_index == 0 or middle_operator_index == expressionLength - 1:
            print('missing operand')
            return False
        # if before the middle operator he has close parentheses or digit or right operator
        expressionElementBefore = expression[middle_operator_index - 1]
        if not self.operations.isDigit(expressionElementBefore):
            if expressionElementBefore is not ')':
                if self.operations.isOperator(expressionElementBefore):
                    if self.operations.getPosition(expressionElementBefore) != Position.RIGHT:
                        print('missing operand')
                        return False
                else:
                    print('missing operand')
                    return False
        # if after the middle operator he has open parentheses or digit or negative sign or left operator
        expressionElementAfter = expression[middle_operator_index + 1]
        if not self.operations.isDigit(expressionElementAfter):
            if expressionElementAfter is not '(':
                if not self.operations.isNegativeSign(expression, middle_operator_index + 1):
                    if self.operations.isOperator(expressionElementAfter):
                        if self.operations.getPosition(expressionElementAfter) != Position.LEFT:
                            print('missing operand')
                            return False
                    else:
                        print('missing operand')
                        return False
        return True
