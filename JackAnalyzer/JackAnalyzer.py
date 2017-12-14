import sys, os, os.path, glob




def main():
    """
    :return:
    """




def get_files_from_input(input):
    """
    gets input files as
    fileName.jack - name of single source file, or
    directoryName - name of a directory containing one or more .jack source
    files
    :return: file(/s) according to input type : dir or file
    """
    if input.endswith('.jack'):
        return [input], input.replace('.jack', '.xml')
    else:
        # case input is dir - generates xml file for every .jack file in dir
        return glob.glob(input + '/*.jack'), input + '/' + input + '.xml'

