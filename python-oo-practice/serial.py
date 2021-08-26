"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=None):
        self.serial_number = start - 1
        self.rs = start - 1
    
    def __repr__(self):
        return str(self.serial_number)
    
    def reset(self):
        self.serial_number = self.rs
    
    def generate(self):
        self.serial_number+=1
        return self.serial_number