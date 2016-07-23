import csv
import os

movie_rows = []
# with open('u.item.csv') as f:
#     fieldnames = ['movieid','movietitle','unknown', 'action']
#     reader = csv.reader(f)
#     headers = next(reader)
#     row = next(reader)
#     #print(row)
    #
#     for row in reader:
#         movie_rows = row(row)
#         movie_rows.append(movie_rows)
#         print(row)
# clear
    # print(movies_rows[])
    # return '{}: {}'.format(self.movieid, self.movietitle, self.unknown, self.action)


with open('ml-100k/u.item', encoding='latin_1') as f:
#with open('u.item', encoding='latin_1') as f:
    reader = csv.reader(f, delimiter='|')
    for row in reader:
        #print(row)
        movie_rows.append(row)
# print(movie_rows[:])
# print(movie_rows[1:6])
    #print(movie_rows[6][1])

user_id = []
with open('ml-100k/u.user', encoding = 'latin_1') as f:
    reader = csv.reader(f, delimiter = '|')
    for row in reader:
        #print(row)
        user_id.append(row)
#print(user_id[:])

ratings = []
with open('ml-100k/u.data', encoding = 'latin_1') as f:
    reader = csv.reader(f, delimiter = '|')
    for row in reader:
        #print(row)
        ratings.append(row)
print(ratings[:])


class Movie:

    def __init__(self, mid, title):
    #def __init__(self, mid, title, ratings, av_ratings):
        self.mid = mid
        self.title = title
        self.ratings = {}
        self.av_ratings = ""

    def __str__(self):
        return "{} Average Ratings = {} Ratings = {}". format(self.movietitle, self.avg_ratings, self.ratings)


    def create_movies_with_id_and_title(mid, movietitle, title, ratings, av_ratings):
        pass


class User:
    pass
    # def __init__(self, row):
    #     self.id = row[0]
    #     self.age = row[1]
    #     self.gender = row[3]

class Ratings:
    pass

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

print(movie_rows[0][1], movie_rows[0][0])
print(movie_rows[1][1], movie_rows[1][0])
print(movie_rows[2][1], movie_rows[2][0])
print(movie_rows[3][1], movie_rows[3][0])

# for i in range(len(ratings)):
#     print(ratings[i])
#     print('')
# count = 0
# for i in range(len(ratings)):
#     if 't1' in ratings[i]:
#         count = count + 1
# print(count)

#if __name__ == '__main__':
