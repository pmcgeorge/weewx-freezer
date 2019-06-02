# weewx-freezer
Simple data service based on Weewx Pond

I wanted to read the Temperature of my freezer while I was gone for long periods of time.

1st step was to add an RPI with a Temp sensor where my freezer is located.  freezertemp.py is run every 5 minutes by a cron job and outputs a file named Freezer.txt with the current temperature say 6.4 to a file, say /home/pi/sesnsordata/Freezer.txt

sensordata is an smb share on the Weewx computer that the Pi has access to

Then I followed the instructions from the "add a sensor" page over a the WeeWX wiki and created freezer.py based on the pond example

To add a service that parses the file.  For my .deb install it is in /usr/share/weewx/user

I used extraTemp2 for the database location, you may need to change it. 

If you use observation names that are not in the database schema, you must extend the database schema for these to be recorded. See the WeeWX customization guide for details.
