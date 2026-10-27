# PROJECT OVERVIEW: 

to-do: 

Project Description: Overview of the calculator application and its features.






## Project Setup and Usage guide: 
### Install and Configure Git

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

### Running the Project
python3 main.py

this will give you a propm that tells you to type a command. Type help to get the list of all commands. 

if you want to add 4 + 4, you would type add and hit ENTER. It will ask you for the first number, type the first number for the operation (in this case it is 4), and hit Enter. It will ask you for number 2 (again 4 in this case), and hit ENTER.

It will display the answer!

This format is used for every arithmetic operation available in this calculator.
Available operations include add, subtract, multiply, divide, modulus, int_division, power, root, absolute difference and percents. 

Add adds two numbers. 

Subtract: subtracts the second number from the first number

Multipy: Multiplies two numbers

Divide: Divides two numbers

Power: calculates the nth power of a number

Root: calculates the nth root of a number

Modulus: returns the remainder from the division of two numbers

Int_division: returns the quotient rounded toward zero.

Percent: calculates the percentage based on the two provided numbers

Absolute difference: calculates the different between two absloute values

History: Saves the calcultions and displays them 

Load: loads the saved history from past session 

Undo: removes the last operation from the history

Redo: add the removed last operation back to the history

Save: saves the operations done in that session 

Clear: clears the history of operations done in the session

Help: displays the commands that can be used to perform operations 

Exit: closes the calculator


### Adding the .env varibles:
Create a .env file in the root of the project. Once created, you can add the following variables and set the values to what you desire them to be:

CALCULATOR_LOG_DIR=./logs

CALCULATOR_HISTORY_DIR=./history

CALCULATOR_MAX_HISTORY_SIZE=1000 (change the number to one you desire to be the max history size)

CALCULATOR_AUTO_SAVE=true (you can set this to true or false depending on what you want)

CALCULATOR_PRECISION=10 (change the number for the decimal places)

CALCULATOR_MAX_INPUT_VALUE=1e999 (maximum digits for input, change it to be your desired value)

CALCULATOR_DEFAULT_ENCODING=utf-8 




### Testing and CI/CD informtaion

There are unit tests in the tests folder. 

In order to run the tests, you can open the terminal and type pytest and hit ENTER. 

That will show you the number of tests that were run and their success rate. 

There will be a final percentage that shows total test coverage. 

In order to run the automated tests, you simply have to push the code to a repository on Github. 

There is a GitHub folder that contains the script to run GitHub Actions on push. 

What that does is that it runs the pytest automatically everytime you push new code to the repository. 

You can change the coverage percentage in the tests.yml file. what that will do is, it will set the new number as the threshold. As long as you have enough successful tests to reach that number, GitHub Actions will mark that test as successful. 

