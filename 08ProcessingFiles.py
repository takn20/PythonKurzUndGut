import os

os.mkdir( 'files-examples-dir' )
os.mkdir( 'files-examples-dir/rename-dir' )
os.mkdir( 'files-examples-dir/subdir1' )
os.mkdir( 'files-examples-dir/subdir2' )

new_csv_file = open( 'files-examples-dir/example-data.csv', mode = "x" )
# if command with mode "x" is run again, then 'FileExistsError'; "x" is for creation only
# documentation on modes https://docs.python.org/3/library/functions.html#open 

os.chdir( 'files-examples-dir' )
new_text_file = open( 'example-file.txt', mode = 'x' )

print( os.getcwd() )
print( 'Absolute path:', os.path.abspath( '.' ) )
print( 'Absolute path:', os.path.abspath( '..' ) )

print( os.listdir() )

for item in os.listdir() :
    if os.path.isdir( item ) :
        print( item, 'is a directory.' )
    if os.path.isfile( item ) :
    #else :
        print( item, 'is a file.' )

def check_exists( path ) :
    if os.path.exists( path ) :
        print( path, 'exists.' )
    else :
        print( path, 'does not exist.' )

check_exists( 'example-file.txt' )
check_exists( 'special.md' )

file_to_read = open( 'test.txt' , mode = 'r' )
file_to_write = open( 'test.txt', mode = 'w' )
binary_file_readwrite = open( 'image.bmp', mode = 'r+b' )
file_to_read.close()
file_to_write.close() 
binary_file_readwrite.close() 

file = open( 'test.txt', encoding = 'utf-8' )
try : 
    # file actions
    pass
finally :
    file.close() 

# more elegant yet
with open( 'test.txt', encoding = 'utf-8' ) as file :
    # file actions
    pass 

# May 8, 2024

with open( 'personenListe.txt', 'w', encoding = 'utf-8' ) as file :
    file.write( 'Person1: Michael\n' )
    file.write( 'Person2: Peter\n' )
    file.write( 'This file contains three lines.\n' )

with open( 'personenListe.txt', 'r', encoding = 'utf-8' ) as file :
    for line in file :
        print( line, end = '' )

with open( 'personenListe.txt', 'r', encoding = 'utf-8' ) as file :
    content = file.read()
    print( content )

with open( 'personenListe.txt', 'r', encoding = 'utf-8' ) as file :
    lines = file.readlines()
    print( 'Lines', lines )

    file.seek( 0 ) # reset pointer
    count = 1
    while line_content := file.readline() :
        print( 'Line', count, ':', line_content, end = '' )
        count += 1

path = 'to_be_created.txt'
check_exists( path )
with open( path, 'x' ) as file :
    pass

check_exists( path )

path = 'overwrite.txt'
check_exists( path )
with open( path, 'w' ) as file :
    file.write( 'Create if does not exist else overwrite.\n' )

check_exists( path )
with open( path, 'r' ) as file :
    while line_content := file.readline() :
        print( 'Line:', line_content, end = '' )

with open( path, 'w' ) as file :
    file.write( 'Force overwrite.\n' )

with open( path, 'r' ) as file :
    while line_content := file.readline() :
        print( 'Line:', line_content, end = '' )

path = 'append.txt'
check_exists( path )
with open( path, 'w' ) as file :
    file.write( 'Append - 1\n' )

with open( path, 'a' ) as file :
    file.write( 'Append - 2\n' )

with open( path, 'r' ) as file :
    print( file.readlines() )

path = 'append.txt'
print( 'Size', path, ':', os.path.getsize( path ) )
print( 'Size "." :', os.path.getsize( '.' ) )
print( 'Size ".." :', os.path.getsize( '..' ) )

for item in os.listdir() :
    if os.path.isdir( item ) :
        print( item, 'is a directory.' )
    if os.path.isfile( item ) :
        with open( item, 'r' ) as file :
            print( item, 'is readable', file.readable() )
            print( item, 'is writeable', file.writable() )

# for directory use os.access() with R_OK, W_OK etc not as elegant

# May 15, 2024
import os
import datetime
def convert_seconds_to_time( seconds ) :
    return datetime.datetime.fromtimestamp( seconds )

os.getcwd()
os.listdir()
os.chdir( 'files-examples-dir' )
print( 'created:', convert_seconds_to_time( os.path.getctime( 'append.txt' ) ) )
print( 'modified:', convert_seconds_to_time( os.path.getmtime( 'append.txt' ) ) )
print( 'accessed:', convert_seconds_to_time( os.path.getatime( 'append.txt' ) ) )

import shutil # for high-level file operations

shutil.copy( 'append.txt', 'copy_append.txt' )
os.listdir()

path_destination1 = 'subdir2/example-file1.txt' 
path_destination2 = 'subdir2/example-file2.txt'

shutil.copy( 'example-file.txt', path_destination1 ) 
# shutil.copy2 also tries to preserve metadata
shutil.copy2( 'example-file.txt', path_destination2 )

os.listdir( 'subdir2' )

# renaming, why not do this with shell/ bash/ zsh directly?

os.chdir( 'rename-dir' )
file_initial = open( 'to-be-renamed.txt', 'w' )
os.listdir() 

def rename_file() :
    if os.path.exists( 'to-be-renamed.txt' ) :
        os.rename( 'to-be-renamed.txt', 'renamed.txt' )
    elif os.path.exists( 'renamed.txt' ) :
        os.rename( 'renamed.txt', 'to-be-renamed.txt' )

rename_file()
os.listdir()

rename_file()
os.listdir()

os.chdir( '..' )

os.mkdir( 'dir-to-be-deleted' )
file_to_be_deleted1 = open( 'dir-to-be-deleted/file-to-be-deleted1.txt', 'x' )
file_to_be_deleted2 = open( 'dir-to-be-deleted/file-to-be-deleted2.txt', 'x' )
os.listdir( 'dir-to-be-deleted' )

os.remove( 'dir-to-be-deleted/file-to-be-deleted1.txt' )
os.listdir( 'dir-to-be-deleted' )

os.mkdir( 'dir-to-be-deleted/new-and-empty' )
os.listdir( 'dir-to-be-deleted' )

os.rmdir( 'dir-to-be-deleted/new-and-empty' )
os.listdir( 'dir-to-be-deleted' )

os.rmdir( 'dir-to-be-deleted' ) # returns error, directory not empty, need to use shutil.rmtree

shutil.rmtree( 'dir-to-be-deleted' )
os.listdir()

## May 22, 24
## 8.2 JSON Verarbeitung
## leichtgewichtiges Format für Datenaustausch

import os
os.getcwd()
os.listdir()
os.chdir( 'files-examples-dir' )

import json

data = { 
    "TIM" : { "name" : "Tim", "age" : 50, "city" : "Kiel" },
    "MIKE" : { "name" : "Mike", "age" : 50, "city" : "Zürich" },
    "INFO" : [ "This", "is", "an", "information" ],
    "CHECKSUM" : 4711
}

with open( 'data.json', 'w' ) as jsonfile :
    json.dump( data, jsonfile )

with open( 'data.json', 'r' ) as jsonfileRead :
    dataRead = json.load( jsonfileRead )

dataRead

dataFormatted = json.dumps( data, indent = 4 )
print( dataFormatted )
