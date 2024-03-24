import RPi.GPIO as GPIO

def check_sensor(hallpin):
    if GPIO.input(hallpin) == False:
        return 1

    return 0

num_of_rows = 8
num_of_cols = 8

base_board = [[0] * 8 for _ in range(8)]

pin_mapping = {
    "col1" : 0,
    "col2" : 0,
    "col3" : 0,
    "col4" : 0,
    "col5" : 0,
    "col6" : 0,
    "col7" : 0,
    "col8" : 0
}

decode_a = 0
decode_b = 0
decode_c = 0

if __name__ == '__main__':
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    # hall effect column array pins
    GPIO.setup(pin_mapping["col1"], GPIO.IN)
    GPIO.setup(pin_mapping["col2"], GPIO.IN)
    GPIO.setup(pin_mapping["col3"], GPIO.IN)
    GPIO.setup(pin_mapping["col4"], GPIO.IN)
    GPIO.setup(pin_mapping["col5"], GPIO.IN)
    GPIO.setup(pin_mapping["col6"], GPIO.IN)
    GPIO.setup(pin_mapping["col7"], GPIO.IN)
    GPIO.setup(pin_mapping["col8"], GPIO.IN)

    # decoder select pins
    GPIO.setup(decode_a, GPIO.OUT)
    GPIO.setup(decode_b, GPIO.OUT)
    GPIO.setup(decode_c, GPIO.OUT)

    # LED select pin
    GPIO.setup(0, GPIO.OUT)

    while (True):
        for i in range(num_of_rows):
            binary_form = format(i, '03b')
            c, b, a = map(int, binary_form)
            
            GPIO.output(decode_a, a)
            GPIO.output(decode_b, b)
            GPIO.output(decode_c, c)
            
            for key in pin_mapping:
                base_board[i][list(pin_mapping.keys()).index(key)] = check_sensor(pin_mapping[key])

        print("Chess base board: ")
        print(base_board)
