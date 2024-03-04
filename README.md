# bmpstudio
Welcome to this repository! This repository at the point of the first draft of the `README.md` file contains code for a custom website implementation for BMP Studio.

##  Album
Represents collections of photos, like galleries, to be displayed on the website.

##  Photo
Represents individual photos taken by the studio.

##  User
Represents users of the website.

##  Review
Represents reviews left by clients who have engaged with the website or have been rendered services by the studio.

- Console (cmd CRUD)
The console allows for CRUD (Create, Update, Destroy, etc) operations on objects. It allows for data model creation. It stores and persists objects to a file (JSON file). The console is a tool that validates the storage engine that I have built. From the console code and from the front-end and RestAPI I will build later, I do not have to worry about how objects are stored. This console abstraction will also allow me to change the type of storage easily without updating my entire codebase.

## Requirements
Python 3.8.5 or later

## How to start the console
1. Clone this repository onto a safe local system. `Ubuntu 20.04` is preferred because it was built on `WSL: Ubuntu-20.04`. Any other local system should still work.
    ```bash
    git clone https://github.com/gitloper-azara/bmpstudio.git
2. Navigate to the root of the clone repository
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
