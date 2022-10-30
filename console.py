#!/usr/bin/python3
"""This script contains the entry point of the command interpreter
"""
import cmd, sys


class HBNHCommand(cmd.Cmd):
    """HBNHCommand class
    Methods:
        do_quit

    """
    
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """Quit command to exit the program"""
        sys.exit()

    def do_quit(self, arg):
        """Termiates the console session"""
        quit()

    def emptyline(self):
        """Do nothing when no arguments are passed"""
        pass

if __name__ == '__main__':
    HBNHCommand().cmdloop()
