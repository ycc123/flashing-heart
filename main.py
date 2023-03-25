def on_forever():
    basic.show_leds("""
        . # . # .
                # . # . #
                # . . . #
                . # . # .
                . . # . .
    """)
    basic.show_leds("""
        . . . . .
                . # . # .
                . # # # .
                . . # . .
                . . . . .
    """)
    basic.show_string("Hello!")
    basic.show_string("OK no problem")
basic.forever(on_forever)
