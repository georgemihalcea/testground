#!/usr/bin/env python3

import socket
import ssl
import sys
from datetime import datetime

def ssl_expiry_datetime(hostname, port=443):
    ssl_date_fmt = r'%b %d %H:%M:%S %Y %Z'
    sslcontext = ssl.create_default_context()
    conn = sslcontext.wrap_socket(socket.socket(socket.AF_INET), server_hostname=hostname)
    conn.settimeout(5.0)
    try:
        conn.connect((hostname,port))
    except Exception as e:
        # in case of error, just print the error message and continue
        print(e)
    else:
        ssl_info = conn.getpeercert()
        return datetime.strptime(ssl_info['notAfter'], ssl_date_fmt)

if __name__ == '__main__':
    if(len(sys.argv) != 2):
        print('Usage: %s <hostname>' % sys.argv[0])
        sys.exit(1)
    # check for port
    hostname = sys.argv[1].split(':')
    cur_date = datetime.today().replace(microsecond=0)
    if len(hostname) == 2:
        exp_date = ssl_expiry_datetime(hostname[0], int(hostname[1]))
    else:
        exp_date = ssl_expiry_datetime(hostname[0])
    print('Current date and time: %s' % cur_date)
    print('Expiry date and time: %s' % exp_date)
    days_to_expire = int((exp_date - cur_date).days)
    print('Days until expire: %d' % days_to_expire)
