Feature: eBay tests HW-1

  Scenario: Add tv to the cart
    Given open eBay.com
    Then search for "Sony XR77A80J" TV
    And click the "search" button
    And click first available item from results list
    And click "Add to the cart"
    And click "Go to cart"


  Scenario: Daily deals to cart
    Given open eBay.com
    And click Daily Deals
    And click SPOTLIGHT DEAL
    And click "Add to the cart"
    And click "Go to cart"

#  Scenario: Add item to the cart from category
#    Given open eBay.com
#    Then choose shop category "cameras & photo"
#    And choose category "camera drones"
#    And choose "DJI camera drones"
#    And choose model "DJI Mavic 2 Pro"
#    Then choose first deal from the list
#    And click "Add to the cart"