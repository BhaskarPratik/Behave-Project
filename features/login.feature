Feature:
  Scenario:Login to the orangeHrm with valid parameters
    Given  I launch chrome browser
    When I open orange HRM homepage
    And Enter username "Admin" and password "admin123"
    And Click on login button
    Then User must successfully login to the dashboard page

  Scenario Outline:
    Given  I launch chrome browser
    When I open orange HRM homepage
    And Enter username "<username>" and password "<password>"
    And Click on login button
    Then User must successfully login to the dashboard page

    Examples:
      |username| password|
      |Admin   | admin123|
      |admin123| admin   |
      |adminxyz| admin123|
      |admin   | adminxyz|
