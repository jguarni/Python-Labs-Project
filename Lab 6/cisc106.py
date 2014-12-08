"""
CISC106 Module that includes some basic helper functions
such as assertEqual

Versions:
0.3
 + adjustment to support Python 3
 + InstanceType replaced by inspect.
0.21
 + improved performance of image animations
0.2
 + added auto repr functionality, can be used by extending Base
0.15
 + added to_repr function for better instance printing
0.13
 + added overlay function
0.12
 + display can be called multiple times
 + assertEqual supports PIL.Image.Image
0.1
 + Initial assertEqual, display, animate, bind
"""
__version__ = 0.21

import sys, traceback, types, os, inspect
import tkinter
#import numpy
#from PIL import Image, ImageTk

success = 0
fail = 0

def assertEqual(x, y, *args):
    """
    Checks an expected value using the isEqual function.
    Prints a message if the test case passed or failed.
    """
    
    trace = traceback.extract_stack()
    frame = trace[len(trace)-2]
    global success, fail
    
    if not isEqual(x, y, *args):
        fail += 1
        print("[%d tests: %d failed] line %d: failure for %s, received %s expected %s" \
            % (success + fail, fail, frame[1], frame[3],
               to_repr(x), to_repr(y)))
    else:
        success += 1
        print ("[%d tests: %d failed] line %d: success" \
            % (success + fail, fail, frame[1]))
    
def isEqual(x, y, *args):
    """
    isEqual : thing thing -> boolean
    isEqual : number number number -> boolean
    Determines whether the two arguments are equal, or in the case of
    floating point numbers, within a specified number of decimal points
    precision (by default, checks to with 4 decimal points for floating
    point numbers).
    
    Examples:
    >>> isEqual('ab', 'a'+'b')
     True
     
    >>> isEqual(12.34, 12.35)
     False
     
    >>> isEqual(12.3456, 12.34568, 4)
     True
         
    >>> isEqual(12.3456, 12.34568w5)
     False
    """
    if (x is None and y is not None) or (y is None and x is not None):
        return False
    elif x is None and y is None:
        return True
    elif type(x) == int and type(y) == int:
        return x == y
    elif type(x) == float or type(y) == float:
        if len(args) == 1:
            error = 10 ** (- args[0])
        else:
            error = 0.0001
        return abs(x - y) < error
    elif isseqtype(x) and isseqtype(y) and len(x)==len(y):
        res = True
        for (x1,y1) in zip(x, y):
            res = res and isEqual(x1, y1, *args)
        return res
   # elif isinstance(x, Image.Image) and isinstance(y, Image.Image):
   #     return list(x.data()) == list(y.data())
    elif type(x) == inspect.isclass(x):
        for f in vars(x):
            if not hasattr(y, f) or not isEqual(getattr(x, f),
                                                     getattr(y, f)):
                return False
        return True
    else:
        return x == y

def isseqtype(x):
    return type(x) == list or type(x) == tuple# or type(x) == numpy.ndarray

def print_verbose(obj):
    for f in dir(obj):
        print (f, "=", getattr(obj, f))

def to_repr(obj):
    if type(obj) == inspect.isclass(obj):
        attr_str = ""
        if getattr(obj, "__init__", None) is not None:
            attrs = [to_repr(getattr(obj, x)) for
                    x in obj.__init__.im_func.func_code.co_varnames[1:]]
            attr_str = ", ".join(attrs)
        return obj.__class__.__name__ + "(" + attr_str + ")"
    else:
        return repr(obj)
		
def resetSuccessFail():
	"""
	Resets the global counters success and fail.
	"""
	global success, fail
	success = 0
	fail = 0
	
def getSuccess():
	"""
	Returns the current success counter
	"""
	global success
	
	return success
	
def getFail():
	"""
	Returns the current fail counter
	"""
	global fail
	
	return fail


        

