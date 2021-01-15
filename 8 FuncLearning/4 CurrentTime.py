import datetime

def currentTime():
    now = datetime.datetime.now()
    return (now.hour, now.minute, now.second)

h, m, s = currentTime()
print("now time is :{}:{}:{}".format(h, m, s))