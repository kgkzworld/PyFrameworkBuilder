"""
.DESCRIPTION
    This library is used to display a message with a timestamp. The message can be an alert, warning, or error.

.NOTES
    [Original Author]
        o Michael Arroyo
    [Original Build Version]
        o 1.0.0.20240822 (Major.Minor.Patch.Date<YYYYMMDD>)
    [Latest Author]
        o Michael Arroyo
    [Latest Build Version]
        o 1.1.0.20250102 (Major.Minor.Patch.Date<YYYYMMDD>)
    [Comments]
        o
    [Python Compatibility / Tested On]
        o Python 3.10.14
    [Forked Project]
        o

.DEPENDENCIES
    o rich # The rich module provides a way to print colored text
    o time # The time module provides various time-related functions

.BUILD NOTES
    o 1.0.0.20240822
        [Michael Arroyo] Initial Build
    o 2.0.0.20241217
        [Michael Arroyo] Change the function name to timestamp
        [Michael Arroyo] Add time lib
        [Michael Arroyo] Add a file logging option
    o 1.1.0.20250102
        [Michael Arroyo] Add rich print for colored text
        [Michael Arroyo] Remove datetime import

.EXAMPLES
    Command: timestamp('This is a warning message for X', 'warning')
    Description: This will display a Warning message with a timestamp.
    Notes:
    Output: [!] 2024-08-22 10:18:35: This is a warning message for X

    Command: timestamp('This is a warning message for X', 'warning', 'logs/app.log')
    Description: The timestamp message will also be appended to the logs/app.log file
    Notes:
    Output: [!] 2024-08-22 10:18:35: This is a warning message for X
"""

from rich import print # The rich module provides a way to print colored text
from time import gmtime, strftime # The time module provides various time-related functions

def timestamp(message, message_type='alert', logfile=None):
    message_types = ['alert', 'warning', 'error']
    if message_type not in message_types:
        raise ValueError("Invalid message type. Expected one of: %s" % message_types)
    if message_type == 'alert':
        current_message = "[+] %s: %s" % (strftime("%Y-%m-%d %H:%M:%S %z"), message)
    if message_type == 'warning':
        current_message = "[!] %s: %s" % (strftime("%Y-%m-%d %H:%M:%S %z"), message)
    if message_type == 'error':
        current_message = "[-] %s: %s" % (strftime("%Y-%m-%d %H:%M:%S %z"), message)

    print(current_message)
    if not logfile is None:
        f = open(logfile, "a")
        f.write(f"{current_message}\n")
        f.close()