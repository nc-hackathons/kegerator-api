# Kegerator Setup

Disclaimer: I used `nc` as the name of my virtual environment to set up Python packages, but you can use whatever name you choose.

    pip install virtualenv && pip install virtualenvwrapper
    
In your ~/.bash_profile, add:
    source "/usr/local/bin/virtualenvwrapper.sh"

Then,

    source ~/.bash_profile
    mkvirtualenv nc
    workon nc

    pip install -r requirements.txt

In mysql,

    CREATE USER 'nc'@'localhost' IDENTIFIED BY 'kegerator1234';
    GRANT ALL PRIVILEGES ON kegerator . * TO 'nc'@'localhost';

    python main.py

Note: Every time you work on this project, you need to enter the `nc` environment by running `workon nc`.