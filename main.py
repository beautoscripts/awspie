#!/usr/bin/env python3

import os
import shutil
import sys
from messenger.messages import Messengers

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


# function: validate aruguments
def validate_args(arglist: list) -> bool:
    
    # dict: parent args (key): length of argument (value)
    args_dict = {
        '-help':1,
        '-setup':1,
        '-version':1
    }

    # check parent args availability in dict
    if arglist[0] in args_dict and len(arglist) == args_dict.get(arglist[0]):
        return True
    else:
        return False    


# function: main
def main():
    # obj: Messenger
    msg_obj = Messengers()

    """
        - check if the valid arguments are passed
        - check if awspie configuration files are available
    """
    if len(sys.argv[1:]) == 0:
        # validating awspie configuration and arguments
        if not validate_awspie_config():
            msg_obj.messenger_run("invalid_awspieconfig")
            quit(1)
        else:
            msg_obj.messenger_run("invalid_args")
            quit(1)

    # check for valid parent arguments
    args_list = sys.argv[1:]
    if not validate_args(args_list):
        print("ERROR")
        quit(1)
    else:
        if args_list[0] == '-help':
            print(msg_obj.messenger_run("run_help"))
            quit(0)
        if args_list[0] == '-version':
            print(msg_obj.messenger_run("run_version"))
            quit(0)

        if args_list[0] == '-setup':
            profile_dir_path = "/usr/local/awspie"
            if os.path.isdir(profile_dir_path):
                try:
                    shutil.rmtree(profile_dir_path)
                    quit(0)
                except PermissionError:
                    print(msg_obj.messenger_run("permission_error"))
                    quit(1)

# Start main
if __name__ == "__main__":
    main()