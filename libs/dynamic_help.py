"""
.DESCRIPTION
    This library is a wrapper for the pydoc module. It is used to parse and display the docstring of a Python module or function.

    The parsed sections include:
        - Description
        - Notes
        - Dependencies
        - Build Notes
        - Examples

    The docstring header should look like the following:

    <Note: The < - > in front of the main properties should be replaced with a single period in the actual docstring>
    *** < Do not include this line in the docstring >

    -DESCRIPTION
        This is a description of the module or function.

    -NOTES
        [Original Author]
            o <Author Name>
        [Original Build Version]
            o <Major>.<Minor>.<Patch>.<Date<YYYYMMDD>>
        [Latest Author]
            o <Author Name>
        [Latest Build Version]
            o <Major>.<Minor>.<Patch>.<Date<YYYYMMDD>>
        [Comments]
            o <Comments>
        [Python Compatibility / Tested On]
            o Python <Version>
        [Forked Project]
            o <Project Name>

    -DEPENDENCIES
        o <Dependency 1> # <Dependency 1 Description>
        o <Dependency 2> # <Dependency 2 Description>

    -BUILD NOTES
        o <Version 1>
            [<Author Name>] <Description>

        o <Version 2>
            [<Author Name>] <Description>

    -EXAMPLES
        Command: <Command>
        Description: <Description>
        Notes: <Notes>
        Output: <Output>

        Command: <Command>
        Description: <Description>
        Notes: <Notes>
        Output: <Output>
    *** < Do not include this line in the docstring >

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
    o argparse # The argparse module makes it easy to write user-friendly command-line interfaces
    o os # The os module provides a way to interact with the operating system
    o re # The re module provides support for regular expressions
    o subprocess # The subprocess module allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes
    o rich # The rich module provides a way to print colored text

.BUILD NOTES
    o 1.0.0.20250102
        [Michael Arroyo] Initial Build

.EXAMPLES
    Command: python .\\libs\\dynamic_help.py --version --module .\\libs\\dynamic_help.py
    Description: Show the latest build version for the module specified
    Notes:
    Output: 1.0.0.20250102

    Command: python .\\libs\\dynamic_help.py --module .\\libs\\dynamic_help.py
    Description: Parse and display the docstring Description field for the module specified
    Notes:
    Output:

    Command: python .\\libs\\dynamic_help.py --module .\\libs\\dynamic_help.py --dependencies
    Description: Parse and display the docstring Dependencies field for the module specified
    Notes:
    Output: o import argparse # The argparse module makes it easy to write user-friendly command-line interfaces
            o os # The os module provides a way to interact with the operating system
            ...

    Command: python .\\libs\\dynamic_help.py --module .\\libs\\dynamic_help.py --notes
    Description: Parse and display the docstring Notes field for the module specified
    Notes:
    Output: [Original Author]
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

    Command: python .\\libs\\dynamic_help.py --module .\\libs\\dynamic_help.py --build_notes
    Description: Parse and display the docstring Build Notes field for the module specified
    Notes:
    Output: o 1.0.0.20250102
                [Michael Arroyo] Initial Build
            ...

    Command: python .\\libs\\dynamic_help.py --module .\\libs\\dynamic_help.py --full_help
    Description: Parse and display the full docstring for the module specified
    Notes:
    Output: .DESCRIPTION
                This library is a wrapper for the pydoc module. It is used to parse and display the docstring of a Python module or function.
                ...
                .EXAMPLES
                    Command: python .\\libs\\dynamic_help.py --version --module .\\libs\\dynamic_help.py
                    Description: Show the latest build version for the module specified
                    Notes:
                    Output: 1.0.0.20250102
                *** < Do not include this line in the docstring >

    Command: python .\\libs\\dynamic_help.py --module .\\libs\\dynamic_help.py --examples
    Description: Parse and display the docstring Examples field for the module specified
    Notes:
    Output: Command: python .\\libs\\dynamic_help.py --version --module .\\libs\\dynamic_help.py
            Description: Show the latest build version for the module specified
            Notes:
            Output: 1.0.0.20250102
            ...

    Command: python .\\libs\\dynamic_help.py --module .\\libs\\dynamic_help.py --sample_docstring
    Description: Return a sample docstring to use as a template
    Notes:
    Output: '''
            .DESCRIPTION
                This is a description of the module or function.
            ...
            .EXAMPLES
                Command: <Command>
                Description: <Description>
                Notes: <Notes>
                Output: <Output>
            '''

    Command: python .\\libs\\dynamic_help.py --module .\\libs\\dynamic_help.py --return_only
    Description: Return the parsed sections only, do not print to console
    Notes:
    Output: ...
"""

