import time

def count_down(tick_tock):

    while tick_tock:
        mins, secs = divmod(tick_tock, 60)
        timer = f"{mins}:{secs}"

        print(timer, end='\r')
        time.sleep(1)
        tick_tock -=1

    print("Alarm!")

tick_tock = input("Enter a time in seconds:\n")

count_down(int(tick_tock))
