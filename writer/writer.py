import os
import time

def load_env(names):
    env_dict = { "unset": [] }
    for nm in names:
        env = os.environ.get(nm)
        
        if env == None:
            env_dict['unset'].append(nm)
            continue

        env_dict[nm] = env
    return env_dict

env = load_env(["DATA_PATH", "WAIT_TIME", "WRITE_TIMES"])

it = 0

if len(env["unset"]) > 0:
    print ("Exit due to env variables being unset.")
    exit(0)

while (True):

    data_path = env["DATA_PATH"]
    wait_time = float(env["WAIT_TIME"])
    write_times = int(env["WRITE_TIMES"])

    with open(data_path, "a") as f:
        write_str = str(it) + "\n"
        f.write(write_str)
        print(write_str, end="")

    it += 1

    if it > write_times:
        break

    time.sleep(wait_time)