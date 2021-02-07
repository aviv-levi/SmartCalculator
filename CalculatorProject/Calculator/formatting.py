
def removeWhiteCharacter(expression):
    """
        This method remove all white characters in the given expression.
    :param expression: given expression.
    :return: expression without white characters.
    """
    # replace function replaces all ' ' characters to empty character
    return expression.replace(" ", "")


def compressMinuses(operations, expression):
    """
        This method compresses all sequence of minuses to minus,plus or nothing.
    :param operations: operations helper.
    :param expression: given expression
    :return: expression after compressing
    """

    # the function search for a sequence of minuses, if the size of sequence
    # is odd, they all just like one minus, if the size is even ,they all just
    # like one plus or nothing depend on the element before the sequence.

    # counter of sequence of minuses
    minusCounter = 0
    # new formatted compressed expression
    compressedExpression = ''
    expressionLength = len(expression)
    # last element before a sequence of minuses
    elementBeforeMinusSequence = None
    for expressionElementIndex in range(expressionLength):
        expressionElement = expression[expressionElementIndex]
        # if the current element is minus, increase counter by one
        if expressionElement == '-':
            minusCounter += 1
        else:
            # if the the element is not minus, the sequence is over or there is no sequence
            # if counter is more then zero there is a sequence, so we will check the size of the sequence
            # and the element before the sequence
            if minusCounter > 0:
                # even sequence size
                if minusCounter % 2 == 0:
                    # it is will not be the first element of compressed expression
                    if len(compressedExpression) != 0:
                        # the element before the sequence is not operator and not open parentheses
                        if not operations.isOperator(elementBeforeMinusSequence):
                            if elementBeforeMinusSequence != '(':
                                # add to the new compressed expression a plus
                                compressedExpression += '+'
                    # if the size of the sequence is even, and is not following the terms ^ , it
                    # will just 'add' an empty element
                else:
                    # if odd sequence size, add a minus to the compressed expression
                    compressedExpression += '-'
                # the minus sequence is over, restart the counter
                minusCounter = 0
            # save last element as element before minus sequence
            elementBeforeMinusSequence = expressionElement
            # adding current element to the compressed expression
            compressedExpression += expressionElement
    # last check for sequence that isn't over in the expression
    if minusCounter > 0:
        if minusCounter % 2 == 0:
            if len(compressedExpression) != 0:
                if not operations.isOperator(elementBeforeMinusSequence):
                    if elementBeforeMinusSequence != '(':
                        compressedExpression += '+'
        else:
            compressedExpression += '-'
    return compressedExpression