import argparse # The argparse module makes it easy to write user-friendly command-line interfaces
import os # The os module provides a way to interact with the operating system
import re # The re module provides support for regular expressions
import subprocess # The subprocess module allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes

from rich import print # The rich module provides a way to print colored text

def parse_docstring(docstring):
    """
    This function is to parse the docstring and extract the identified sections

    The parsed sections include:
        - Description
        - Notes
        - Dependencies
        - Build Notes
        - Examples
    """
    # Updated regex patterns for newer docstring structure
    pattern_description = r"(?<=\.DESCRIPTION\n)(.*?)(?=\n\n\s*\.NOTES)"
    pattern_notes = r"(?<=\.NOTES\n)(.*?)(?=\n\n\s*\.DEPENDENCIES)"
    pattern_dependencies = r"(?<=\.DEPENDENCIES\n)(.*?)(?=\n\n\s*\.BUILD NOTES)"
    pattern_build_notes = r"(?<=\.BUILD NOTES\n)(.*?)(?=\n\n\s*\.EXAMPLES)"
    pattern_examples = r"(?<=\.EXAMPLES\n)(.*?)(?=\n\nFUNCTIONS)"

    # Extracting sections with fallback for missing matches
    description_match = re.search(pattern_description, docstring, re.DOTALL)
    notes_match = re.search(pattern_notes, docstring, re.DOTALL)
    dependencies_match = re.search(pattern_dependencies, docstring, re.DOTALL)
    build_notes_match = re.search(pattern_build_notes, docstring, re.DOTALL)
    examples_match = re.search(pattern_examples, docstring, re.DOTALL)

    # Safely extract and strip, or default to empty string
    description = description_match.group(1).strip() if description_match else ""
    notes = notes_match.group(1).strip() if notes_match else ""
    dependencies = dependencies_match.group(1).strip() if dependencies_match else ""
    build_notes = build_notes_match.group(1).strip() if build_notes_match else ""
    examples = examples_match.group(1).strip() if examples_match else ""

    # Organize into a dictionary for output
    parsed_sections = {
        "Description": description,
        "Notes": notes,
        "Dependencies": dependencies,
        "Build Notes": build_notes,
        "Examples": examples,
    }

    return parsed_sections

def extract_latest_build_version(text):
    """
    This function is to extract the latest build version from the notes section of the docstring
    """
    # Define the regex pattern for the [Latest Build Version]
    pattern = r"\[Latest Build Version\]\n\s*o\s*(\d+\.\d+\.\d+\.\d+)"

    # Search for the pattern in the text
    match = re.search(pattern, text)

    # Return the matched version or None if not found
    return match.group(1) if match else None

def display_output(info, print_type, color=None):
    """
    This function is to Display output to the console or return the output as a string
    """
    if print_type:
        return info
    else:
        if color:
            print(f"[{color}]{info}[/{color}]")
        else:
            print(info)
        return

