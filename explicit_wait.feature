Feature: Check results on item page

  Scenario: Search item and validate results on 4th pages
    Given Open https://www.ebay.com website
    Then Search Michelin tires tires
    And Apply filters
      | Category      | Filter        |
      | Rim Diameter  | 20            |
      | Section Width | 265           |
      | Aspect Ratio  | 45            |
      | Condition     | New           |
      | Quantity      | 4             |
    Then Validate all listing results by parameters
      | parameter             |
      | Michelin              |
      | 265/45R20             |
    And Validate all results on each result page
      | param          | value         |
      | Condition:     | New           |
      | Brand:         | Michelin      |
      | Rim Diameter:  | 20            |
      | Section Width: | 265           |
      | Aspect Ratio:  | 45            |
      | Quantity:      | 4             |
    Then Print tests results