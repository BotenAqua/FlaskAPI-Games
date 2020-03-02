from flask import Flask, jsonify, abort, make_response

app = Flask(__name__)

games = [
    {
        'ID': 1,
        'title': 'Half_Life_3',
        'Steam': True,
        'DRM-Free': False,
        'other DRM': False,
        'box': False
    },
    {
        'ID': 2,
        'title': 'Deep_Rock_Galactic',
        'Steam': True,
        'DRM-Free': False,
        'other DRM': False,
        'box': False
    }
]

@app.route('/library/api/v0.1/games', methods=['GET'])
def get_tasks():
    return jsonify({'games': games})

@app.route('/library/api/v0.1/games/<title>')
def get_game(title):
    game = [game for game in games if game['title'].lower() == title.lower()]
    if not game:
        abort(404)
    return jsonify({'game': game})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/library/api/v0.1/games', methods=['POST'])
def add_game():
    #ToDo
    return

if __name__ == '__main__':
    app.run(debug=True)
