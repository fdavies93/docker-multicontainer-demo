import os
import time

print 

env = [os.environ.get('DATA_PATH'), os.environ.get('WAIT_TIME'), os.environ.get("WRITE_TIMES")]

it = 0

for e in env:
    if e == None:
        print ("Exit due to env variables being unset.")
        exit(0)

while (True):

    data_path = env[0]
    wait_time = float(env[1])
    write_times = int(env[2])

    with open(data_path, "a") as f:
        write_str = str(it) + "\n"
        f.write(write_str)
        print(write_str, end="")

    it += 1

    if it > write_times:
        break

    time.sleep(wait_time)