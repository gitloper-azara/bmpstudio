#!/usr/bin/env bash
# This is a custom script that automates the setup of the BMP Studio database
# Refer the to sql files for detailed information about the database setup process
# NOTE: using the script in your environment might fail if your root user requires
# a password before accessing MySQL.

# This script further assumes all files are located in the same path as this script
# It is no substitute for a manual process. It is created for my perusal ONLY!

server="mysql"
database="bmpstudio_db"
init="init_bmp.sql"
setup="setup_bmpstudio.sql"
db_user="bmp_dev"
host="localhost"

# delete the database if it exists
echo "DROP DATABASE IF EXISTS "$database";" | "$server" -uroot

# initialise the database and user
cat "$init" | "$server" -uroot

# create relevant tables and constraints if available
cat "$setup" | "$server" -u"$db_user" -h"$host" -p "$database"
