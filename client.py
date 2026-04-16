import sys, Ice
import Demo
 
communicator = Ice.initialize(sys.argv)

base = communicator.stringToProxy("SimplePrinter:default -p 11000")
printer = Demo.PrinterPrx.checkedCast(base)
if not printer:
    raise RuntimeError("Invalid proxy")

printer.printString("Hello World!")
printer.printInt(42)

base_calc = communicator.stringToProxy("SimpleCalculator:default -p 11000")
calc = Demo.CalculatorPrx.checkedCast(base_calc)
if not calc:
    raise RuntimeError("Invalid proxy for Calculator")

result = calc.add(10, 20)
print("10 + 20 =", result)
