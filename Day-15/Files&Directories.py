# Files & Directories
"""
We can work on our file/directory by creting, removing, checking & searching
for file/directory using module called 'pathlib' which will provide
object-oriented filesystem paths.
We basically have 2 ways. They are :
1. Absolute Path - Way of working with the path from the root of our Hard disk.
   Example : (C:\'ProgramFiles\'....)
2. Relative Path - Way of working with the path from our current directory we
   are working on.
Mostly we use Relative Path when we are working with files/directories.
"""
from pathlib import Path

path = Path("Day-15")
print(path.exists())            # True

# Creating a directory
path = Path("MKDIR")
print(path.mkdir())             # None - (folder created)

# To remove a Directory
print(path.rmdir())             # None - (remove "MKDIR")

# To search a file/folder
path = Path()
print(path.glob('*.py'))

# To iterate over a directory
path = Path()

for file in path.glob('*.txt'):
    print(file)

# Output :
# <generator object Path.glob at 0x000001A5A8EA46D0>
# demo.txt
# NewFile.txt
