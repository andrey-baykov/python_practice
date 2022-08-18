Feature: Test with asserts

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

  Scenario:  Verify page in "Restaurant & Food Service"
    Given open eBay website
    Then click "Shop by category" and choose "Restaurant & Food Service"
    And verify page "Restaurant & Food Service" was opened

  Scenario:  Verify page in "Video Games & Consoles"
    Given open eBay website
    Then click "Shop by category" and choose "Video Games & Consoles"
    And verify page "Video & PC Gaming" was opened

  Scenario: Open "Refrigeration Equipment" with left menu
    Given open eBay website
    Then click "Shop by category" and choose "Restaurant & Food Service"
    And choose left menu "Refrigeration Equipment"
    And verify page "Commercial Refrigeration Equipment" was opened

  Scenario: Open "Refrigeration Equipment" with slide menu
    Given open eBay website
    Then click "Shop by category" and choose "Restaurant & Food Service"
    And choose block menu "Refrigeration & Ice Machines"
    And choose slide menu "Refrigeration Equipment Parts & Accessories"
    And verify page "Commercial Refrigeration Equipment Parts & Accessories" was opened

  Scenario: Verify "Colorforms Toys" page opened from top menu
    Given open eBay website
    Then choose in top menu "Toys"
    And open list of "Classic Toys"
    And choose left menu "Colorforms Toys"
    Then verify page "Colorforms Toys" was opened

  Scenario: Verify "Colorforms" item on opened page from top menu
    Given open eBay website
    Then choose in top menu "Toys"
    And open list of "Classic Toys"
    And choose left menu "Colorforms Toys"
    Then verify item is "Colorforms"

  Scenario: Verify "Chess" page opened from top menu
    Given open eBay website
    Then choose in top menu "Toys"
    And open list of "Games"
    And choose left menu "Chess Sets"
    Then verify page "Chess Sets" was opened

  Scenario: Verify "Chess" item on opened page from top menu
    Given open eBay website
    Then choose in top menu "Toys"
    And open list of "Games"
    And choose left menu "Chess Sets"
    Then verify item is "Chess"
    
  Scenario: Verify "Trains" page opened from top menu
    Given open eBay website
    Then choose in top menu "Toys"
    And choose block menu "Model Railroads & Trains"
    Then verify page "Model Trains" was opened

  Scenario: Verify "Train" item on opened page from top menu
    Given open eBay website
    Then choose in top menu "Toys"
    And choose block menu "Model Railroads & Trains"
    Then verify item is "Train"

  Scenario: Verify "Tabletop Games" page opened from top menu
    Given open eBay website
    Then choose in top menu "Toys"
    And choose block menu "Tabletop Games"
    Then verify page "Games" was opened

  Scenario: Verify "Game" item on opened page from top menu
    Given open eBay website
    Then choose in top menu "Toys"
    And choose block menu "Tabletop Games"
    Then verify item is "Game"

  Scenario: Verify "Board & Traditional Games" page opened from top menu
    Given open eBay website
    Then choose in top menu "Toys"
    And choose block menu "Tabletop Games"
    And quick top filter "Board & Traditional Games"
    Then verify page "Board & Traditional Games" was opened

  Scenario: Verify "Board Game" item on opened page from top menu
    Given open eBay website
    Then choose in top menu "Toys"
    And choose block menu "Tabletop Games"
    And quick top filter "Board & Traditional Games"
    Then verify item is "Board"

  Scenario: Verify item conteins text on opened page from top menu
    Given open eBay website
    Then choose in top menu "Toys"
    And choose block menu "Tabletop Games"
    And quick top filter "Board & Traditional Games"
    Then verify item contains text "Boards"

  Scenario: Verify book "Clean Code" by author "Robert C. Martin"
    Given open eBay website
    Then type "Clean code" to search string and click search button
    And verify item contains text "Clean Code"
    And verify item is "Robert C. Martin"

  Scenario: Verify book "Clean Code" price lower than $40
    Given open eBay website
    Then type "Clean code" to search string and click search button
    And verify item contains text "Clean Code"
    And verify item is "Robert C. Martin"
    And verify item price lower than 40

  Scenario: Verify book "Clean Code" price higher than $40
    Given open eBay website
    Then type "Clean code" to search string and click search button
    And verify item contains text "Clean Code"
    And verify item is "Robert C. Martin"
    And verify item price higher than 40

  Scenario: Verify book "Clean Code" price between $30 and $40
    Given open eBay website
    Then type "Clean code" to search string and click search button
    And verify item contains text "Clean Code"
    And verify item is "Robert C. Martin"
    And verify item price between 30 and 40

  Scenario: Verify book "Clean Code" has free shipping
    Given open eBay website
    Then type "Clean code" to search string and click search button
    And verify item contains text "Clean Code"
    And verify item is "Robert C. Martin"
    And verify item has "Free shipping"

  Scenario: Verify book "Clean Code" shipping less than $5
    Given open eBay website
    Then type "Clean code" to search string and click search button
    And verify item contains text "Clean Code"
    And verify item is "Robert C. Martin"
    And verify item shipping price lower than 5

  Scenario: Verify book "Clean Code" with free returns
    Given open eBay website
    Then type "Clean code" to search string and click search button
    And choose "Show only" and "Free Returns" in left menu
    And verify item has "Free returns"

  Scenario: Verify book "Clean Code" is brand new
    Given open eBay website
    Then type "Clean code" to search string and click search button
    And choose "Show only" and "Free Returns" in left menu
    And verify item condition is "Brand New"

  Scenario: Verify book "Clean Code" is sponsored
    Given open eBay website
    Then type "Clean code" to search string and click search button
    And verify item is "Robert C. Martin"
    And verify item is sponsored

  Scenario: Verify "Dysov v8" page
    Given open eBay website
    Then type "Dysov V8" to search string and click search button
    And verify item contains text "Dyson V8"

