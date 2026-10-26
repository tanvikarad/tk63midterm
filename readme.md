Project Setup and Usage guide: 
Install and Configure Git


Download and install from (https://git-scm.com/download/win).  
Accept the default options during installation.

verify the version of git and connect to github using ssh

Generate a new SSH key:
ssh-keygen -t ed25519 -C "your_email@example.com"

Start the SSH agent:
eval "$(ssh-agent -s)"

Add the SSH private key to the agent:
ssh-add ~/.ssh/id_ed25519

Copy your SSH public key:
cat ~/.ssh/id_ed25519.pub | clip

Add the key to your GitHub account
    Go to [GitHub SSH Settings](https://github.com/settings/keys)
    Click **New SSH Key**, paste the key, save.

Test the connection:
ssh -T git@github.com

You should see a success message.


Clone the Repository

Now you can safely clone the course project:
git clone <repository-url>
cd <repository-directory>


Install Python 3.10+

Download and install (https://www.python.org/downloads/).  

python --version



Create and Activate a Virtual Environment (Optional but recommended)
python3 -m venv venv
source venv/bin/activate   

Install Required Packages
pip install -r requirements.txt

Running the Project
python3 main.py

this will give you a propm that tells you to type a command. Type help to get the list of all commands. 
if you want to add 4 + 4, you would type add and hit ENTER. It will ask you for the first number, type the first number for the operation (in this case it is 4), and hit Enter. It will ask you for number 2 (again 4 in this case), and hit ENTER.
It will display the answer!
This format is used for every arithmatic operation available in this calculator. 
You can additionally type history and hit ENTER to see your calculation history. 
If you would like to undo an operation (to remove it from the hisroty) type UNDO and hit ENTER. This can be reversed with redo.
If you would like to save the history, you can write save and hit ENTER. 
If you would like to clear the history, type clear and hit ENTER. 
To load history, type load and hit ENTER. 
once you are done using the application, type exit to close it. 



Adding the .env varibles:
Create a .env file in the root of the project. Once created, you can add the following variables and set the values to what you desire them to be:
CALCULATOR_LOG_DIR=./logs
CALCULATOR_HISTORY_DIR=./history
CALCULATOR_MAX_HISTORY_SIZE=1000 (change the number to one you desire to be the max history size)
CALCULATOR_AUTO_SAVE=true (you can set this to true or false depending on what you want)
CALCULATOR_PRECISION=10 (change the number for the decimal places)
CALCULATOR_MAX_INPUT_VALUE=1e999 (maximum digits for input, change it to be your desired value)
CALCULATOR_DEFAULT_ENCODING=utf-8 




to-do: 
Project Description: Overview of the calculator application and its features.

Testing Instructions: How to run unit tests and check test coverage.

CI/CD Information: Overview of GitHub Actions workflow and its purpose.

