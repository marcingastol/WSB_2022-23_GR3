Feature: Healthy food

Scenario: eating
    Given there were <start> cucumbers
    When I eat <eat> cucumbers
    Then I should have <left> cucumbers

Examples:
    | start | eat   | left |
    | 5     | 2     | 3     |
    | 3     | 3     | 0     |
    | 0     | 0     | 0     |