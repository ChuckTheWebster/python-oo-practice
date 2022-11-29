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
    def __init__(self, start):
        """Initiate Serial instance with start number and save start reference"""
        self.start = start
        self.start_reference = start
        self.called_before = False

    def generate(self):
        """On first call, returns start, subsequent calls return Serial (start)
        incremented by one"""
        if self.called_before == False:
            self.called_before = True
            return self.start
        else:
            self.start += 1
            return self.start

    def reset(self):
        """Resets Serial to start reference"""
        self.start = self.start_reference
        self.called_before = False
