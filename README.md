# Multi-Container Demo

This project demonstrates concepts for working with multiple containers in Docker using simple Python apps.

## Building and Running

You can build by simply entering into the subfolders reader and writer and running `docker build . -t reader`.

**Creating a shared volume**
```sudo docker volume create demo```

**Running writer**
```sudo docker run -ditP -v demo:/data -e DATA_PATH="data/log.txt" ```

**Running reader**

Non-detached.
```sudo docker run -it -v demo:/data -e DATA_PATH="data/log.txt" -e WAIT_TIME=5 reader```