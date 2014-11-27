from behave import *


def addition(a, b):
    return a + b

@given(u'I have entered {value_a} into the calculator')
def step_impl(context, value_a):
    context.a = value_a


@given(u'I added another {value_b} into the calculator')
def step_impl(context, value_b):
    context.b = value_b

@when(u'I press add')
def step_impl(context):
    pass

@then(u'the results should be {value_results} on the screen')
def step_impl(context, value_results):
    assert addition(context.a, context.b), value_results
