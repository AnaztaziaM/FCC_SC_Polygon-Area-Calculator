class Rectangle:

    def __init__(self, width, height ):
        self.width = width
        self.height = height

    def __str__(self):
        shape_in_lines = "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"
        return shape_in_lines

    def set_width (self, number_w):
        self.width = number_w

    def set_height (self, number_h):
        self.height = number_h

    def get_area (self):
        area = self.width * self.height
        return area

    def get_perimeter (self):
        perimeter = 2 * self.width + 2 * self.height
        return perimeter

    def get_diagonal (self):
        diagonal = (self.width ** 2 + self.height ** 2)** 0.5
        return  diagonal

    def get_picture(self):
        lines = self.height
        colums = self.width
        if lines > 50 or colums > 50:
            too_big_pictures = "Too big for picture."
            return  too_big_pictures
        else:
            shape_picture = ((colums * "*")+ "\n")*lines
            return  shape_picture

    def get_amount_inside(self, shape):
        w = self.width // shape.width
        h = self.height // shape.height
        amount= w*h
        return amount


class Square (Rectangle):

    def __init__(self, length):
        self.width = length
        self.height = length

    def __str__(self):
        shape_in_line = "Square(side=" + str(self.width) + ")"
        return shape_in_line

    def set_side (self, number_s):
        self.width = number_s
        self.height = number_s

    def set_width (self, number_w):
        super(Square, self).set_width(number_w)
        self.height = number_w

    def set_height (self, number_h):
        super(Square, self).set_height(number_h)
        self.width = number_h

    def get_area(self):
        return super(Square, self).get_area()

    def get_perimeter(self):
        return super(Square, self).get_perimeter()

    def get_diagonal(self):
        return super(Square, self).get_diagonal()

    def get_picture(self):
        return super(Square, self).get_picture()

    def get_amount_inside(self):
        return super(Square, self).get_amount_inside()
