'''
    fdsafds
'''

def getMovie(movies, level=0):
    if isinstance(movies, list):
        for imovie in movies:
            getMovie(imovie, level + 1)
    else :
        for num in range(level):
            print("\t")
        print(movies)

