# Interface Segregation Principle 


class Printer:
    def print(self):
        pass
    
class Scanner:
    def scan(self):
        pass


class Pnew(Printer):
    pass


class Snew(Scanner):
    pass


class PSnew(Printer, Scanner):
    pass