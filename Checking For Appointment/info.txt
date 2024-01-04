AUTO MAIL FOR FREE APPOINTMENT:

You can use the code it to be auto informed with Email when there is an available appointment in Bürger Service or anywhere else.

It is an example of this website: https://www.service.bremen.de/dienstleistungen/personalausweis-beantragen-8363

But it can be changed and adjusted according to your own wish. 


HOW TO RUN: 

For Mac:

1.Open Terminal 
2.Write following commands line by line
"crontab -e" 
"*/5 * * * * /path/to/python /path/to/appointment.py"
"0 15 * * * /usr/bin/killall -q python"

For Windows:

Open Task Scheduler, create a new task, and set up a trigger to run the task every 1 minute. In the Actions tab, set the program/script to the path of your Python interpreter (python.exe) and add the arguments as the full path to your script (\path\to\scheduler.py). Make sure to adjust the paths according to your system.
