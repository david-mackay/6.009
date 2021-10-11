import doctest
# NO ADDITIONAL IMPORTS ALLOWED!
# You are welcome to modify the classes below, as well as to implement new
# classes and helper functions as necessary.

def tokenize(s):
    """
    Takes string s and splits it by space to create a list of elements in an algebraic expression
    """
    l = s.split(' ')
    result = []
    for elem in l:
        while elem[0] == '(': #adds parentheses that are in 1 element as separate elements
            result.append('(')
            elem = elem[1:]
        if ')' in elem: #samething for closed parentheses
            i = elem.find(')')
            result.append(elem[0:i])
            result+= [p for p in elem[i:]]
        else:
            result.append(elem)

    return result

def parse(tokens):
    """
    Converts an ordered list of elements into an algebraic expression
    """
    binops ={'+': Add, '-': Sub, '*': Mul, '/': Div}
    def parse_expression(index):
        thing= tokens[index]
        if thing.isdigit() or ('-' in thing and len(thing) !=1):
            return (Num(int(thing)), index+1)
        
        if thing.isalpha():
            return (Var(thing), index+1)
        if thing is '(': #recursively parses expressions with operations (operations are always bound by parentheses)
            left, next_index  = parse_expression(index+1)
            while tokens[next_index] == ')':
                next_index +=1
            operation = binops[tokens[next_index]]
            right, end = parse_expression(next_index+1)
            return operation(left, right), end
    parsed_expression, _ = parse_expression(0)
    return parsed_expression

def sym(s):
    """
    Converts string into algebraic expression
    """
    tokens = tokenize(s)
    return parse(tokens)


class Symbol:

    def __add__(self, other):
        return Add(self, other)
    def __radd__(self, other):
        return Add(other, self)
    def __sub__(self, other):
        return Sub(self, other)
    def __rsub__(self, other):
        return Sub(other, self)
    def __mul__(self, other):
        return Mul(self, other)
    def __rmul__(self, other):
        return Mul(other, self)
    def __truediv__(self, other):
        return Div(self, other)
    def __rtruediv__(self, other):

        return Div(other, self)
    


        



class BinOp(Symbol):
    def __init__(self, left, right):

        self.left = left
        self.right = right
        if isinstance(left, str):
            self.left = Var(left)
        if isinstance(left, int):
            self.left = Num(left)
        if isinstance(right, str):
            self.right = Var(right)
        if isinstance(right, int):
            self.right = Num(right)


    def __str__(self):
        rightstring = str(self.right)
        leftstring = str(self.left)
        modified = 0
        if self.left.precedence < self.precedence:
            leftstring = '(' +str(self.left)+')'

        if self.right.precedence < self.precedence:
            rightstring = '('+str(self.right)+')'
            modified = 1
        
        if modified == 0:
            if self.noncommutative and self.precedence == self.right.precedence:
                rightstring = '('+str(self.right)+')'

        if self.left.precedence == 0:
            leftstring = str(self.left)
        if self.right.precedence ==0:
            rightstring = str(self.right)


        return leftstring + ' ' + self.symbol + ' ' + rightstring

    def eval(self, mapping):
        """
        Solves left and right
        """
        left = self.left.eval(mapping)
        right= self.right.eval(mapping)

        symbols = {'+': lambda x,y : x+y, '-':lambda x,y : x-y, '*' : lambda x,y : x*y, '/': lambda x,y : x/y,} #inheritable method that allows every function to be defined.
        #a new binop would require its function to be implemented here
        return symbols[self.symbol](left, right)      
class Add(BinOp):
    def __init__(self, left, right):
        BinOp.__init__(self, left, right)
        self.precedence = 1
        self.noncommutative = False
        self.symbol = '+'

    
    def __repr__(self):
        return 'Add(' + repr(self.left) + ', ' + repr(self.right) + ')'

    def deriv(self, x):
        """
        Differentiates the expression with respect to variable x(not literally x duh)
        """

        return (self.left.deriv(x) + self.right.deriv(x))
    
    def simplify(self):
        """
        Reduces the expression based on given rules
        """
        left = self.left.simplify()
        right = self.right.simplify()

        if isinstance (left, Num) and isinstance(right, Num):
            return Num(left.n + right.n)
        if isinstance(left, Num) and left.n == 0:
            return right
        if isinstance(right, Num) and right.n == 0:
            return left

        return left + right

