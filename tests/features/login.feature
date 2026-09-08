Feature: Customer login

  As a customer,
  I want to successfully log in to the Saucedemo platform
  So that I can access my account

  @smoke @regression
  Scenario: Customer successfully logs in to Saucedemo
    Given The customer is at the login page
    When The customer fills in his email and password
    And The customer clicks on the Log In button
    Then The customer can see the products page
    