def main(args):
    """
    This is the main function to parse and display the docstring of a Python module or function
    """
    # Set Variables
    version_flag = args.version
    module = args.module
    full_help_flag = args.full_help
    examples_flag = args.examples
    build_notes_flag = args.build_notes
    dependencies_flag = args.dependencies
    notes_flag = args.notes
    sample_docstring_flag = args.sample_docstring
    return_only_flag = args.return_only
    module_path = os.path.realpath(module)

    try:
        pydoc_cmd = f'python3 -m pydoc {module_path}'
        results = subprocess.run(pydoc_cmd, shell=True, capture_output=True, text=True, check=False)
        docstring = results.stdout
    except subprocess.CalledProcessError:
        pass

    if results.returncode != 0:
        try:
            pydoc_cmd = f'python -m pydoc {module_path}'
            results = subprocess.run(pydoc_cmd, shell=True, capture_output=True, text=True, check=False)
            docstring = results.stdout
        except subprocess.CalledProcessError:
            pass

    if results.returncode != 0:
        display_output(f"Error: Unable to find module or function: {module}", return_only_flag, 'red')

    parsed_sections = parse_docstring(docstring)

    if version_flag:
        latest_build_version = extract_latest_build_version(parsed_sections["Notes"])
        display_output(latest_build_version, return_only_flag)
    elif full_help_flag:
        display_output(docstring, return_only_flag)
    elif examples_flag:
        display_output(f'{" "*8}{parsed_sections["Examples"]}', return_only_flag)
    elif notes_flag:
        display_output(f'{" "*8}{parsed_sections["Notes"]}', return_only_flag)
    elif dependencies_flag:
        display_output(f'{" "*8}{parsed_sections["Dependencies"]}', return_only_flag)
    elif build_notes_flag:
        display_output(f'{" "*8}{parsed_sections["Build Notes"]}', return_only_flag)
    elif sample_docstring_flag:
        help_docstring = '''
        """
        .DESCRIPTION
            This is a description of the module or function.

        .NOTES
            [Original Author]
                o <Author Name>
            [Original Build Version]
                o <Major>.<Minor>.<Patch>.<Date<YYYYMMDD>>
            [Latest Author]
                o <Author Name>
            [Latest Build Version]
                o <Major>.<Minor>.<Patch>.<Date<YYYYMMDD>>
            [Comments]
                o <Comments>
            [Python Compatibility / Tested On]
                o Python <Version>
            [Forked Project]
                o <Project Name>

        .DEPENDENCIES
            o <Dependency 1> # <Dependency 1 Description>
            o <Dependency 2> # <Dependency 2 Description>

        .BUILD NOTES
            o <Version 1>
                [<Author Name>] <Description>

            o <Version 2>
                [<Author Name>] <Description>

        .EXAMPLES
            Command: <Command>
            Description: <Description>
            Notes: <Notes>
            Output: <Output>

            Command: <Command>
            Description: <Description>
            Notes: <Notes>
            Output: <Output>
        """
        '''
        display_output(help_docstring, return_only_flag)
    else:
        display_output(f'{" "*8}{parsed_sections["Description"]}', return_only_flag)

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Parse and display the docstring of a Python module or function.")
    parser.add_argument('-v', '--version', action='store_true', help='Show the latest build version')
    parser.add_argument('-m', '--module', required=True, type=str, help='The module or function to parse')
    parser.add_argument('-fh', '--full_help', action='store_true', help='Get the full help docstring')
    parser.add_argument('-ex', '--examples', action='store_true', help='Get the examples')
    parser.add_argument('-bn', '--build_notes', action='store_true', help='Get the Build Notes')
    parser.add_argument('-dp', '--dependencies', action='store_true', help='Get the Dependencies')
    parser.add_argument('-nt', '--notes', action='store_true', help='Get the Notes')
    parser.add_argument('-sd', '--sample_docstring', action='store_true', help='Return a sample docstring')
    parser.add_argument('-ro', '--return_only', action='store_true', help='Return the parsed sections only, do not print to console')

    main(parser.parse_args())