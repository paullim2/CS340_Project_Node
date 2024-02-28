from flask import Flask, request

# dictionary of games data
games = [
    {"genre": "rpg", "title": "Final Fantasy XVI", "cost": "70", "length": "35", "platform": ["Playstation"], "image_name": "ffxvi.jpg"},
    {"genre": "rpg", "title": "Xenoblade Chronicles 3", "cost": "60", "length": "65", "platform": ["Nintendo Switch"], "image_name": "xbc.jpg"},
    {"genre": "rpg", "title": "Final Fantasy VII Ever Crisis", "cost": "Free", "length": "45", "platform": ["Mobile", "PC"], "image_name": "ffvii.jpg"},
    {"genre": "action-adventure", "title": "Red Dead Redemption 2", "cost": "60", "length": "50", "platform": ["Playstation", "Xbox", "PC"], "image_name": "rdr2.jpg"},
    {"genre": "action-adventure", "title": "The Legend of Zelda: Tears of the Kingdom", "cost": "70", "length": "60", "platform": ["Nintendo Switch"], "image_name": "totk.jpg"},
    {"genre": "action-adventure", "title": "Marvel's Spider-Man 2", "cost": "70", "length": "20", "platform": ["Playstation"], "image_name": "sm2.jpg"},
    {"genre": "adventure", "title": "Twisted Wonderland", "cost": "Free", "length":"100+", "platform": ["Mobile"], "image_name": "twst.jpg"},
    {"genre": "adventure", "title": "Kingdom Hearts III", "cost": "60", "length": "30", "platform": ["Playstation", "Xbox", "Nintendo Switch", "PC"], "image_name": "kh3.jpg"},
    {"genre": "adventure", "title": "Stray", "cost": "30", "length": "5", "platform": ["Playstation", "Xbox", "PC"], "image_name": "stray.jpg"},
    {"genre": "simulation", "title": "Stardew Valley", "cost": "15", "length": "100+", "platform": ["Nintendo Switch", "Playstation", "Xbox", "PC", "Mobile"], "image_name": "stardew.jpg"},
    {"genre": "simulation", "title": "Animal Crossing: New Horizons", "cost": "60", "length": "100+", "platform": ["Nintendo Switch"], "image_name": "anch.jpg"},
    {"genre": "simulation", "title": "Dredge", "cost": "25", "length": "10", "platform": ["Nintendo Switch", "Playstation", "Xbox", "PC"], "image_name": "dredge.jpg"},
    {"genre": "platform", "title": "Cuphead", "cost": "20", "length": "25", "platform": ["Nintendo Switch", "Playstation", "Xbox", "PC"], "image_name": "cuphead.jpg"},
    {"genre": "platform", "title": "Super Mario Odyssey", "cost": "60", "length": "15", "platform": ["Nintendo Switch"], "image_name": "mario.jpg"},
    {"genre": "platform", "title": "Sonic Mania", "cost": "20", "length": "5", "platform": ["Nintendo Switch", "Playstation", "Xbox", "PC"], "image_name": "sonic.jpg"}
]

# algorithm to recommend game based on input (a list in string form)
def recommend_game(input):
    for game in games:
        if game['genre'] == input[0] and game['length'] == input[1]:
            for platform in input[2]:
                if platform in game['platform']:
                    return str([game["title"], game["cost"], game["length"], game["platform"], game["image_name"]])
            return "No Match Found"
    return "No Match Found"




app = Flask(__name__)

@app.route('/')
def index():
    return open('vg_recommender.html').read()

@app.route('/submit', methods=['POST'])
def submit():
    genre = request.form['genre']
    length = request.form['length']
    platforms = request.form.getlist('platform')
    concatenated_string = [genre, length, platforms]
    recommended_game = recommend_game(concatenated_string)
    return recommended_game

if __name__ == '__main__':
    app.run(debug=True, port=8000)