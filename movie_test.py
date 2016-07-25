from movies_lib20 import Movie
from movies_lib20 import User
from movies_lib20 import Ratings

def test_create_movie_with_id_and_title():
    movie1 = Movie(1, "Toy Story")
    movie2 = Movie(2, "Die Hard")
    assert movie1.mid == 1
    assert movie1.title == "Toy Story"
    assert movie2.mid == 2
    assert movie2.title == "Die Hard"
    #assert movie1.ratings == 3
    #assert movie1.av_ratings == 4

def test_search_by_movie_id():
    movie = Movie(1, "Toy Story")
    assert movie.mid == 1
    assert movie.title == "Toy Story"

def test_create_user():
    user1 = User(1, 'Female')
    user2 = User(2, "Male")
    assert user1.uid == 1
    assert user1.gender == 'Female'
    assert user2.uid == 2
    assert user2.gender == 'Male'


def test_rating_stars():
    ratings1 = Ratings(1)
    ratings2 = Ratings(2)
    ratings3 = Ratings(3)
    ratings4 = Ratings(4)
    assert ratings1.ratings_rid == 1
    assert ratings2.ratings_rid == 2
    assert ratings3.ratings_rid == 3
    assert ratings4.ratings_rid == 4

def test_search_ratings_by_user():
    ratings1 = Ratings(1)
    user1 = User(3, 'Female')
    assert ratings1.ratings_rid == 1
    assert user1.uid == 3

    

# def test_movies_have_ratings():
#     movie = Movie(1, 'Toy Story')
#     movie.add_rating(1234, 5.0)
#     assert len(movie.ratings) == 1
#     assert movie.ratings[0].user_id == 1234
#     assert movie.ratings[0].score == 5.0
#
