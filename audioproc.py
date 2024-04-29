GPIO.output(3,False)
GPIO.output(4,False)

r = sr.Recognizer()
mic = sr.Microphone()

print("Listening...")

while True:
    try:
        with mic as source:
            audio = r.listen(source, 10, 3)
            
        words = r.recognize_google(audio).lower()

        if words == "red led":
            print("Toggle Red LED")
            GPIO.output(2,not GPIO.input(2))

        elif words == "orange led":
            print("Toggle Orange LED")
            GPIO.output(3,not GPIO.input(3))

        elif words == "green led":
            print("Toggle Green LED")
            GPIO.output(4,not GPIO.input(4))

        elif words == "all leds" or "all led":
            print("Toggle All LEDs")
            GPIO.output(2,not GPIO.input(2))
            GPIO.output(3,not GPIO.input(3))
            GPIO.output(4,not GPIO.input(4))
            
        elif words == "exit":
            print("...")
            sleep(1)
            print("Goodbye")
            break
        
        else:
            print("Heard: \'" + words + "\', Unknown command")
    except:
        print(".")





                                
