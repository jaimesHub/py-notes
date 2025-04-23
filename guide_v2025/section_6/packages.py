# a package is a collections of modules in a directory
# contains init.py to indicate that it's a package
# init.py can be empty or defined some initialization code

from my_package import module_website, module_internet

module_internet.connect()
module_website.load('www.google.com')