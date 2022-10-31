#!/usr/bin/python3
"""This script contains the entry point of the command interpreter
"""
import cmd
import sys
import shlex
from models.base_model import BaseModel

classes = {'BaseModel': BaseModel, 'User': User, 'State': State, 'City': City,
            'Place': Place, 'Amenity': Amenity, 'Review': Review}


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class
    Methods:
        do_EOF
        do_quit
        emptyline
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

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        try:
            args = shlex.split(arg)
            if len(args) == 0:
                print("** class name missing **")
            elif args[0] in classes:
                print(eval(args[0])().id)
                models.storage.save()
                print("** Created successfully! **")
            else:
                print("** class doesn't exist **")
        except Exception:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints string representation of an instance based on
            the class name and id
            """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            if len(args) > 1:
                key = args[0] + '.' + args[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            if len(args) > 1:
                key = args[0] + '.' + args[1]
                if key in models.storage.all():
                    del models.storage.all()[key]
                    models.storage. save()
                    print("** Deleted successfully! **") # Remove later
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = shlex.split(arg)
        if len(args) > 0 and args[0] not in classes:
            print("** class doesn't exist **")
        else:
            object_dt = []
            for item in models.storage.all().values():
                if len(args) >= 0 and args[0] == item.__class__.__name__:
                    object_dt.append(item.__str__())
            for i in range(len(object_dt)):
                print(object_dt[i])
                if i == len(object_dt) - 1:
                    break

    def do_update(self, arg):
        """Updates an instance based on the class name and 'id'"""
        args == shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            if len(args) > 1:
                key = args[0] + '.' + args[1]
                if key in models.storage.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            setattr(models.storage.all()[key,
                                args[2]], args[3])
                            models.storage.save()
                            print("** Updated successfully! **") # Remove later
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNHCommand().cmdloop()
