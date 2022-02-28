"""
Let's make a very basic Path object

"""

from pathlib import Path

##
cwd = Path.cwd()


## create a new path using concatenation

# you can use cwd.joinpath
# or you can use the special / symbol (overloaded for concatenation)


## examine your new path object

## print the following parts

# .parent

# .anchor

# .name

# .stem

# .suffix

# .parent


## check if your path is a directory or file

## .is_file()

## .is_dir()

## print out your path and look at the type (you may need to print(type(your_path_here)))
## does it accurately reflect your OS?
