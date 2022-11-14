from behave import *
import sys

#changed cwd to testible dir
sys.path.append("../../lab_python_oop")
from lab_python_oop.Rectangle import Rectangle
from lab_python_oop.Circle import Circle
from lab_python_oop.Square import Square

@given('rectangle with sides of "{first}" and "{second}", color is "{color}" and name is "{name}"')
def step_impl(context, first, second, name, color):
    global shape
    try:
        shape = Rectangle(int(first), int(second), name, color)
        return True
    except:
        return False

@given('circle with radius of "{radius}", color is "{color}" and name is "{name}"')
def step_impl(context, radius, name, color):
    global shape
    try:
        shape = Circle(int(radius), name, color)
        return True
    except:
        return False     

@given('square with side of "{side}", color is "{color}" and name is "{name}"')
def step_impl(context, side, name, color):
    global shape
    try:
        shape = Square(int(side), name, color)
        return True
    except:
        return False     

@when('we try to get properties')
def step_impl(context):
    if shape.area():
        if shape.get_name():
            if shape.color.value:
                return True
    return False

@then('we get area of "{area}", color is "{color}" and name is "{name}"')
def step_impl(context, area, color, name):
    if shape.area() == area:
        if shape.get_name() == name:
            if shape.color.value == color:
                return True
    return False