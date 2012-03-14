#!/usr/bin/env python
#! This line is ignored, as is the previous line.

#! Set the title variable of the parser:
## title = "mylit example"

# <h1>A simple mylit example</h1>
# This is a simple example of literate <a
# href="http://www.python.org/">Python</a> programming with <a
# href="http://pypi.python.org/pypi/mylit">mylit</a>.

# Here we define a function that checks whether a given pair of coordinates
# lies within a circle of radius <code>r</code>.
def in_circle(x, y, r):
    # We first square both <code>x</code> and <code>y</code>, and sum them up.
    s = x ** 2 + y ** 2

    # <p>Note how the above comment contains HTML markup. The indentation of
    # the highlighted Python code is unaffected by interspersed comments.</p>

    # Here we check whether the coordinates (<code>x</code>, <code>y</code>)
    # lie within a circle of radius <code>r</code>.
    if s < r ** 2:
        # Everything's okay, so we can return <code>True</code>:
        return True
    else:
        # We may have a problem here. Better print a warning.
        import warnings
        warnings.warn("Danger, Will Robinson!")
        return False

# When this program is run from the command line, it performs a simple test.
if __name__ == "__main__":
    assert in_circle(3, 4, 5.1) == True
    assert in_circle(3, 4, 4.9) == False

