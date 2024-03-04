# BMP Studio
Welcome to this repository! This repository at the point of the first draft of the `README.md` file contains code for a custom website implementation for BMP Studio.

##  [Album](https://github.com/gitloper-azara/bmpstudio/blob/ef8ac9b1c33c168bbfc22b8360029151d6285fea/models/album.py)
Represents collections of photos, like galleries, to be displayed on the website.

##  [Photo](https://github.com/gitloper-azara/bmpstudio/blob/ef8ac9b1c33c168bbfc22b8360029151d6285fea/models/photo.py)
Represents individual photos taken by the studio.

##  [Review](https://github.com/gitloper-azara/bmpstudio/blob/ef8ac9b1c33c168bbfc22b8360029151d6285fea/models/review.py)
Represents reviews left by clients who have engaged with the website or have been rendered services by the studio.

##  [User](https://github.com/gitloper-azara/bmpstudio/blob/ef8ac9b1c33c168bbfc22b8360029151d6285fea/models/user.py)
Represents users of the website.

# Console (cmd CRUD)
The [console](https://github.com/gitloper-azara/bmpstudio/blob/ef8ac9b1c33c168bbfc22b8360029151d6285fea/bmp_console.py) allows for CRUD (Create, Update, Destroy, etc) operations on objects. It allows for data model creation. It stores and persists objects to a file (JSON file). The console is a tool that validates the storage engine that I have built. From the console code and from the front-end and RestAPI I will build later, I do not have to worry about how objects are stored. This console abstraction will also allow me to change the type of storage easily without updating my entire codebase.

## Requirements
Python 3.8.5 or later

## How to use the console
1. Clone this repository onto a safe local system. `Ubuntu 20.04` is preferred because it was built on `WSL: Ubuntu-20.04`. Any other local system should still work.
    ```bash
    git clone https://github.com/gitloper-azara/bmpstudio.git
2. Navigate to the root of the cloned repository
    ```bash
    cd bmpstudio
3. Grant execution rights of the console to the current user.
    ```bash
    chmod +x bmp_console.py
4. Run the command `$ ./bmp_console.py` to start the console in interactive mode.
    Sample screen display;
    ```bash
    azara@Ubuntu:~/bmpstudio$ ./bmp_console.py
    (bmp)
5. Type `help` from within the console to display the CRUD commands/methods available
    ```bash
    azara@Ubuntu:~/bmpstudio$ ./bmp_console.py
    (bmp) help

    Documented commands (type help <topic>):
    ========================================
    EOF all create destroy help quit show update

    (bmp) quit
6. For a complete list of commands and their usage, check `Documented commands` and use the `help` command.
    Sample usage;
    ```bash
    (bmp) help

    Documented commands (type help <topic>):
    ========================================
    EOF all create destroy help quit show update

    (bmp)
    (bmp) help create
    Usage: create <class_name>
    Create would make an instance of a model and save this newly created instance to a JSON file.
    (bmp)
    (bmp) quit
