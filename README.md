# Restaurant Finder 
This program allows users to search for a restaurant based on their desired location and
food type by utilizing two seperate web APIs.

This project utilizes the following APIs:
* Google Geocode API
* Foursquare Places API

## How to Run
This application can be run from your local machine by following the steps
detailed below:

## Linux VM Installation
Setup can be performed via the steps below.

#### 1. Install VirtualBox
VirtualBox is the software that actually runs the virtual machine. You can
download it from virtualbox.org, [here](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1). Install the platform package for your operating system.

#### 2. Install Vagrant
Vagrant is the software that configures the VM and lets you share files
between your host computer and the VM's filesystem. Download and install
the version for your operating system [here.](https://www.vagrantup.com/downloads.html)

#### 3. Download the VM configuration
Download and unzip the following: [FSND-Virtual-Machine.zip.](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip)
Inside of this directory is another called vagrant. `cd` into vagrant and
enter the command, `vagrant up`, to download and install the Linux operating
system.

Once the installation concludes, run `vagrant ssh` to run the the newly
installed VM.


## Instructions to run this program:
Run the application with the following command:
* `python restaurantFinder.py`

The application is set by default to run at port 5000 from your local machine.
This may be altered by changing the designated port on _line 85_ of the `restaurantFinder.py` file.

In your browser navigate to the following; `http://localhost:5000`
