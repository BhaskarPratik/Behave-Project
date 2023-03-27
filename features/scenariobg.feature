Feature:OrangeHrm Login
  Background:common steps
    Given I launch Browser
    When I open application
    And Enter valid username and password
    And Click on login button

  Scenario:Login to the HRM application
    Then User must login to the dashboard page

  Scenario:Search user
    When navigate to search page
    Then Search page should be display


  Scenario:Advance user search
    When navigate to advance search page
    Then advanced search page should display