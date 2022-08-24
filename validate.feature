Feature: Validate searched results

  # For some reason when I run all tests in regular mode I have browser exception
  # "Too many redirections..."
  # Then I switch to incognito mode and continue execute tests without exceptions
  Background:
    Given Set regular or incognito mode for browser: regular

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

  Scenario: Find Rammstein tickets in LA and validate result
    Given Open a home page on the eBay website
    Then Type "Rammstein" in the search string
    And Choose in dropdown list "Tickets & Experiences"
    And Click search button
    Then Apply filters to results
      | category | filter |
      | Category | Concert Tickets |
    Then Apply filters to results
      | category | filter |
      | Venue City | Los Angeles |
    And Validate that items in the result list matched to filters
      | filters |
      | Rammstein |
      | Los Angeles |

  Scenario: Advanced search Rammstein tickets in LA
    Given Open a home page on the eBay website
    Then Click "Advanced search" link
    And Verify "Advanced search" page was opened
    Then Type "Rammstein concert Los Angeles" in the search string
    And Choose parameters on the page
      | parameter             |
      | Title and description |
      | Buy It Now            |
    And Click search button
    And Validate that items in the result list matched to filters
      | filters |
      | Rammstein |
      | Los Angeles |


