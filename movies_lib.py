import csv
import os

movie_rows = []

with open('ml-100k/u.item', encoding='latin_1') as f:
#with open('u.item', encoding='latin_1') as f:
    reader = csv.reader(f, delimiter='|')
    for row in reader:
        movie_rows.append(row)
print(movie_rows[:])
print(movie_rows[6][1])
print(movie_rows[7][1])
print(movie_rows[1681][1])

user_id = []
with open('ml-100k/u.user', encoding = 'latin_1') as f:
    reader = csv.reader(f, delimiter = '|')
    for row in reader:
        user_id.append(row)
#print(user_id[:])

ratings = []
with open('ml-100k/u.data', encoding = 'latin_1') as f:
    reader = csv.reader(f, delimiter = '\t')
    for row in reader:
        ratings.append(row)
#print(ratings[:])


class Movie:

    def __init__(self, mid, title):
    #def __init__(self, mid, title, ratings, av_ratings):
        self.mid = mid
        self.title = title


    def __str__(self):
        return "Movie Title {} Average Rating {} Ratings {}". format(self.movietitle, self.avg_ratings, self.ratings)


    def create_movies_with_id_and_title(mid, movietitle, title, ratings, av_ratings):
        pass

    def search_by_movie_id(mid):
        #Search for movies by id in movie list
        #return  movie_rows[mid].title
        return movie_rows[mid][1]


class User:
    def __init__(self, uid, gender):
        self.uid = uid
        self.gender = gender

    def __str__(self):
        return "User Id {}". format(self.uid)


class Ratings:
    def __init__(self, ratings):
        self.ratings_rid = ratings
        self.ratings = []
        self.av_ratings = 0

    def add_rating(self, ratings):
        self.ratings.append(ratings)
        self.av_ratings = sum(self.ratings)/len(self.ratings)

    def __str__(self):
        return "User_ID {} Movie ID {} Ratings {}". format(self.user_rid, self.movie_id, self.ratings_rid)
    # def __str__(self):
    #     return "Ratings {}". format(self.ratings_rid)

    def top_rated_movies(number_of_movies, minum_number_of_ratings):
        top_rated_movies = []
        for movie in movie.title[movie]():
            if len(movie.ratings) >= minum_number_of_ratings_num_ratings:
                top_rated_movies.append(movie)

# def euclidean_distance(v, w):
#     """Given two lists, give the Euclidean distance between them on a scale
#     of 0 to 1. 1 means the two lists are identical.
#     """
#
#     # Guard against empty lists.
#     if len(v) is 0:
#         return 0
#
#     # Note that this is the same as vector subtraction.
#     differences = [v[idx] - w[idx] for idx in range(len(v))]
#     squares = [diff ** 2 for diff in differences]
#     sum_of_squares = sum(squares)
#
#     return 1 / (1 + math.sqrt(sum_of_squares))

# print(movie_rows[0][1], movie_rows[0][0])
# print(movie_rows[1][1], movie_rows[1][0])
# print(movie_rows[2][1], movie_rows[2][0])
# print(movie_rows[3][1], movie_rows[3][0])

print(' The one', end=' ')
print(ratings[0][0])


def display_rated_movies():
    try:
        number_of_movies = int(input("How many movies would you like to view? "))
        minum_number_of_ratings = int(input("What's the minimum number of ratings? "))

    except ValueError:
        print("That's not a number!\n")

    else:
        print("RANK\tRATING\tTITLE")
        for i, movie in enumerate(ratings_rid.top_rated_movies(numbmer_of_movies, minum_number_of_ratings), start=1):
                print(i, "\t", movie.av_ratings, "\t", movie.title)

def main():

    display_rated_movies()

#print('in main')
#search_by_movie_id(1681)
#
if __name__ == '__main__':
    main()
