Feature: Testing lab_python_oop

    Scenario Outline: Testing properties of rectangle
        Given rectangle with sides of "<first>" and "<second>", color is "<color>" and name is "<name>"
        When we try to get properties
        Then we get area of "<area>", color is "<color>" and name is "<name>"

        Examples: Rectangle
            | first | second | name           | color | area  |
            | 9     | 4      | pryamougolnik  | blue  | 45    |
            | 5     | 1      | xXx_rect_xXx   | red   | 5     |
            | 99    | 98     | rEcTaNgLe      | yellow| 9702  |

    Scenario Outline: Testing properties of circle
        Given circle with radius of "<radius>", color is "<color>" and name is "<name>"
        When we try to get properties
        Then we get area of "<area>", color is "<color>" and name is "<name>"

        Examples: Circle
            | radius | name             | color | area               |
            | 1      | krug             | cyan  | 3.141592653589793  |
            | 12     | mega_krug        | gray  | 37.69911184307752  |
            | 200    | super ultra krug | black | 348.71678454846705 |

    Scenario Outline: Testing properties of circle
        Given square with side of "<side>", color is "<color>" and name is "<name>"
        When we try to get properties
        Then we get area of "<area>", color is "<color>" and name is "<name>"

        Examples: Square
            | side | name         | color | area  |
            | 1    | kvadrat      | lime  | 1     |
            | 12   | kvadratik    | pink  | 144   |
            | 200  | square shape | white | 40000 |