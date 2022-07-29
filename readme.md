I would suggest creating a service for your app, it's not as painful as you would think. This will start after the network is up so you don't need an intermediate script that adds delays. There are other parameters you can add to this file if you don't want to run as root user (the default), or you want to use virtualenv.

Create the following file /etc/systemd/system/my_project.service:

[Unit]
Description=My Project
After=network.target

[Service]
WorkingDirectory=/home/pi/project/
ExecStart=/usr/bin/python /home/pi/project/script.py
Restart=always

[Install]
WantedBy=multi-user.target
Then you can run:

sudo systemctl start my_project    
sudo systemctl status my_project
If bad, tweak and try:

sudo systemctl restart my_project
sudo systemctl status my_project
If Good:

sudo systemctl enable my_project
Reboot your pi and verify it all works.

Also double check any ports that you are using with other stuff running on the system.
