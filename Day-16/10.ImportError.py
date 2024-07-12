# ImportError
"""
ImportError: This exception is raised when an import statement fails to
             find or load a module.
Reasons :
1. Incorrect Module or Package Name
2. Missing Dependencies
3. Issues with Python Path
"""

# 1. Incorrect Module or package Name.
import maths

# Solution : Check Module Names and 
"""
Ensure that the module or package names specified in the import statements are
correct. Double-check the spelling and the case of the names. If the module is
part of a package, verify the directory structure and package hierarchy.
"""
import math

# 2. Missing Dependencies.
import tensorflow

# Solution : Install Missing Dependencies
"""
Use the appropriate package manager (e.g., pip) to install any missing
dependencies. Make sure that all required packages are installed and
up-to-date.
"""
pip install tensorflow

# Solution :

# 3. Issues with Python Path
from mypackage import mymodule

# Solution : Activate and Verify Virtual Environment
"""
If you are using a virtual environment, activate it before running the
script. Ensure that the virtual environment is properly set up and contains
all necessary dependencies.
"""
# Activate virtual environment (Windows)
# venv\Scripts\activate


"""
The ''ImportError: Unknown Location'' in Python can be frustrating, but by
understanding the reasons behind it and following the appropriate approaches,
you can effectively troubleshoot and resolve the issue. Double-checking module
names, installing missing dependencies, verifying virtual environment setups,
and examining the Python path are crucial steps in debugging and fixing import
errors.
"""
