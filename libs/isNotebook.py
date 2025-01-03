"""
    .DESCRIPTION
        This library is used to detect if the session your running the code in is in a Jupyter Notebook or not.

    .NOTES
        [Original Author]
            o Michael Arroyo
        [Original Build Version]
            o 1.0.0.20241219 (Major.Minor.Patch.Date<YYYYMMDD>)
        [Latest Author]
            o Michael Arroyo
        [Latest Build Version]
            o 1.0.0.20241219 (Major.Minor.Patch.Date<YYYYMMDD>)
        [Comments]
            o
        [Python Compatibility / Tested On]
            o Python 3.10.14
        [Forked Project]
            o
        [Dependencies]
            o

	.Build Notes
		o 1.0.0.20241219 -
			[Michael Arroyo] Initial Build

    .EXAMPLE
        Command: print(is_notebook())
        Description: This will return True if the session is a Jupyter Notebook and False if it is not.
        Notes:
        Output: True
"""

def is_notebook() -> bool:
    try:
        shell = get_ipython().__class__.__name__
        if shell == 'ZMQInteractiveShell':
            return True   # Jupyter notebook or qtconsole
        elif shell == 'TerminalInteractiveShell':
            return False  # Terminal running IPython
        else:
            return False  # Other type (?)
    except NameError:
        return False      # Probably standard Python interpreter