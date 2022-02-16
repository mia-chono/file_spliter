import argparse
import os
from os import path

split_by = 50
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='split file each x lines (defined by the parameter -l)')
    parser.add_argument(
        "-d",
        "--destination",
        dest="destination",
        help="specify the destination to create the new files"
    )
    parser.add_argument("-l",
                        "--lines",
                        dest="split_by",
                        help="Give by how many lines do you want split your files (default: {})".format(split_by))
    required_args = parser.add_argument_group('required named arguments')
    required_args.add_argument("-f",
                               "--file",
                               dest="file",
                               help="Give the filename or complete path",
                               required=True)

    args = parser.parse_args()
    destination = args.destination

    if args.split_by and int(args.split_by) != 50:
        split_by = args.split_by

    if not destination:
        destination = "./files"

    if not path.exists(destination):
        os.makedirs(destination)

    with open(args.file) as file:
        lines = [line.rstrip() for line in file]

    composite_list = [lines[x:x + int(split_by)] for x in range(0, len(lines), int(split_by))]
    print(composite_list)

    i = 0
    for content in composite_list:
        file_name = "{name}.txt".format(name=str(i).zfill(3))
        with open(os.path.join(destination, file_name), "w") as file:
            # Writing data to a file
            file.writelines("\n".join(content))

        i += 1
