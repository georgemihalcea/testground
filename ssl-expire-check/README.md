# ssl-expire-check

## Python - Check ssl certificate expiration date and number of days until expiration date

Sample usage:

    ./check.py <hostname>

If the ssl certificate was installed on a different port (other than 443), the check script can be used like this:

    ./check.py <hostname>:<port>

To automate for a list of hosts, create a file with the name "hosts" in the same folder with the script "check.py" and execute the included bash script "check.sh".
Sample hosts file:

    server1.example.net
    server2.example.net:8080

The script "check.sh" will parse all the lines in the "hosts" file and will launch the "check.py" script with the parameters read from the "hosts" file.
