# tekken_data_scraper
# Python 3.12.2, I guess
# Windows OS only

import time, re
import vgamepad as vg

# init gamepad
gamepad = vg.VX360Gamepad()

# map tekken inputs to long ass vgamepad codes
CODE_TABLE = {
    1: vg.XUSB_BUTTON.XUSB_GAMEPAD_X,
    2: vg.XUSB_BUTTON.XUSB_GAMEPAD_Y,
    3: vg.XUSB_BUTTON.XUSB_GAMEPAD_A,
    4: vg.XUSB_BUTTON.XUSB_GAMEPAD_B,
    "u": vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP,
    "d": vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN,
    "f": vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT,
    "b": vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT,
}


# primary function for sending gamepad inputs
def send(inputs, duration=0.0167):
    for input in inputs:
        gamepad.press_button(button=CODE_TABLE[input])
    gamepad.update()
    time.sleep(duration)
    for input in inputs:
        gamepad.release_button(button=CODE_TABLE[input])
    gamepad.update()


# parse tekken notation as regex and return as list for send() func
def parse_input(notation):
    segments = notation.split(",")

    list_of_inputs = []

    # Look for Tekken inputs
    pattern = re.compile(r"([udbf]+|\d)")

    for segment in segments:
        matches = pattern.findall(segment.strip())

        output = []

        for match in matches:
            if match.isalpha():
                output.extend(list(match))
            else:
                output.append(int(match))

        list_of_inputs.append(output)

    return list_of_inputs


# Wait so game can connect to virtual gamepad
# time.sleep(3)


while True:
    # I hate single quotes my formatter is dumb as fuck
    notation = input('Enter Tekken notation, or "q" to quit:\n')

    if notation == "q":
        print("Exiting data scraper")
        break
    else:
        print(parse_input(notation))
