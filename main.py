#!/usr/bin/env python3

import os
import sys


# function : message handler
def messenger(msg: str)-> str:
    # ANSI color code
    RED = "\033[1;31m"
    YELLOW = "\033[1;33m"
    BLUE = "\033[1;34m"
    GREEN = "\033[1;32m"
    CLOSE = "\033[0m"


    if msg == "invalid_args":
        error_msg = f"""
{RED}| Error:{CLOSE} Invalid arguments
{BLUE}| Info:{CLOSE} Try running awspie -help
        """
        return error_msg
    if msg == "invalid_awspieconfig":
        error_msg = f"""
{RED}| Error:{CLOSE} AWSPIE setup configuration missing
{BLUE}| Info:{CLOSE} Run awspie setup
        """
        return error_msg

# function: validate the awspie configuration
def validate_awspie_config() -> bool:
    orig_dir_path = "/usr/local/awspie"
    db_path = "/usr/local/awspie/db/profile"

    if os.path.isdir(orig_dir_path):
        # check if profile database exists
        if os.path.isfile(db_path):
            return True
        else:
            return False
    else:
        return False

# function: main
def main():
    """
        - check if the valid arguments are passed
        - check if awspie configuration files are available
    """
    if len(sys.argv[1:]) == 0:
        # validating awspie configuration and arguments
        if not validate_awspie_config():
            print(messenger("invalid_awspieconfig"))
            quit(1)
        else:
            print(messenger("invalid_args"))
            quit(1)

# Start main
if __name__ == "__main__":
    main()