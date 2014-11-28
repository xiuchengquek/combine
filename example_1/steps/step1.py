from behave import *

def addition(a, b):
	return a + b


@given(u'I have entered 50 into the calculator')
def step_impl(context):
    pass
@given(u'I added another 70 into the calculator')
def step_impl(context):
    pass

@when(u'I press add')
def step_impl(context):
    pass

@then(u'the results should be 120 on the screen')
def step_impl(context):
    assert addition(50, 70) == 120
