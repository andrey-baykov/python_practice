Feature: Validate searched results

# In this scenario page divider is present
  Scenario: Find list of items "360 action camera" and validate that match to search
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

# In this scenario page divider is NOT present
  Scenario: Find list of items "apple watch" and validate that match to search
    Given Open a home page on the eBay website
    Then Type "apple watch" in the search string
    And Click search button
    Then Apply filters to results
      | category     | filter               |
      | Series       | Apple Watch Series 7 |
      | Case Size    | 45 mm                |
      | Band Color   | Black                |
    And Validate that items in the result list matched to filters
      | filters              |
      | Apple Watch Series 7 |
      | 45                   |