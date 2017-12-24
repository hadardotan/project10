import sys, os, os.path, glob, re
from JackAnalyzer.CompilationEngine import CompilationEngine


def analyze(files_to_process):
    """
    for each jack file in files_to_process:

    - create xml output file
    - compile files using CompilationEngine
    :param files_to_process: paths of files to process
    :return:
    """
    for input_file_name in files_to_process:
        file_name = os.path.splitext(input_file_name)[0]
        output_file_name = file_name + ".xml"

        input_file = open(input_file_name,'r')
        output_file = open(output_file_name,'w')

        compiler = CompilationEngine(input_file, output_file)


def main(path):
    """
    gets input files as
    fileName.jack - name of single source file, or
    directoryName - name of a directory containing one or more .jack source
    files

    alanyzes files
    :return:
    """
    files_to_process =[]
    if os.path.isfile(path):
        files_to_process = [path]

    elif os.path.isdir(path):
        files_to_process = [os.path.join(path, f) for f in os.listdir(path) if
                            f.endswith(".jack")]

    analyze(files_to_process)




if __name__ == "__main__":
    main(sys.argv[1])

#
# main("C:\nand\nand2tetris\projects\10\test3\2")

