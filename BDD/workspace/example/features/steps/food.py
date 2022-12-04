#pip install behave

from behave import given, when, then, step
import cucumbers #import pliku cucumber.py

@given("there were {start:d} cucumbers")
def step_cucumber(context, start):
    context.amount_of_cucumbers = start

@when("I eat {eat:d} cucumbers")
def step_eating(context, eat):
    context.amount_of_cucumbers = \
    cucumbers.eat(context.amount_of_cucumbers, eat)

@then("I should have {left:d} cucumbers")
def step_after(context, left):
    assert context.amount_of_cucumbers == left