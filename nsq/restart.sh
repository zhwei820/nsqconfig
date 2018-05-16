kill -9 $(ps -ef|grep nsq|grep -v grep| awk '{print $2}')


nohup bin/nsqlookupd -config config/nsqlookupd.cfg &

nohup bin/nsqd -config config/nsqd.cfg &

nohup bin/nsqadmin -config config/nsqadmin.cfg &
