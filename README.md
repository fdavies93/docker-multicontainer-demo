# Multi-Container Demo

This project demonstrates concepts for working with multiple containers in Docker using simple Python apps.

## Building and Running

You can build by simply entering into the subfolders reader and writer and running `docker build . -t reader`.

**Creating a shared volume**
```sudo docker volume create demo```

**Running writer**
```sudo docker run -dit -e DATA_PATH="data/log.txt" -e WAIT_TIME=10 -e WRITE_TIMES=1000 writer```

```sudo docker run -dit -v demo:/data -e DATA_PATH="data/log.txt" -e WAIT_TIME=10 -e WRITE_TIMES=1000 writer```

**Running reader**
```sudo docker run -dit -v demo:/data -e DATA_PATH="data/log.txt" -e WAIT_TIME=5 reader```