Feature: Add a product to cart

  As a customer,
  I want to add a product to my cart
  So that I can then see it in my cart

  @smoke @regression
  Scenario: Customer successfully adds a product to the cart
    Given A customer is logged on the Saucedemo platform
    And The customer is on the products page
    When The customer adds "Sauce Labs Backpack" to the cart
    And The customer clicks on the cart button
    Then The customer can see the product previously selected
    