Feature: Validate searched results in "incognito" mode of browser
  # For some reason when run all tests in regular mode browser have an exception
  # "Too many redirections..."
  # Then switch to incognito mode and execute tests without exceptions

  Background:
    Given Open a home page on the eBay website

# In this scenario page divider is present
  Scenario: Find list of items "360 action camera" and validate that match to search
    Then Type "360 action camera" in the search string
    And Click search button
    Then Apply filters to results
      | category | filter         |
      | Brand    | Insta360       |
      | Model    | Insta360 ONE X |
    And Validate that items in the result list matched to filters
      | filters  |
      | Insta360 |
      | ONE X    |
      | Camera   |

# In this scenario page divider is NOT present
  Scenario: Find list of items "apple watch" and validate with separate table filters
    Then Type "apple watch" in the search string
    And Click search button
    Then Apply filters to results
      | category   | filter               |
      | Series     | Apple Watch Series 7 |
      | Case Size  | 45 mm                |
      | Band Color | Black                |
    And Validate that items in the result list matched to filters
      | filters              |
      | Apple Watch Series 7 |
      | 45                   |

  # In this scenario page divider is NOT present
  Scenario: Find list of items "apple watch" and validate with applied filters
    Then Type "apple watch" in the search string
    And Click search button
    Then Apply filters to results
      | category   | filter               |
      | Series     | Apple Watch Series 7 |
      | Case Size  | 45 mm                |
      | Band Color | Black                |
    And Validate that items in the result list matched to filters


  Scenario: Find Rammstein tickets in LA and validate result
    Then Type "Rammstein" in the search string
    And Choose in dropdown list "Tickets & Experiences"
    And Click search button
    Then Apply filters to results
      | category | filter          |
      | Category | Concert Tickets |
      | Venue City | Los Angeles |
    And Validate that items in the result list matched to filters
      | filters     |
      | Rammstein   |
      | Los Angeles |

  Scenario: Advanced search Rammstein tickets in LA
    Then Click "Advanced search" link
    And Verify "Advanced search" page was opened
    Then Type "Rammstein concert Los Angeles" in the search string
    And Choose parameters on the page
      | parameter             |
      | Title and description |
      | Buy It Now            |
    And Click search button
    And Validate that items in the result list matched to filters
      | filters     |
      | Rammstein   |
      | Los Angeles |


