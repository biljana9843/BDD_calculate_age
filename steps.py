
# steps.py

from behave import given, when, then
from calculate_age import calculate_age_in_days
from datetime import datetime

@given('I enter the birthdate "{date}"')
def step_enter_birthdate(context, date):
    context.birthdate = date

@when('I calculate the age')
def step_calculate_age(context):
    context.result = calculate_age_in_days(context.birthdate, datetime(2022, 1, 1).date())
    print("Calculated age in days:", context.result)  # Dodaj ispis rezultata

@then('I should get result "{expected_result}"')
def step_verify_result(context, expected_result):
    print("Expected result:", expected_result)  # Dodaj ispis očekivanog rezultata
    print("Actual result:", context.result)  # Dodaj ispis stvarnog rezultata
    assert context.result == expected_result, f"Expected result '{expected_result}', but got '{context.result}'"

