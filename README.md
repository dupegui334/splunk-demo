# Splunk demo
In collaboration with David Lopez

## Random access and secure logs generator:
Used for uploading dummy data into our Splunk accounts and making a nice demo for the students.
access-log-generator.py was used for generating random web access logs, secure-log-generator.py was used for secure logs of our systems.
You can add more ips to the ips.txt file, the idea is that you have enough dummy logs to experiment with Splunk.

## HEC data sender:
This is used to generate some data for testing alerts. The data is sent via HEC simulating real-time events.