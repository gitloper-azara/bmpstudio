#!/usr/bin/python3
'''A command line interpreter that performs CRUD operations
for the website.
'''

import cmd
import shlex
from models.album import Album
from models.base_model import BaseModel
from models.photo import Photo
from models.review import Review
from models.tags import Tag
from models.user import User
from models import storage


class BMPCommand(cmd.Cmd):
    '''Console that performs CRUD operations.'''
    prompt = '(bmp) '
    methods = ['create', 'show']
    __classes = {
        'BaseModel': BaseModel,
        'Album': Album,
        'Photo': Photo,
        'Review': Review,
        'Tag': Tag,
        'User': User
    }

    def precmd(self, line: str) -> str:
        '''Handles custom implementation of CRUD commands'''
        if not line or not line.endswith(')'):
            return line

        flag = 1
        for classs in self.__classes:
            for method in self.methods:
                if line.startswith(f'{classs}.{method}'):
                    flag = 0
        if flag:
            return line

        temp = ''
        for method in self.methods:
            temp = line.replace('(', '.').replace(')', '.').split('.')
            if temp[0] not in self.__classes:
                return ' '.join(temp)
            while temp[-1] == '':
                temp.pop()
            if len(temp) < 2:
                temp = f'{temp[1]} {temp[0]}'
            else:
                temp = f'{temp[1]} {temp[0]} {temp[2]}'

            if temp.startswith(method):
                return temp

        return ''

    def do_create(self, arg):
        '''Creates a new instance of BaseModel, saves it to the JSON file
        and prints the id
        '''
        args = parse(arg)
        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in self.__classes:
            print("** class doesn't exists **")
        else:
            new_instance = eval(f'{args[0]}()')
            new_instance.save()
            print(new_instance.id)

    @staticmethod
    def help_create():
        '''Static method that displays the help info of the create method.
        '''
        print(
            'Usage: create <class_name>'
            '\nCreate would make an instance of a model and save this '
            'newly created instance to a JSON file.'
        )

    def do_show(self, arg):
        '''Prints the string representation of an instance based on the
        class name and id
        '''
        args = parse(arg)
        if len(args) < 2:
            print('** instance id missing **')
            return
        if args[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        key = f'{args[0]}.{args[1]}'
        if key not in storage.all():
            print('** no instance found **')
            return
        print(storage.all()[key])

    @staticmethod
    def help_show():
        '''Static method that displays the help info of the show method.
        '''
        print(
            'Usage: show <class_name> <instance_id>'
            '\nShows the string representation of an instance '
            'based on the class name and instance id.'
        )

    def do_quit(self, arg):
        '''Quit command that exists the program'''
        return True

    def do_EOF(self, arg):
        '''Exits the program on Ctrl+D'''
        print()
        return True

    def emptyline(self):
        '''Do nothing on emptyline by overiding default emptyline behaviour
        '''
        pass


def parse(line):
    '''Handles command line parsing using shell logic.'''
    return shlex.split(line)


if __name__ == '__main__':
    BMPCommand().cmdloop()
