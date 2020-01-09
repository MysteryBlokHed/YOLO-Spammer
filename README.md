# YOLO Spammer
A tool that's fairly useless, only really designed to annoy people.  
**Note: It can be very easily stopped by blocking the anonymous spammer, and use will most likely get you banned from YOLO if the target reports you.**

## Requirements
- [**Python v3.6+**](https://www.python.org/downloads/)
- **requests** Python module  
  Get it by running `pip install requests` or `python -m pip install requests`.

# How to use
## The required values
**THREAD COUNT (argv run only)**  
How many spam threads to run (Default: 50).  
**COOKIE**  
A cookie is submitted with the POST request. This can really be whatever you want.  
**YOLO ID**  
What appears after `/m/` in the YOLO url and before the `?w=`.  
**QUESTION TO MIMIC**  
When someone posts a YOLO, a question must be supplied. However, this question can be set in the POST request, so you can set it to whatever you want to simulate them asking.  
**MESSAGE TO SPAM**  
Fairly self-explanatory; the message to spam the YOLO with.  
**ADD INTERVAL**  
Whether or not to add a counter to the messages to show how many times it's been spammed (Example: `MESSAGE CONTENT 1`, `MESSAGE CONTENT 2`, etc.)

## Running `__main__.py` with no arguments
When you run `__main__.py` with no arguments, it will ask you for the values listed above (Other than the thread count).

## Running `__main__.py` with arguments
The command should be formatted as such when running with arguments (without the angle brackets):  
`python __main__.py <THREAD COUNT> <COOKIE> <YOLO ID> <QUESTION TO MIMIC> <MESSAGE TO SPAM> <ADD INTERVAL>`  
`QUESTION TO MIMIC` and `MESSAGE TO SPAM` should have double quotes around them (`"`) if they have spaces.  
`THREAD COUNT` should just be an integer.  
`ADD INTERVAL` should be `y` or `n`.

After either run method, you will see output of each message spammed, and the POST status code.  
The result status code should be **`200`**.