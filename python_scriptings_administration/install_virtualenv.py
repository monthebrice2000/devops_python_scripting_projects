
# 1. First check whether pip is installed or not. We are going to install pip for python3
sudo apt install python3-pip

# 2. Install the virtual environment using pip3
sudo pip3 install virtualenv

# 3. Now we will create the virtual environment. You can give it any name; I have called it pythonenv:
virtualenv pythonenv

# 4. Activate your virtual environment:
source venv/bin/activate

# 5. After your work is done, you can deactivate virtualenv by using following command:
deactivate
