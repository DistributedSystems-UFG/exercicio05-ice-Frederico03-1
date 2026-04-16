import sys, Ice
import Demo
 
class PrinterI(Demo.Printer):
    def printString(self, s, current=None):
        print(s)
        
    def printInt(self, val, current=None):
        print("Value:", val)

class CalculatorI(Demo.Calculator):
    def add(self, a, b, current=None):
        return a + b

communicator = Ice.initialize(sys.argv) 

adapter = communicator.createObjectAdapterWithEndpoints("SimpleAdapter", "default -p 11000")

object = PrinterI()
adapter.add(object, communicator.stringToIdentity("SimplePrinter"))

calc_object = CalculatorI()
adapter.add(calc_object, communicator.stringToIdentity("SimpleCalculator"))

adapter.activate()

communicator.waitForShutdown()
