Feature: Validate searched results

  Scenario: Find list of items and validate that match to search
    Given Open a home page on the eBay website
    Then Type "360 action camera" in the search string
    And Click search button
    Then Apply filters to results
      | category | filter         |
      | Brand    | Insta360       |
      | Model    | Insta360 ONE X |
    And Validate that items in the result list matched to filters
      | filters |
      | Insta360 |
      | ONE X    |
      | Camera   |
