class quadratic:
    """
    This class will be used to represent the left hand side of the quadratic
    equation.

    a - integer
    b - integer
    c - integer
    """
    

    

    def __init__(self,a,b,c):

        self.a = a
        self.b = b
        self.c = c
        
    """
    def quadratic_function(shape,x):
        return quadratic.a
               quadratic.b
               quadratic.c
            
    """
   
    def evaluate_quadratic(shape,x):
        """
        This function will evaluate the quadratic equation
        when given a shpae with a.b.c and then a seperate
        value x

        shape -- shape
        x - integer

        return integer

        """
        d = ((shape.a*x)** 2) + (shape.b * x) + shape.c
        return d
        
shape1 = quadratic(3,4,5)
shape2 = quadratic(1,3,5)
shape3 = quadratic(4,5,6)

assertEqual(quadratic.evaluate_quadratic(shape1,3),98)
assertEqual(quadratic.evaluate_quadratic(shape2,3),23)
assertEqual(quadratic.evaluate_quadratic(shape3,3),165)