class Sub(BinOp):
    def __init__(self, left, right):
        BinOp.__init__(self, left, right)
        self.precedence = 1
        self.noncommutative = True
        self.symbol = '-'

    def __repr__(self):
        return 'Sub(' + repr(self.left) + ', ' + repr(self.right) + ')'
    
    def deriv(self, x):
        """
        Differentiates the expression with respect to variable x(not literally x duh)
        """
        return(self.left.deriv(x) - self.right.deriv(x))

    def simplify(self):
        """
        Reduces the expression based on given rules
        """
        left = self.left.simplify()
        right = self.right.simplify()
        if isinstance (left, Num) and isinstance(right, Num):
            return Num(left.n - right.n)
 
        if isinstance(right, Num) and right.n == 0:
            return left

        return left - right
class Mul(BinOp):
    def __init__(self, left, right):
        BinOp.__init__(self, left, right)
        self.precedence = 2
        self.noncommutative = False
        self.symbol = '*'

    def __repr__(self):
        return 'Mul(' + repr(self.left) + ', ' + repr(self.right) + ')'

    def deriv(self, x):
        """
        Differentiates the expression with respect to variable x(not literally x duh)
        """
        return(self.left * self.right.deriv(x) + self.right*self.left.deriv(x))

    def simplify(self):
        """
        Reduces the expression based on given rules
        """
        left = self.left.simplify()
        right = self.right.simplify()

        if isinstance (left, Num) and isinstance(right, Num):
            return Num(left.n * right.n)
        
        if isinstance (left, Num) and left.n == 1:
            return right
        if isinstance (right, Num) and right.n == 1:
            return left
        if isinstance (left, Num) and left.n == 0:
            return Num(0)
        if isinstance (right, Num) and right.n == 0:
            return Num(0)
        return left * right
class Div(BinOp):
    def __init__(self, left, right):
        BinOp.__init__(self, left, right)
        self.precedence = 2
        self.noncommutative = True
        self.symbol ='/'


    def __repr__(self):
        return 'Div(' + repr(self.left) + ', ' + repr(self.right) + ')'

    def deriv(self, x):
        """
        Differentiates the expression with respect to variable x(not literally x duh)
        """
        return (self.right *(self.left.deriv(x)) - self.left*self.right.deriv(x))/(self.right * self.right)

    def simplify(self):
        """
        Reduces the expression based on given rules
        """
        left = self.left.simplify()
        right = self.right.simplify()

        if isinstance (left, Num) and isinstance(right, Num):
            return Num(left.n / right.n)

        if isinstance (right, Num) and right.n == 1:
            return left

        if isinstance (left, Num) and left.n == 0:
            return Num(0)

        return left/right


class Var(Symbol):
    def __init__(self, n):
        """
        Initializer.  Store an instance variable called `name`, containing the
        value passed in to the initializer.
        """
        self.name = n
        self.precedence = 0
        self.noncommutative = False


    def __str__(self):
        return self.name

    def __repr__(self):
        return 'Var(' + repr(self.name) + ')'
    
    def deriv(self, x):
        if str(self) == x:
            return Num(1)
        else:
            return Num(0)

    def simplify(self):
        return self

    def eval(self, mapping):
        """
        returns its value
        """
        return mapping[self.name]
class Num(Symbol):
    def __init__(self, n):
        """
        Initializer.  Store an instance variable called `n`, containing the
        value passed in to the initializer.
        """
        Symbol.__init__(self)
        self.n = n
        self.precedence = 0
        self.noncommutative = False

    def __str__(self):
        return str(self.n)

    def __repr__(self):
        return 'Num(' + repr(self.n) + ')'

    def deriv(self, x):
        return Num(0)
    
    def simplify(self):
        return self
    def eval(self, mapping):
        """
        returns its value
        """
        return self.n
if __name__ == '__main__':
    s= ''
    while s!= 'QUIT':
        s = input(str)
        if s == 'QUIT':
            pass
        
        else:
            try:
                print(repr(sym(s)))
            except:
                print('Bomboclaat bredda that cyah work enuh')