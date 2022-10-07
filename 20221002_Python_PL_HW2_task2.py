from MyTimer import MyTimer
import time

with MyTimer(units="m") as t:
    print("Hello world")
    time.sleep(6)
print(t.elapsed_time())

with MyTimer(units="s") as t:
    print("Hello world")
    time.sleep(6)
print(t.elapsed_time())

with MyTimer(units="h") as t:
    print("Hello world")
    time.sleep(6)
print(t.elapsed_time())

