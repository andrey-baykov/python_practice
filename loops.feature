Feature: Loops and tables, raw text

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

    Scenario: Find sport watch throw menus and validate that
    Given Open URL "ebay.com"
    Then Click flying out menu "Shop by category" and verify correct page was opened
      | Category         | Subcategory     | Page title                  |
      | Sporting goods   | Sporting goods  | Sporting Goods & Equipment  |
    And Click item "Fitness, Running & Yoga" in mosaic menu
    And Verify page "Fitness, Running & Yoga" was opened
    And Click item "Fitness Technology" in mosaic menu
    And Verify page "Fitness Gadgets" was opened
    Then Click item "GPS & Running Watches" in carousel menu
    And Verify page "GPS & Running Watches" was opened
    Then Validate item with parameters from the table
      | Apply | Parameters           | Value      |
      | Yes   | Description contains | Watch      |
      | Yes   | Price higher then    | 85        |
      | Yes   | Price between        | 80 120     |

  Scenario: Find GoPro camera by filter and verify percent of items correct
    Given Open URL "ebay.com"
    Then Input "Gopro hero 10 black" in the search field
    And Click search button
    And Validate correct items with words in the title more than 50%
      | Parameter       |
      | GoPro Hero      |
      | 10              |
      | Camera          |
      | Black           |

  Scenario: Find Garmin watch by filter and verify percent of items correct
    Given Open URL "ebay.com"
    Then Input "Garmin watch" in the search field
    And Click search button
    And Validate correct items with words in the title more than 80%
      | Parameter       |
      | Garmin          |
      | watch           |
      | GPS             |

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

  Scenario: Verify selling FAQ - test 1
    Given Open URL "ebay.com/sl/sell"
    Then Open FAQ element "What’s the best way to ship my item?"
    And Verify that element "What’s the best way to ship my item?" contains text
    """
    eBay provides recommendations, but you can choose a preferred shipping carrier.
    Can’t make it to your local dropoff? Some offer free “ship from home” pickup.
    Print your shipping labels with eBay to receive a discount from the carriers we work with.
    If you don’t have a printer, we also offer QR codes for eBay labels.
    """

  Scenario: Verify selling FAQ - test 2
    Given Open URL "ebay.com/sl/sell"
    Then Open FAQ element "What can I sell on eBay?"
    And Verify that element "What can I sell on eBay?" contains text
    """
    You can sell almost anything, from homemade goods to used or unused items from your closet.
    We restrict items that violate any laws, or infringe on intellectual property.
    """

  Scenario: Verify selling FAQ - test 3
    Given Open URL "ebay.com/sl/sell"
    Then Open FAQ element "Do I have to pay federal income tax on my sales?"
    And Verify that element "Do I have to pay federal income tax on my sales?" contains text
    """
    Starting on Jan 1, 2022, IRS regulations require all businesses that process payments,
    including online marketplaces like eBay, to issue a Form 1099-K for all sellers who receive
    $600 or more in sales. The new tax reporting requirement may impact your 2022 tax return
    that you may file in 2023. However, just because you receive a 1099-K doesn’t automatically
    mean that you’ll owe taxes on the amount reported on your 1099-K. Only goods that are sold
    for a profit are considered taxable, so you won’t owe any taxes on something you sell
    for less than what you paid for it. For example, if you bought a bike for $1,000 last
    year, and then sold it on eBay today for $700, that $700 you made would generally not be
    subject to income tax. Check out our 1099-K FAQ to learn more about these changes.
    """