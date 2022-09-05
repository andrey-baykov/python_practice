Feature: Explicit wait

  Scenario: Search item and validate results on 4th pages
    Given Open ebay website
    Then Type "dell 27 monitor" in string and press search button
    And Apply filters from the tables
      | category | filter |
      | Display Type | LCD           |
      | Video Inputs | HDMI Standard |
    And Validate results on 4 pages
      | filters    |
      | LCD        |
      | New        |
