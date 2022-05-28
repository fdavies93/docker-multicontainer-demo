import os
import time

# refit to automatically send API request to "writer" triggering a write
# then grab the last line of log.csv (CSV) after wait
# writer should store API requests as a JSON string with timestamp and source (?)

def load_env(names):
    env_dict = { "unset": [] }
    for nm in names:
        env = os.environ.get(nm)
        
        if env == None:
            env_dict['unset'].append(nm)
            continue

        env_dict[nm] = env
    return env_dict

env = load_env(["DATA_PATH", "WAIT_TIME"])

if len(env["unset"]) > 0:
    print ("Exit due to env variables being unset.")
    exit(0)

while (True):
    data_path = env["DATA_PATH"]
    wait_time = float(env["WAIT_TIME"])
    print("Last line: ", end="")

    with open(data_path, "rb") as f:
        # get last line of file
        try: 
            f.seek(-2, os.SEEK_END)
            while f.read(1) != b'\n':
                f.seek(-2, os.SEEK_CUR)
        except OSError:
            f.seek(0)
        last_line = f.readline().decode()

    print(last_line, end="")
    time.sleep(wait_time)