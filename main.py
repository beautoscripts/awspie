#!/usr/bin/env python3

import os
import shutil
import sys
from messenger.messages import Messengers
from sqlalchemy import create_engine,MetaData,Table,Column,Integer,String,DateTime, engine
from sqlalchemy_utils import database_exists,create_database
from datetime import datetime

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
        '-create':2,
        '-version':1
    }

    # check parent args availability in dict
    if arglist[0] in args_dict and len(arglist) == args_dict.get(arglist[0]):
        return True
    else:
        return False    

# function : build profile database
def build_profile_database():
    # create database
    engine = create_engine('sqlite:////usr/local/awspie/profile.db',echo=True)
    create_database(engine.url)

    # create table
    meta = MetaData()
    db_url = "sqlite:////usr/local/awspie/profile.db"
    profile_table = Table('profile',meta,Column('id',Integer(),primary_key=True),Column('profile_name',String(10),nullable=False,unique=True),
    Column('aws_accesskey_id',String(50),nullable=False,unique=True),
    Column('aws_secretkey',String(50),nullable=False,unique=True),
    Column('aws_region',String(10),default="us-east-1"),
    Column('date_created',DateTime(),default=datetime.utcnow)
    )
    meta.create_all(engine)
    return f"Created Database"
    
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
        print(msg_obj.messenger_run("invalid_args"))
        quit(1)
    else:
        # help argument
        if args_list[0] == '-help':
            print(msg_obj.messenger_run("run_help"))
            quit(0)
        # version argument
        if args_list[0] == '-version':
            print(msg_obj.messenger_run("run_version"))
            quit(0)
        # setup argument
        if args_list[0] == '-setup':
            directory = "awspie"
            profile_path = "/usr/local/"
            profile_dir_path = "/usr/local/awspie"
            BLUE = "\033[1;34m"
            CLOSE = "\033[0m"

            # show warning message and ask user permission to proceed
            user_input=input(f"""| AWSPIE - Monitor and Manage AWS resources
{BLUE}| Info:{CLOSE} If you have existing profile setup, it will be deleted. Press 'Y/y' to continue and 'N/n' to quit.\n""")

            if user_input in ['Y','y']:
                
                if os.path.isdir(profile_dir_path):
                    try:
                        shutil.rmtree(profile_dir_path)
                        path = os.path.join(profile_path,directory)
                        os.makedirs(path)
                        build_profile_database()
                        print(msg_obj.messenger_run("db_created"))
                        quit(0)
                    except PermissionError:
                        print(msg_obj.messenger_run("permission_error"))
                        quit(1)
                else:
                    try:
                        path = os.path.join(profile_path,directory)
                        os.makedirs(path)
                        build_profile_database()
                        print(msg_obj.messenger_run("db_created"))
                        quit(0)
                    except PermissionError:
                        print(msg_obj.messenger_run("permission_error"))
                        quit(1)
            else:
                quit(0)
        # create profile argument
        if args_list[0] == '-create':
            BLUE = "\033[1;34m"
            CLOSE = "\033[0m"
            print(f"""| AWSPIE - Monitor and Manage AWS resources\n""")
            profile_name = input(f"{BLUE}|{CLOSE} Profile Name : ").split()
            aws_accesskeyid = input(f"{BLUE}|{CLOSE} AWS Access Key Id : ").split()
            aws_secretaccesskey = input(f"{BLUE}|{CLOSE} AWS Secret Access Key : ").split()
            aws_region = input(f"{BLUE}|{CLOSE} AWS Region [ Default: us-east-1 ] : ").split()
        

# Start main
if __name__ == "__main__":
    main()