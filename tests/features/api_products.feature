Feature: Products API

  @api @regression
  Scenario: Get products successfully
    When The client requests the products endpoint
    Then The response status should be 200
    And The response should contain products