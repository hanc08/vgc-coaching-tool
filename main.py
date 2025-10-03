from flask import Blueprint, current_app, json, jsonify, render_template
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', email=current_user.email)

@main.route('/tutorial')
def tutorial():
    path = 'tutorial.html'
    levelName = 'tutorial'
    mon1 = "Ursaluna"
    mon2 = "Gholdengo"
    target1 = "Archaludon"
    target2 = "Sinistcha"
    switch1 = "Flamigo"
    switch2 = "Incineroar"
    canOne = "cant"
    canTwo = "cant"
    tera = "cant"
    move1= "Facade"
    typeM1 = "normal"
    move2 = "Headlong Rush"
    typeM2 = "ground"
    move3 = "Earthquake"
    typeM3 = "ground"
    move4 = "Protect"
    typeM4 = "normal"
    move5= "Make It Rain"
    typeM5 = "steel"
    move6 = "Shadow Ball"
    typeM6 = "ghost"
    move7 = "Nasty Plot"
    typeM7 = "dark"
    move8 = "Protect"
    typeM8 = "normal"
    replaySRC="https://replay.pokemonshowdown.com/gen9vgc2025regh-2451197018-g4n4vm0gt4ir286hlvpi3ax5n4erba1pw?turn=6"
    return render_template(path, levelTitle = levelName, pokemon1 = mon1, pokemon2 = mon2, targetOne = target1,targetTwo = target2, switchOne = switch1,switchTwo  = switch2, can1 = canOne, can2 = canTwo, tera1 = tera,tera2 = tera,moveOne = move1,typeMove1 = typeM1,moveTwo = move2,typeMove2 =typeM2,moveThree = move3,typeMove3 = typeM3,moveFour = move4,typeMove4 = typeM4,moveFive = move5,typeMove5 = typeM5,moveSix = move6,typeMove6 = typeM6,moveSeven = move7,typeMove7 = typeM7,moveEight = move8,typeMove8 = typeM8, replay=replaySRC)

@main.route('/data')
def data():
    """Return the answers.json file from the instance folder as JSON."""
    try:
        with current_app.open_instance_resource('answers.json', mode='r', encoding='utf-8') as f:
            return jsonify(json.load(f))
    except FileNotFoundError:
        return jsonify({"error": "answers.json not found"}), 404

@main.route('/levels')
@login_required
def levels():
    return render_template('levels.html')


@main.route('/level1')
@login_required
def level1():
    path = 'level1.html'
    levelName = 'level1'
    mon1 = "Charizard"
    mon2 = "Jumpluff"
    target1 = "Basculegion"
    target2 = "Pelipper"
    switch1 = "Porygon2"
    switch2 = "Torkoal"
    canOne = "cant"
    canTwo = "can"
    tera = "cant"
    move1= "Heat Wave"
    typeM1 = "fire"
    move2 = "Air Slash"
    typeM2 = "flying"
    move3 = "Overheat"
    typeM3 = "fire"
    move4 = "Weather Ball"
    typeM4 = "water"
    move5= "Sleep Powder"
    typeM5 = "grass"
    move6 = "Rage Powder"
    typeM6 = "bug"
    move7 = "Tailwind"
    typeM7 = "flying"
    move8 = "Sunny Day"
    typeM8 = "fire"
    replaySRC="https://replay.pokemonshowdown.com/gen9vgc2025regh-2454120667-2n0wldgvhbtcy2uv6f628b021ute7vbpw?turn=10"
    return render_template(path, levelTitle = levelName, pokemon1 = mon1, pokemon2 = mon2, targetOne = target1,targetTwo = target2, switchOne = switch1,switchTwo  = switch2, can1 = canOne, can2 = canTwo, tera1 = tera,tera2 = tera,moveOne = move1,typeMove1 = typeM1,moveTwo = move2,typeMove2 =typeM2,moveThree = move3,typeMove3 = typeM3,moveFour = move4,typeMove4 = typeM4,moveFive = move5,typeMove5 = typeM5,moveSix = move6,typeMove6 = typeM6,moveSeven = move7,typeMove7 = typeM7,moveEight = move8,typeMove8 = typeM8, replay=replaySRC)