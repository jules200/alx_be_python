class Calculator:
    calculation_type = "Arithmetic Operations"
    
    @staticmethod
    def add(a, b):
        ad = a + b
        return ad
         
    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b