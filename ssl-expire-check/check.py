#!/usr/bin/env python3

import socket
import ssl
import sys
from datetime import datetime

def ssl_expiry_datetime(hostname):
    ssl_date_fmt = r'%b %d %H:%M:%S %Y %Z'
    sslcontext = ssl.create_default_context()
    conn = sslcontext.wrap_socket(socket.socket(socket.AF_INET), server_hostname=hostname)
    conn.settimeout(5.0)
    try:
        conn.connect((hostname,443))
    except Exception as e:
        print(e)
    else:
        ssl_info = conn.getpeercert()
        return datetime.strptime(ssl_info['notAfter'], ssl_date_fmt)

if __name__ == '__main__':
    if(len(sys.argv) != 2):
        print('Usage: %s <hostname>' % sys.argv[0])
        sys.exit(1)
    hostname = sys.argv[1]
    cur_date = datetime.today().replace(microsecond=0)
    exp_date = ssl_expiry_datetime(hostname)
    print('Current date and time: %s' % cur_date)
    print('Expiry date and time: %s' % exp_date)
    days_to_expire = int((exp_date - cur_date).days)
    print('Days until expire: %d' % days_to_expire)
    
