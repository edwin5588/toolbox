#
# Given a text file of a list of packages and their versions,
# as well as a text file of a list of packages,
# output the version of packages to find

import os
import re
import sys
import subprocess

class get_package_version:

    def __init__(self, fp):
        self.filelocation = fp
        self.contents = self.open_file(fp)
        self.packages_to_find = self.input_packages()



    def open_file(self, fp):
        """
        opens a text file and returns a list, where each item is a line
        """
        contents = {}

        with open(fp, 'r') as file:
            header_line = next(file)
            for line in file:
                    newline = line.strip()
                    package, version_info = newline.split("/")
                    contents[package] = version_info
        file.close()

        return contents


    def input_packages(self):
        """
        Nonending while loop that requires the user to input packages until
        user presses Ctrl + C (keyboard interrupt)
        it will continuously give versions of packages as well
        """
        try:
            while True:
                val = input("Enter your package name: ")
                print(self.contents[val])
        except KeyboardInterrupt:
            print("Package version finding tool stopped...")


if __name__ == "__main__":
    fp = sys.argv[1]

    package_finder = get_package_version(fp)
    
