

class IllegalArguementError(ValueError):
    def __init__(self, arguement, message="Salary is not in (5000, 15000) range"):
        self.arguement = arguement
        self.message = message
        super().__init__(self.message)