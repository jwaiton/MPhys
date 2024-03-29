import numpy as np
import matplotlib.pyplot as plt
import sys

# read and write, read formats into float array now with tuples
def read_file(filename):
    with open(filename) as f:
        contents = f.readlines()

    if (len(contents) > 1):
        print("File read of length: " + str(len(contents)))
    else:
        print("File length is too short to process (please include more positions)")

    # convert to floats in this case
    contents = [contents[i].rstrip().lstrip() for i in range(len(contents))]
    contents = [contents[i].split() for i in range(len(contents))]
    contents = (np.array(contents)).astype(float)
    return contents

def write_file(filename, data, errors, suffix):
    """
    Hand over standard array of data and write to file
    eg File:
    1313
    23232
    242151
    2392
    2323
    ...
    """

    file_name_new = filename + str(suffix)
    # adding .txt for windows
    file_name_new += ".txt"
    with open(file_name_new, "w") as f:
        for i in range(len(data)):
            # reformatting
            pos = str(str(data[i]) + " " + str(errors[i]))
            # FOR COORDINATE SYSTEM
            #pos = str(new_positional[i])
            #pos = pos.strip("[]")
            #pos = pos.replace(",","")
            f.write(pos + "\n")

def main(file_name1, file_name2):
    # Find the largest value in our two read_files, and use this to normalise and write our data.
    data1 = read_file(file_name1)
    data2 = read_file(file_name2)
    print(data1[0], data2[0][0])


    max_val = 0
    # Loop over list looking for max values
    for i in range(len(data)):
        if (data1[i][0] > max_val):
            max_val = data1[i][0]
            max_err = data1[i][1]

        if (data2[i][0] > max_val):
            max_val = data2[i][0]
            max_err = data2[i][1]

    print("Maximum value found at: {:.2f}".format(max_val))

    # Write new normalised files
    norm_positions1 = [data[i][0]/max_val for i in range(len(data1))]
    # apply appropriate error scaling here
    errors1 = [(data[i][0]/max_val) * data[i][1] for i in range(len(data1))]
    #print(norm_positions)

    # Write new normalised files
    norm_positions2 = [data2[i][0]/max_val for i in range(len(data2))]
    # apply appropriate error scaling here
    errors2 = [(data2[i][0]/max_val) * data2[i][1] for i in range(len(data2))]


    write_file(file_name1, norm_positions1, errors1, "norm")
    write_file(file_name2, norm_positions2, errors2, "norm")


# Collect arguments to run, if you dont have enough, stop the code

if len(sys.argv) == 3:
    # ignoring the name of the python script
    main(sys.argv[1], sys.argv[2])
else:
    print("collect_data takes exactly 1 argument. (" + str(len(sys.argv)-1) + ") given\nPlease input two file names")
