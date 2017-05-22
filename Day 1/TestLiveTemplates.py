import math

class Point:
    """
    Represents a point in 2-D geometric space
    """
    def __init__(self, x=0, y=0):
        """
        Initializes the position of a new point
        If they are not specified, the point defaults to the origin
        :param x: x coordinate
        :param y: y coordinate
        """
        self.x = x
        self.y = y

    def reset(self):
        """
        Reset point to the origin in 2D space
        :return:  Nothis
        """
        self.move(0,0)

    def move(self, x, y):
        """
        Move a point to a new location in 2D space
        :param x: x - coordinates
        :param y:  y coordinate
        :return: nothing
        """
        self.x = x
        self.y = y

    def calculate_distance(self, other_point):
        """
        Calculate the distance from this point to a second point
        passed as a parameter
        This function uses Pythagorean Theorem to claculate the distance
        the tow points
        :param other_point: second poit to calculate distance
        :return: The distance between tow Points (float)
        """
        return math.sqrt(((self.x - other_point.x)**2) + ((self.y - other_point.y)**2))


def main():
    """
    Test code to test the functions
    :return:  nothing
    """
    p1 = Point()
    print (p1.x, p1.y)
    p2 = Point(5, 8)
    print (p2.x, p2.y)
    p2.reset()
    print(p2.x, p2.y)
    p2.move(9, 10)
    print(p2.x, p2.y)
    print(p1.calculate_distance(p2))
    assert(p2.calculate_distance(p1) == p1.calculate_distance(p2))


if __name__ == '__main__':
    main()
    exit(0)