import os
os.getcwd()

if os.path.exists("test.txt"):

    try:
        data = open('test.txt', 'w')

        print('write xxx')

        data.close()
    except Exception, e:
        print(e)
        pass
else:
    print('The data file is missing!')