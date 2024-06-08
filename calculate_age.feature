


Feature: Calculate Age

  Scenario: Calculate age for a valid date
    Given I enter the birthdate "1990-05-15"
    When I calculate the age
    Then I should get result "11554"

  Scenario: Calculate age for an invalid date format
    Given I enter the birthdate "15-05-1990"
    When I calculate the age
    Then I should get result "Invalid date format. Please enter the date in the format YYYY-MM-DD."

  Scenario: Calculate age for a future date
    Given I enter the birthdate "2040-01-01"
    When I calculate the age
    Then I should get result "Birthdate cannot be in the future."
