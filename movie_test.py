from movies import Movie

def test_create_movie_with_id_and_title():
    movie = Movie(1, 'Toy Story')
    assert movie.id == 1
    assert movie.title == 'Toy Story'


# def test_movies_have_ratings():
#     movie = Movie(1, 'Toy Story')
#     movie.add_rating(1234, 5.0)
#     assert len(movie.ratings) == 1
#     assert movie.ratings[0].user_id == 1234
#     assert movie.ratings[0].score == 5.0
#
# def test_find_movie_by_id():
#     movie = Movie.find_by_id(1)
#     assert movie.id == 1
#     assert movie.title == 'Toy Story'
