import os
os.getcwd()

if os.path.exists("test.txt"):

    try:
        data = open('test.txt')

        data.seek(0)

        for each_line in data:
            try:
                if each_line.find(':') != -1:
                    (role, line_spoken) = each_line.split(":", 1)
                    print(role)
                    print(" said: ")
                    print(line_spoken)
                else:
                    print(each_line)
            except ValueError:
                pass

        data.close()
    except Exception, e:
        print(e)
        pass
else:
    print('The data file is missing!')