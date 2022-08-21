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

  Scenario: Find item throw search with parameters in the left menu and validate that
    Given Open URL "ebay.com"
    Then Input "DJI" in the search field
    And Click search button
    And Apply left menu with filters from the table
      | Filter menu | Filter              |
      | Brand       | DJI                 |
      | Model       | DJI Mavic Pro       |
      | Type        | Ready to Fly Drone  |
      | Condition   | New                 |
    And Validate filters was applied and shows above result table
      | Filter              |
      | DJI                 |
      | DJI Mavic Pro       |
      | Ready to Fly Drone  |
      | New                 |
    Then Validate item with parameters from the table
      | Apply | Parameters           | Value    |
      | Yes   | Description contains | Drone    |
      | Yes   | Shipping             | Free     |
      | Yes   | Returns              | Free     |
      | No    | Price lower then     | 400      |
      | No    | Price higher then    | 30       |
      | Yes   | Price between        | 30 400   |

  Scenario: Find item throw menus and validate that
    Given Open URL "ebay.com"
    Then Click flying out menu "Shop by category" and verify correct page was opened
        | Category      | Subcategory      | Page title       |
        | Electronics   | Cameras & Photo  | Cameras & Photo  |
    And Click item "Digital Cameras" in mosaic menu
    And Verify page "Digital Cameras" was opened
    Then Click item "Hasselblad" in carousel menu
    And Verify page "Hasselblad Photo Digital Cameras" was opened
    Then Validate item with parameters from the table
      | Apply | Parameters           | Value      |
      | Yes   | Description contains | Hasselblad |
      | Yes   | Price higher then    | 1500     |
      | Yes   | Price between        | 1800 2000   |