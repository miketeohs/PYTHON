import io
dummy_file = io.StringIO()                        # declare a dummy file
print('Hello Geeks!!', file=dummy_file)           # add message to the dummy file
print(dummy_file.getvalue())                      # get the value from dummy file

# ************** Write to a file ************************************************#
Testfile.txt = io.StringIO()
print('Welcome to GeeksforGeeks Python world.!!', file=open('Testfile.txt', 'w'))
#print("Testfile.txt".getvalue())
print('Testfile.txt'.getvalue())                      # get the value from dummy file
