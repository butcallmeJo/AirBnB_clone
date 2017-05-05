#!/usr/bin/python3
"""
This is module base_model
This module defines one class HBNBCommand.
It inherits from cmd and creates a command interpreter
"""
import cmd
# from models.base_model import BaseModel
# from models.user import User
# from models.amenity import Amenity
# from models.city import City
# from models.place import Place
# from models.review import Review
# from models.state import State
# from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Create a command interpreter.

    **Class Attributes**
        prompt: the prompt
        valid_classes: all the classes currently handled by the
        interpreter
    """
    prompt = '(hbnb) '
    # storage.reload()
    # valid_classes = {"BaseModel": BaseModel, "User": User,
    #  "Amenity": Amenity, "City": City, "Place": Place,
    #  "Review": Review, "State": State}

    def emptyline(self):
        """handles empty commands"""
        pass

    def do_quit(self, args):
        """Quit command to exit the program"""
        quit()

    def do_EOF(self, args):
        """Ctrl + D to exit program"""
        print("")
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
