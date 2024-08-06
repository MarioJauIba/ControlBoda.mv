# Wedding control
Wedding control is a simple wedding managing app with support for a simple landing webpage and digital invitation and guest management capabilities.

## Environment setup
### Prerequisites
* python 3.9+
    * `sudo apt-get install python3.10` 
* python venv
    * `sudo apt-get install python3.10-venv`
* git
    * `sudo apt-get install git`
* [redis](https://redis.io/docs/getting-started/installation/install-redis-on-linux/)

### Quick setup
* Clone this repo
* Navigate to the main project's folder `wedding_control`
* Create a python virtual environment using `python3 -m venv .`
* Activate the python virtual environment using `source bin/activate`
* Install required packages using pip `pip install -r requirements.txt`

### Start development server
* Within an activated python virtual environment run `flask run`