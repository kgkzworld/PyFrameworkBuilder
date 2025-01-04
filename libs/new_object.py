"""
.DESCRIPTION
	This library will create a new object and return it

.NOTES
	[Original Author]
		o Michael Arroyo
	[Original Build Version]
		o 1.0.0.20250102 (Major.Minor.Patch.Date<YYYYMMDD>)
	[Latest Author]
		o Michael Arroyo
	[Latest Build Version]
		o 1.0.0.20250102 (Major.Minor.Patch.Date<YYYYMMDD>)
	[Comments]
		o
	[Python Compatibility / Tested On]
		o Python 3.13.1
	[Forked Project]
		o

.DEPENDENCIES
	o None

.BUILD NOTES
	o 1.0.0.20250102
		[Michael Arroyo] Initial Post

.EXAMPLES
	Command:    from new_object import new_object
                obj = new_object()
	Description: Create a new object and return it
	Notes: This is a simple function that will create a new object and return it
	Output: obj

"""

def new_object():
    """
    .DESCRIPTION
        This function will create a new object and return it

    .PARAMETERS
        None
    """
    obj = type('', (), {})()
    return obj