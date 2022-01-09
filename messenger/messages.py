#!/usr/bin/env python3

from sqlalchemy.sql.schema import Column


class Messengers:

    def messenger_run(self,msg: str)-> str:
        # ANSI color code
        RED = "\033[1;31m"
        YELLOW = "\033[1;33m"
        BLUE = "\033[1;34m"
        GREEN = "\033[1;32m"
        CLOSE = "\033[0m"

        # msg: invalid argument
        if msg == "invalid_args":
            error_msg = f"""
{RED}| Error:{CLOSE} Invalid arguments
{BLUE}| Info:{CLOSE} Try running awspie -help
            """
            return error_msg

        # msg: invalid awspie configuration
        if msg == "invalid_awspieconfig":
            error_msg = f"""
{RED}| Error:{CLOSE} AWSPIE setup configuration missing
{BLUE}| Info:{CLOSE} Run awspie -setup
            """
            return error_msg

        # msg: help
        if msg == "run_help":
            help_msg = f"""
| AWSPIE - Monitor and Manage AWS resources
{YELLOW}| Usage:{CLOSE}
       -setup   : setup awspie cli environment
       -version : print awspie release version
            """
            return help_msg
        
        # msg: version
        if msg == "run_version":
            version_msg = f"""
| AWSPIE - Monitor and Manage AWS resources
{YELLOW}| Version:{CLOSE}
        awspie 1.0.0
            """
            return version_msg

        # msg: permission error
        if msg == "permission_error":
            error_msg = f"""
{RED}| Error:{CLOSE} Permission Error
{BLUE}| Info:{CLOSE} Run sudo awspie -setup
            """
            return error_msg