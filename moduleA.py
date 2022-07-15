class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        print(f"Area of {self} ---> {self.length * self.width} cm2")

    def __str__(self):
        return f"Rectangle with length {self.length} cm and width {self.width} cm"