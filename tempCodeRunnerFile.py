    if guess> computer_number:
            THRESOLD=guess-computer_number
            if THRESOLD > 5:
                print("Too high")
            else:
                print("High")
        if guess< computer_number:
            THRESOLD=computer_number-guess
            if THRESOLD < 5:
                print("Too low")
            else:
                print("Low")