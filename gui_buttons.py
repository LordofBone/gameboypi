import RPi.GPIO as GPIO
import time
import uinput

GPIO.setmode(GPIO.BCM)

GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)


device = uinput.Device([
        uinput.BTN_LEFT,
        uinput.BTN_RIGHT,
        uinput.REL_X,
        uinput.REL_Y,
		uinput.KEY_W,
		uinput.KEY_S,
        ])

try:
	while True:
		input_down = GPIO.input(27)
		input_a = GPIO.input(22)
		input_b = GPIO.input(23)
		input_right = GPIO.input(24)
		input_left = GPIO.input(17)
		input_start = GPIO.input(5)
		input_up = GPIO.input(6)
		input_select = GPIO.input(12)

		if input_up == False:
			#print('Up Button Pressed')
			device.emit(uinput.REL_Y, -15)
			time.sleep(0.2)
			
		if input_down == False:
			#print('Down Button Pressed')
			device.emit(uinput.REL_Y, 15)
			time.sleep(0.2)
			
		if input_left == False:
			#print('Left Button Pressed')
			device.emit(uinput.REL_X, -15)
			time.sleep(0.2)
			
		if input_right == False:
			#print('Right Button Pressed')
			device.emit(uinput.REL_X, 15)
			time.sleep(0.2)
			
		if input_start == False:
			#print('Start Button Pressed')
			device.emit(uinput.KEY_W)
			time.sleep(0.2)
			
		if input_select == False:
			#print('Select Button Pressed')
			device.emit(uinput.KEY_S)
			time.sleep(0.2)
			
		if input_a == False:
			#print('A Button Pressed')
			device.emit_click(uinput.BTN_RIGHT)
			time.sleep(0.2)
			
		if input_b == False:
			#print('B Button Pressed')
			device.emit_click(uinput.BTN_LEFT)
			time.sleep(0.2)

finally:  
    GPIO.cleanup()
