Feature: Test menus

  Scenario: Test left menu for "scott bike"
    Given open eBay.com website
    Then type "scott bike" to search string and click search button
    And choose "Bike Type" and "Hybrid Bike" in left menu
    And choose "Color" and "Black" in left menu
    And choose "Condition" and "New" in left menu
    Then verify item is "Hybrid"
    And verify item is "Black"
    And verify item is "New"

  Scenario: Test "Applied filters" for "scott bike"
    Given open eBay.com website
    Then type "scott bike" to search string and click search button
    And choose "Bike Type" and "Road Bike" in left menu
    And choose "Condition" and "New" in left menu
    Then verify filter is applied "Road Bike"
    And verify filter is applied "New"

  Scenario: Test left menu for "go pro 10 black"
    Given open eBay.com website
    Then type "go pro 10 black" to search string and click search button
    And choose "Brand" and "GoPro" in left menu
    And choose "Model" and "GoPro HERO10 Black" in left menu
    And choose "Condition" and "New" in left menu
    Then verify item is "HERO10"
    And verify item is "Black"
    And verify item is "New"

  Scenario: Test "Applied filters" for "go pro 10 black"
    Given open eBay.com website
    Then type "go pro 10 black" to search string and click search button
    And choose "Model" and "GoPro HERO10 Black" in left menu
    And choose "Condition" and "New" in left menu
    Then verify filter is applied "GoPro HERO10 Black"
    And verify filter is applied "New"

  Scenario: Test left menu for "go pro 10 black" with price
    Given open eBay.com website
    Then type "go pro 10 black" to search string and click search button
    And choose "Model" and "GoPro HERO10 Black" in left menu
    And choose "Condition" and "New" in left menu
    And choose with category "Price" from 400 to 500
    Then verify item is "HERO10"
    And verify item is "Black"
    And verify item is "New"
    And verify price between 400 and 500
    And verify filter is applied "$400.00 to $500.00"