# Portfolio Website Builder
This is a solo project to create a website builder to make a portfolio site using
Flask and SQLAlchemy libriaries. This uses the [Start Bootstrap]  (https://startbootstrap.com/)
free Bootstrap theme and using the [Freelancer] (https://startbootstrap.com/template-overviews/freelancer/)
templates.


# Installation to deploy on Amazon Web Services EC2 server

1. Go to AWS console and log in. If you do not have an account you can activate
it for a 12 month free tier account. If you are no longer on free tier don't worry.
This build setup is designed to keep costs low.

2. Navigate to EC2 pages

3. Click on Launch Instance.
    1. Choose an AMI > Ubuntu Server 16.04
    2. Chose and Instance Type > t2.micro
    3. Configure Instance >  Nothing here. Go to next page
    4. Add Storage > Uncheck Delete on Termination. This will allow you to have a backup incase you tereminate it.
    5. Tags > Set Name = >what you want to call the EC2 Instance. This is so you can recognize it.
    6. Create a Secruity Group > You want to have SSH (22), and HTTP (80). This is all you need open at this point.
    7. Click Launch. If you do not have a KeyPair made create a new one and make a name for it. It will download a file with the extention pem. It it should be found in your download directory.

4. At the dashboard for the EC2 instances click on Actions > Instance Settings > Change Termination Protection and set it to enable. This will protect it from accidental termination

5. While the instance is being set up you can start to configure things on your local machine

6. Go to the Terminal if on Mac/Linux or Git-Bash if on Windows:
    1. In your home directory type 'mkdir .ssh'
    2. Go to the directory the flie was downloaded to and type
        ```
        chmod 400 filename.pem
        mv filename.pem ~/.ssh
        ```
    3. Change directory to your home directory to add an alias to make things easy for you to connect to the server.

    4. Add this line to your .bashrc file:

        ```
        alias portfolio=ssh -i ~/.ssh/filename.pem ubuntu@public_ip'
        ```
    public_Ip is the ip address of your EC2 site.

    5. Check to see if the server is up and running. When it is connect to it with the alias your crated.

## Linux Ubuntu Configuration

To start setting up the Ubuntu Linux Server run:

```
sudo apt-get update && apt-get upgrade -y
sudo apt-get install apache2 postgresql python-pip python-dev build-essential git-all ntp python-psycopg2 libpq-dev libapache2-mod-wsgi python-virtualenv unattended-upgrades glances
sudo pip install --upgrade pip
```

This should get the apache server up and running, but now you need to start configuring it for the Python WSGI to run the Flask application.

After you have installed Apache, as per the instructions above, you need to get the latest version of python-wsgi. Once you get it installed, enable it.
```
sudo a2enmod wsgi
```
The directory that was created specifically by Apache is `/var/www` which is the directory that you will be working from. Change to that directory and install the repository,
```
cd /var/www
sudo git clone https://github.com/jpdesigns316/item-catalog.git item-catalog
```

After this you will need to set up some files so that the WSGI will be able to work. Copy the item-catalog file
to `/etc/apache2/sites-available`

```
sudo mv /var/www/item-catalog/item-catalog.conf /etc/apache2/sites-available
```
To enable it type
```
sudo a2ensite item-catalog
```
Restart the Apache server
```
sudo service apache2 restart
```
## Monitoring Apache Web server

Source: [How To Install, Configure, And Use Modules In The Apache Web Server] (https://www.digitalocean.com/community/tutorials/how-to-install-configure-and-use-modules-in-the-apache-web-server)

One of the most helpful and easiest modules to configure comes pre-installed and configured when you install Apache on Ubuntu. The mod_status module provides an overview of your server load and requests.

If mod_status is not already active you can type `sudo /usr/sbin/a2enmod status` to activate it.

Change the test in the '&lt;Locaiton /server-status&gt;' to look like this

```
<Location /server-status>
	SetHandler server-status
	Order deny,allow
	Deny from all
	Allow from 127.0.0.1 ::1
	Allow from Your.IP.Address.Here
</Location>
```


## Creating virtual environment
A virtual environment is important to create when running applications Python/Django. This is so you can create and environment that hold the dependencies for specific modules. One program could depend on one version of a file, whereas another could use a different version. Instead of pointing in multiple locations, just use a virtual environment. The following is how to set it up:

Source: [Hitchhiker's Guide to Python] (http://docs.python-guide.org/en/latest/dev/virtualenvs/)

If you do not currently have `venv` installed get it with the following:
```
sudo -H pip install virtualenv
```
If you already have it installed, change to the directory of the project that you wish to create the virtual environment for. For this project it is `/www/FlaskApp/src`, however it could be different depending on what you have created.
```
cd /www/item-catalog/src
sudo virutalenv venv
```
virtualenv syntax: `sudo virtualenv -p /usr/bin/python2.7 venv`
Now activate the newly created venv and install the modules you wish to use. After you have done so, exit the `venv`.
```
source venv/bin/activate
pip install -r requirements.txt
deactivate
```

MORE TO COME AS PROJECT GET COMPLETED
