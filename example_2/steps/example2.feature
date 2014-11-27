Feature: Addition
  In order to avoid silly mistakes
  As a math dimwit
  I want to be told the sum of two numbers

Scenario Outline: Add two numbers
  Given I have entered <value_a> into the calculator
  And I added another <value_b> into the calculator
  When I press add
  Then the results should be <value_c> on the screen

  Examples: Calculator Values
    | value_a | value_b | value_c |
    | 10      | 20      | 30      |
    | -10     | 20      | 10      |
    | 10      | -20     | 10      |
    | -10     | -30     | -40     |
