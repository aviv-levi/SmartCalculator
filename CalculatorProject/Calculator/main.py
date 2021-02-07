from calculator import Calculator
from calculator import Position


def main():
    calculator = Calculator()
    
    # an example of adding operator to the calculator in one simple line.
    # calculator.addOperator('#', lambda a: a + 1, 15, Position.LEFT)

    while True:
        try:
            expression = input('>>> ')
            result = calculator.evaluate(expression)
            if result is not None:
                print(result)
        except Exception:
            print('something went wrong, try again.')



if __name__ == "__main__":
    main()
