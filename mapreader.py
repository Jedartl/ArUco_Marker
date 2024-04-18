import pickle
import copy  # Might be used for other operations in surrounding code

# Load data from a pickle file
mapa = pickle.load(open("mapa.pickle", "rb"))
# This line opens the file "mapa.pickle" in read-binary mode and loads the
# serialized Python object back into a variable named `mapa`.

# Access and print specific data from the loaded object
for element in mapa["values"]:
    # Iterate through each element in the list named "values" within the `mapa` object
    print(element[1])
    # Print the second element (index 1) of each element in the list