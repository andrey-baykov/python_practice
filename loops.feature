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

  Scenario: Find items by filter and verify percent of items correct
    Given Open URL "ebay.com"
        Then Input "Gopro hero 10 black" in the search field
    And Click search button
    And Validate correct items with words in the title more than 50%
      | Parameter       |
      | GoPro Hero      |
      | 10              |
      | Camera          |
      | Black           |

  Scenario: Find item throw search with parameters in the left menu and validate that by %
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
      | New                 |
    And Validate correct items with words in the title more than 50%
      | Parameter       |
      | DJI             |
      | Mavic Pro       |

  Scenario Outline: Test top menu items with examples
    Given Open URL "ebay.com"
    Then Click "<menu_items>" on the top menu
    And Verify page "<page_title>" was opened
    Examples:
      | menu_items      | page_title        |
      | Daily Deals     | Deals             |
      | Brand Outlet    | The Brand Outlet  |

  Scenario Outline: Find item and validate that by %
    Given Open URL "ebay.com"
    Then Input "<search_item>" in the search field
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
      | New                 |
    And Validate correct items with words in the title more than <percentage>%
      | Parameter       |
      | DJI             |
      | Mavic Pro       |
    Examples:
      | search_item | percentage |
      | DJI         | 50         |
      | DJI         | 40         |
      | DJI Mavic   | 50         |

  Scenario Outline: Find items and verify percent of items correct
    Given Open URL "ebay.com"
        Then Input "<search_item>" in the search field
    And Click search button
    And Validate correct items with words in the title more than <percentage>%
      | Parameter       |
      | GoPro Hero      |
      | 10              |
      | Camera          |
      | Black           |
    Examples:
      | search_item         | percentage |
      | GoPro               | 50         |
      | GoPro Hero          | 40         |
      | GoPro Hero 10       | 50         |