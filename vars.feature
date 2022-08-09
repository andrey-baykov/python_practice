Feature: Variables

  Scenario: Verify motors page
    Given open eBay website
    And click "Shop by category" then choose category "Motors"
    Then verify page "eBay Motors" was opened

  Scenario: Verify cameras & photos page
    Given open eBay website
    And click "Shop by category" then choose category "Cameras & Photo"
    Then verify page "Cameras & Photo" was opened

  Scenario: Verify Golf Equipment page
    Given open eBay website
    And click "Shop by category" then choose category "Golf Equipment"
    Then verify page "Golf Equipment" was opened

  Scenario: Verify Restaurant & Food Service page
    Given open eBay website
    And click "Shop by category" then choose category "Restaurant & Food Service"
    Then verify page "Restaurant & Food Service" was opened