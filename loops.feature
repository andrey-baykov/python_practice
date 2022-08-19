Feature: Loops and tables

  Scenario: Test top menu items variable
    Given Open URL "ebay.com"
    Then Click "Deals" on the top menu
    And Verify page "Deals" was opened

  Scenario: Test top menu items with table of variants
    Given Open URL "ebay.com"
    Then Click menu item from a table on the top menu and verify opened page
        | Menu items      | Page title        |
        | Daily Deals     | Deals             |
        | Brand Outlet    | The Brand Outlet  |

