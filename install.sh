
cp autoping.py /usr/bin/autoping.py
mkdir -p /etc/autoping/
cp ping.list /etc/autoping/ping.list 

cp system/* /etc/systemd/system/

systemctl daemon-reload
