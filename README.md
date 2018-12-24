# weewx-freezer
Simple data service based on Weewx Pond
I wanted to read the Temperature of my freezer while I was gone for long periods of time.

1st step was to add a RPI with a Temp sensor where my freezer is located.

The I follow the instructions from the "add a sensor" page over a the WeeWX wiki

These are instructions for adding data from a single sensor.
How to do it

Save the sensor data to a file, say /home/pi/sesnsordata/Freezer.txt.  Mine is an smb share on the Weewx computer that the Pi has access to

Add a service that parses the file, that is what this is.  For my .deb install it is in /usr/share/weewx/user 

If you use observation names that are not in the database schema, you must extend the database schema for these to be recorded. See the WeeWX customization guide for details.
