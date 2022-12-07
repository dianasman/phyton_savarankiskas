# Sukurkite klasę "Movie", kuri gebės sukurti objektus 3 savybėm ir 1 metodu. 
# Naudojant šią klasę sukurkite bent du skirtingus objektus.

# Savybės:
# title: string
# director: string
# budget: number

# Metodas: 
# wasExpensive() - jeigu filmo "budget" yra daugiau nei 100 000 000 mln USD, tada grąžins True, kitu atveju False. 

class Movie:
    def __init__(self, title, director, budget):
        self.title = title
        self.director = director
        self.budget = budget

    def wasExpensive(self):
        if (self.budget >= 10000000):
            return True
        elif self.budget < 10000000:
                return False      

movies = []

movie1 = Movie("Dark" , "Baran bo Odar" , 102000000)
movie2 = Movie("Wednesday", "Tim Burton", 9990999)
movie3 = Movie("1899", 'Baran bo Odar', 550000000)

movies.append(movie1)
movies.append(movie2)
movies.append(movie3)

for movie in movies:
    print(movie.title, movie.director, movie.budget, movie.wasExpensive())