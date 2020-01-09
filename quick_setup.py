# Created by MysteryBlokHed on 09/01/2020.
import subprocess
import sys
from subprocess import CalledProcessError

requirements = ["requests"]

try:
    subprocess.check_call([sys.executable, "-m", "pip", "install", *requirements])
    print("**********************")
    print("Quick Setup Complete.")
    print("**********************")
except CalledProcessError:
    print("Something went wrong with the install.")
except OSError:
    print("You do not have permission to do this.")
    print("Are you running quick_setup.py as an admin?")
    print("")