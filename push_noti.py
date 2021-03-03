from win10toast import ToastNotifier
import time


while True:
    current_time = time.strftime("%H:%M:%S")
    if current_time == "12:40:00":
        print(current_time)
        break
    else:
        pass


hr = ToastNotifier()
hr.show_toast('Alarm','hello u have to be stronger')