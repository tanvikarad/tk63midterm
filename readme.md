Project Setup: 
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