# Modules and pip in Python!

Module is like a code library which can be used to borrow code written by somebody else in our Python program. There are two types of modules in Python:

1. **Built-in Modules** - These modules are ready to import and use and ship with the Python interpreter. There is no need to install such modules explicitly.

2. **External Modules** - These modules are imported from a third-party file or can be installed using a package manager like pip or conda. Since this code is written by someone else, we can install different versions of the same module over time.

## The pip command

It can be used as a package manager `pip` to install a Python module. Let's install a module called pandas using the following command:

```bash
py -m pip install pandas