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

  Scenario: Test flying out menu "Shop by category"
    Given Open URL "ebay.com"
    Then Click flying out menu "Shop by category" and verify correct page was opened
        | Category      | Subcategory                              | Page title                                |
        | Motors        | Parts & accessories                      | Auto Parts & Accessories                  |
        | Motors        | Cars & trucks                            | Cars & Trucks                             |
        | Motors        | Motorcycles                              | Motorcycles                               |
        | Motors        | Other vehicles                           | Other Vehicles & Trailers                 |
        | Electronics   | Computers, Tablets & Network Hardware    | Computers, Tablets & Network Hardware     |
        | Electronics   | Cell Phones, Smart Watches & Accessories | Cell Phones, Smart Watches & Accessories  |
        | Electronics   | Video Games & Consoles                   | Video & PC Gaming                         |
        | Electronics   | Cameras & Photo                          | Cameras & Photo                           |
        | Home & garden | Yard, Garden & Outdoor Living Items      | Yard, Garden & Outdoor                    |
        | Home & garden | Tools & Workshop Equipment               | Tools & Workshop Equipment                |
        | Home & garden | Home Improvement                         | Home Improvement                          |
        | Home & garden | Kitchen, Dining & Bar Supplies           | Kitchen, Dining & Bar Supplies            |