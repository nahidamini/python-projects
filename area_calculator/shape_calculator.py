class Rectangle:

  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return float(((self.width**2 + self.height**2)**.5))

  def get_picture(self):
    shape = ""
    w = '*' * self.width
    if self.height > 50 or self.width > 50:
      shape += 'Too big for picture.'
    else:
      for h in range(0, self.height):
        shape += w + '\n'
    return shape

  def __str__(self):
    if self.width == self.height:
      return f'Square(side={self.width})'
    else:
      return f'Rectangle(width={self.width}, height={self.height})'

  def get_amount_inside(self, shape):
    if isinstance(shape, Rectangle):
      new_shape = Rectangle(shape.width, shape.height)
      new_area = new_shape.get_area()
      shape_area = self.get_area()
      return shape_area // new_area


class Square(Rectangle):

  def __init__(self, width):
    super().__init__(width, width)

  def set_side(self, side):
    super().set_height(side)
    super().set_width(side)

  def set_width(self, width):
    self.set_side(width)

  def set_height(self, height):
    self.set_side(height)
