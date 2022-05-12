import time

def greeting():
    t = time.localtime()
    current_time = time.strftime("%H", t)

    if int(current_time) >= 0 and int(current_time) < 12:
        greet_day_condition = "Good Morning"
    elif int(current_time) >= 12 and int(current_time) < 16:
        greet_day_condition = "Good Afternoon"
    else:
        greet_day_condition = "Good Evening"

    return(greet_day_condition)

if __name__ == '__main__':
    spoken = greeting()
    print(spoken)