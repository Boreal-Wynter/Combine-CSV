import os
import sys
import glob
import pandas as pd

def main():
    data_directory = sys.argv[1]
    target_directory = sys.argv[2]
    extension = sys.argv[3]

    os.chdir(data_directory)

    fetch_files = [file for file in glob.glob('*.{}'.format(extension))]

    keep_column_header = pd.read_csv(fetch_files[0])
    remove_column_header = [pd.read_csv(file, skiprows=1) for file in fetch_files[1:]]

    combined_csv_file = pd.concat([keep_column_header] + remove_column_header, ignore_index=True)

    os.chdir(target_directory)

    combined_csv_file.to_csv("results.csv", index=False, encoding='utf-8-sig')

    return

if __name__ == "__main__": 
    main()