Feature: Addition
   In order to avoid silly mistakes
   As a math dimwit
   I want to be told the sum of two numbers

Scenario: Add two numbers
   Given I have entered 50 into the calculator
   And I added another 70 into the calculator
   When I press add
   Then the results should be 120 on the screen
