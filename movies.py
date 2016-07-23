import csv
import os

movie_rows =[]

with open('u.item', encoding='latin_1') as f:
    reader = csv.DictReader(f, fieldnames=['movie_id', 'movie_title', 'unknown', 'action'], delimiter='|')
    for row in reader:
        print(row)
        movie_rows.append(movie_rows)

class MOVIE:

    def __init__(self,movieid,movietitle,unknown,action):
        self.movieid = row[0]
        self.movietitle = row[1]
        # self.releasedate = row[2]
        # #self.idmb = idmb[3]
        # self.unknown = unknown[4]
        # self.action = action[5]





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
            #print(movies_rows[])
            # return '{}: {}'.format(self.movieid, self.movietitle, self.unknown, self.action)
