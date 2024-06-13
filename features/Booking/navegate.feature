Feature: Navigate menu

Scenario Outline: Navigate between menu_option and validate the URL
      Given I navigate to the booking main page
      Then I should be in the "home" page
      When I click on the "<menu_option>" "<element_type>"
      Then The URL of the page should match the expected "<URL>"

    Examples:
      | menu_option         | element_type | URL                                  |
      | alojamiento         | button       | https://www.booking.com              |
      | vuelo               | button       | https://www.booking.com/flights      |
      | alquiler            | button       | https://www.booking.com/cars         |
      | atraccion           | button       | https://www.booking.com/attractions  |
      | taxis               | button       | https://www.booking.com/taxi         |