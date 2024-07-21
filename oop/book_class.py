class Book:
    def __init__(self, title, author, year):
        self.title =title
        self.author = author
        self.year = year
        
    def __del__(self):
        self.title.close()
    
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"
        
