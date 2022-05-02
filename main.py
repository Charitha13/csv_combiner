import pandas as pd
import sys
import os
import argparse
from os import path


def parse_args( args):
    """ This function will parse the command line arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument('name', nargs='+')
    return parser.parse_args(args)

class CombineCSV:

    def combineFiles(self):
        """ This function will combine the csv files and stdouts into a file
         and also adds an extra column filename to represent from which file did
          the row came from"""
        dataframes = []
        paths = parse_args(sys.argv[1:]).name

        path1 = ""
        #To get path of the files to be read
        if len(paths) > 0:
            path1 = os.path.dirname(paths[0])
            # #Checking if path is passed or only filename is passed
            if path1.startswith("/"):
                path1 = path1[1:]
            elif path1.startswith("."):
                path1 = path1[2:]
            path1 += "/"

        #Extracting filenames from paths in the arguments
        filenames = []
        for f in paths:
            # if f.startswith("."):
            #     pass
            # else:
            f = "." + f
            if path.exists(f):
                fname = os.path.basename(f)
                if fname.lower().endswith('.csv'):
                    filenames.append(fname)
                else:
                    raise Exception("File Type not compatible. Please enter a csv file")
            else:
                raise Exception("File Not Found. Enter a valid filename")

        #checking if the files have same columns
        read_columns = [pd.read_csv("." + file_path , nrows=0).columns
        for file_path in paths]
        cols_identical = [all(read_columns[0] == colx) for colx in read_columns[1:]]
        same_columns = all(cols_identical)

        #Data reading and manipulating from csv files
        if same_columns:
            for file in filenames:
                dataframe = pd.read_csv(path1 + file, index_col=0)
                dataframe["filename"] = file
                dataframes.append(dataframe)
            concatFiles = pd.concat(dataframes)
        else:
            raise Exception("Columns are not same in the given files. Please check")

        # output the combined data to stdout
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        pd.set_option('display.max_colwidth', None)
        print(concatFiles)
        # concatFiles.to_csv("output13.csv", index = False)

if __name__ == "__main__":
    obj = CombineCSV()
    obj.combineFiles()

