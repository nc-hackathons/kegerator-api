# Kegerator

# Setup the API

1. Install Python/Pip:

    **Raspbian**:

        sudo apt-get install python-pip && sudo apt-get install python-dev

    **Mac**:
    
        brew install python

2. Install MySQL:

  **Raspbian**:

        sudo apt-get install mysql-server mysql-client libmysqlclient-dev

  **Mac**:
        brew install mysql
3. Install `virtualenv` and `virtualenvwrapper`:

        pip install virtualenv && pip install virtualenvwrapper
        
  Add `sudo` to the two installs only if it fails.
    
In your `~/.bash_profile`, add:
    
    source "/usr/local/bin/virtualenvwrapper.sh"

Then,

    source ~/.bash_profile
    mkvirtualenv nc
    workon nc

    pip install -r requirements.txt

    mysql -u root -p

    CREATE DATABASE kegerator;
    CREATE USER 'nc'@'localhost' IDENTIFIED BY 'kegerator1234';
    GRANT ALL PRIVILEGES ON kegerator . * TO 'nc'@'localhost';

    python app.py

To add some sample data in your database, run `python create_data.py`.

Note: Every time you work on this project, you need to enter the `nc` environment by running `workon nc`.

Disclaimer: I used `nc` as the name of my virtual environment to set up Python packages, but you can use whatever name you choose.