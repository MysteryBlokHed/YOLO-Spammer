# YOLO Spammer
A tool that's fairly useless, only really designed to annoy people.  
**Note: It can be very easily stopped by blocking the anonymous spammer, and use will most likely get you banned from YOLO if the target reports you.**

One more thing to note: This guide (and some of the files) are targeted more towards people unfamiliar with programming, so some files (such as `quick_setup.py`) are just to make the process of running `__main__.py` easier.

## Run Online (Recommended for non-programmers)
If you don't have access to a device that has Python, you can use online Python interpreters to run the code, and it'll work just fine. [Repl.it](https://repl.it/languages/python3) is one that worked in my testing. Just copy+paste [the source code](https://raw.githubusercontent.com/MysteryBlokHed/yolo-spammer/master/__main__.py) and paste it into the window on the left, then press the Run button at the top.

## Quickstart
Go to the [releases page](https://github.com/MysteryBlokHed/yolo-spammer/releases) and download `YOLOSpammer.exe` to quickly run YOLO Spammer.  
**You will still need to download [Python v3.6+](https://www.python.org/downloads/).**

## Requirements
- [**Python v3.6+**](https://www.python.org/downloads/)
- **requests** Python module  
  Get it by running `pip install requests` or `python -m pip install requests`.  
  **If you are unfamiliar with using the command line, there is an easier way to install the module.**

### Automate module install (Windows)
Right-click the `quick_setup.bat` file and select `Run as administrator` from the menu.  

# How to use
## The required values
**THREAD COUNT (argv run only)**  
How many spam threads to run (Default: 50).  
**COOKIE**  
A cookie is submitted with the POST request. This can really be whatever you want.  
**YOLO ID**  
What appears after `/m/` in the YOLO url and before the `?w=`.  
Example: If the URL is `http://onyolo.com/m/2DmxFx7a2d?w=Honest%20opinions%3F`, the ID would be `2DmxFx7a2d`.  
**QUESTION TO MIMIC**  
When someone posts a YOLO, a question must be supplied. However, this question can be set in the POST request, so you can set it to whatever you want to simulate them asking.  
**MESSAGE(S) TO SPAM**  
Fairly self-explanatory; the message to spam the YOLO with. To have multiple, separate the messages with pipes `|`.  
**ADD INTERVAL**  
Whether or not to add a counter to the messages to show how many times it's been spammed (Example: `MESSAGE CONTENT 1`, `MESSAGE CONTENT 2`, etc.)

## Running `__main__.py` with no arguments
When you run `__main__.py` with no arguments, it will ask you for the values listed above (Other than the thread count).

## Running `__main__.py` with arguments
The command should be formatted as such when running with arguments (without the angle brackets):  
`python __main__.py <THREAD COUNT> <COOKIE> <YOLO ID> <QUESTION TO MIMIC> <MESSAGE(S) TO SPAM> <ADD INTERVAL>`  
`QUESTION TO MIMIC` and `MESSAGE TO SPAM` should have double quotes around them (`"`) if they have spaces. If you want to have multiple messages to spam, separate them (in the quotes) with a pipe `|`.  
`THREAD COUNT` should just be an integer.  
`ADD INTERVAL` should be `y` or `n`.

After either run method, you will see what the message sent was. If the POST result code is not `200`, it will be logged.
