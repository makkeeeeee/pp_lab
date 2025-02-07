# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

# 1. Check if a movie's score > 5.5
def good_score(mv):
    return mv["s"] > 5.5

# 2. Get movies with score > 5.5
def good_mvs(mvs):
    return [m for m in mvs if good_score(m)]

# 3. Get movies of a category
def cat_mvs(cat, mvs):
    return [m for m in mvs if m["c"] == cat]

# 4. Calc avg score of movies
def avg_score(mvs):
    if not mvs:
        return 0
    return sum(m["s"] for m in mvs) / len(mvs)

# 5. Calc avg score of a category
def cat_avg_score(cat, mvs):
    return avg_score(cat_mvs(cat, mvs))