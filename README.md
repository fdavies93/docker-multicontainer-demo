# Multi-Container Demo

This project demonstrates concepts for working with multiple containers in Docker using simple Python apps.

## Building and Running

You can build by simply entering into the subfolders reader and writer and running `docker build . -t reader`.

**Running writer**
`sudo docker run -dit -e DATA_PATH="log.txt" -e WAIT_TIME=10 -e WRITE_TIMES=1000 writer`

**Running reader**
`tbc`