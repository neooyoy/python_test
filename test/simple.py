import nester

def getMovie():
    print(1)

movies = ["the holy grail",
          "the life of brian",
          "the meanin of life"]

movies.pop()

movies.insert(1, "test0")

movies.append(["test1", "test2"])

nester.getMovie(movies)

# print(movies)
