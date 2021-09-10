# autoping

Simple python 2.7 ping script for linux

This script reads `ping.list` file line by line and ping hosts specified this lines. 
One line - one hostname (or IP) or comment (starts with ';' or '#')

## ping.list format

```
# it is comment
; it is comment too

# IP:
10.0.0.50
# hostname:
 google.com

# this format NOT supported. Sсript will try to ping "google.com # wrong, comment must be in separate line"
google.com # wrong, comment must be in separate line
```

## ping.list location

By default script use `/etc/autoping/ping.list`. If it not exist script it will try to open ping.list in directory that contains autoping.py file

## instal and use systemd

Skript support systemd service and timer.

1. Install:
```
$ sudo ./install.sh
```

2. Start auto ping service:
```
$ sudo ./start.sh
```

3. View jourlal of service:
```
$ sudo ./journal.sh
```

4. Stop service:
```
$ sudo ./stop.sh
```




