# Introduction

These are instructions for installing Keras Gemma support on windows using these methods:
* Via WSL Ubuntu
* Via Docker for Windows

At this point, we've done minimal testing so YMMV :)

# WSL Ubuntu

* Install Ubuntu Linux via WSL:
  * There are various instructions and youtube videos, I recommend following the one that looks reasonable for your version of Windows.
  * Here's what I did:
    * opened a windows powershell prompt
    * typed the following:
    ```
    $ wsl.exe --install -d Ubuntu
    ```
    * I waited a minute or so and noticed it was hanging on a "waiting" message, so I hit Ctl-C and it continued the installation asking for a new Linux username and password
    * I entered my preferred Linux username and password (recorded it for later use) and it dropped me into a Linux console
    * At the Linux console, I immediately updated the Ubuntu packages like so: 
    ```
    $ sudo apt-get update
    ```
    * I then went back into Windows and disabled all the Windows BitDefender firewall profiles
    * Then I rebooted the machine
    * After reboot, I opened an Ubuntu console using the new Ubuntu option in the Windows start menu
* Download and install Anaconda for Linux (not Windows):
  * I downloaded and ran this version: Anaconda3-2024.06-1-Linux-x86_64.sh Anaconda3-2024.06-1-Linux-x86_64.sh
    * Note that I moved that file from the download location in Windows to the Linux file system
    * I also changed the permissions adding the "x" chmod attribute so that I could execute it
    * The installation will take a long time (like 30 mins for me)
  * After installation verify your conda installation and version by running the following at the Linux command line:
    ```
    $ conda --version
    conda 24.5.0
    ```
  * If the above didn't work, you might need to log out of your Linux console and log back in, or just run another "bash" shell
  * Create a custom conda environment for python 3.9 like so:
    ```
    conda create -n <custom_name> python=3.9
    ```
  * Activate the custom conda environment you just created
  * Clone the "kagglex_gemma" github repository and check-out the branch "gw/initial"
  * Install the packages in the requirements.txt file like so:
    ```
    $ python -m pip install -r requirements.txt
  * Test everything via the test.ipynb notebook located in this directory

# Docker For Windows

TBD
