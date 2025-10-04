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
    notes = "Note: Opponent has used tera"
    replaySRC="https://replay.pokemonshowdown.com/gen9vgc2025regh-2451197018-g4n4vm0gt4ir286hlvpi3ax5n4erba1pw?turn=6"
    return render_template(path, levelTitle = levelName, pokemon1 = mon1, pokemon2 = mon2, targetOne = target1,targetTwo = target2, switchOne = switch1,switchTwo  = switch2, can1 = canOne, can2 = canTwo, tera1 = tera,tera2 = tera,moveOne = move1,typeMove1 = typeM1,moveTwo = move2,typeMove2 =typeM2,moveThree = move3,typeMove3 = typeM3,moveFour = move4,typeMove4 = typeM4,moveFive = move5,typeMove5 = typeM5,moveSix = move6,typeMove6 = typeM6,moveSeven = move7,typeMove7 = typeM7,moveEight = move8,typeMove8 = typeM8, Notes = notes, replay=replaySRC)

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
    notes = "Note: Opponent has used tera"
    replaySRC="https://replay.pokemonshowdown.com/gen9vgc2025regh-2454120667-2n0wldgvhbtcy2uv6f628b021ute7vbpw?turn=10"
    return render_template(path, levelTitle = levelName, pokemon1 = mon1, pokemon2 = mon2, targetOne = target1,targetTwo = target2, switchOne = switch1,switchTwo  = switch2, can1 = canOne, can2 = canTwo, tera1 = tera,tera2 = tera,moveOne = move1,typeMove1 = typeM1,moveTwo = move2,typeMove2 =typeM2,moveThree = move3,typeMove3 = typeM3,moveFour = move4,typeMove4 = typeM4,moveFive = move5,typeMove5 = typeM5,moveSix = move6,typeMove6 = typeM6,moveSeven = move7,typeMove7 = typeM7,moveEight = move8,typeMove8 = typeM8, Notes = notes, replay=replaySRC)

@main.route('/level2')
@login_required
def level2():
    path = 'level2.html'
    levelName = 'level2'
    mon1 = "Porygon2"
    mon2 = "Incineroar"
    target1 = "Baxcalibur"
    target2 = "Sneasler"
    switch1 = "Torkoal"
    switch2 = "Ursaluna"
    canOne = "cant"
    canTwo = "cant"
    tera = "cant"
    move1= "Tera Blast"
    typeM1 = "fighting"
    move2 = "Ice Beam"
    typeM2 = "ice"
    move3 = "Recover"
    typeM3 = "normal"
    move4 = "Trick Room"
    typeM4 = "psychic"
    move5= "Fake Out"
    typeM5 = "normal"
    move6 = "Flare Blitz"
    typeM6 = "fire"
    move7 = "Knock Off"
    typeM7 = "dark"
    move8 = "Parting Shot"
    typeM8 = "dark"
    notes = "Note: Opponent has used tera. Both Incineroar and Sneasler are on the field for the first time."
    replaySRC="https://replay.pokemonshowdown.com/gen9vgc2025regh-2454673942-dnccwpk8k2dvckxfomrwa9xvl67jyaupw?turn=5"
    return render_template(path, levelTitle = levelName, pokemon1 = mon1, pokemon2 = mon2, targetOne = target1,targetTwo = target2, switchOne = switch1,switchTwo  = switch2, can1 = canOne, can2 = canTwo, tera1 = tera,tera2 = tera,moveOne = move1,typeMove1 = typeM1,moveTwo = move2,typeMove2 =typeM2,moveThree = move3,typeMove3 = typeM3,moveFour = move4,typeMove4 = typeM4,moveFive = move5,typeMove5 = typeM5,moveSix = move6,typeMove6 = typeM6,moveSeven = move7,typeMove7 = typeM7,moveEight = move8,typeMove8 = typeM8, Notes = notes, replay=replaySRC)

@main.route('/level3')
@login_required
def level3():
    path = 'level3.html'
    levelName = 'level3'
    mon1 = "Ursaluna"
    mon2 = "Sinistcha"
    target1 = "Sneasler"
    target2 = "Gholdengo"
    switch1 = "Archaludon"
    switch2 = "Gholdengo"
    canOne = "cant"
    canTwo = "can"
    tera = "cant"
    move1= "Facade"
    typeM1 = "normal"
    move2 = "Headlong Rush"
    typeM2 = "ground"
    move3 = "Earthquake"
    typeM3 = "ground"
    move4 = "Protect"
    typeM4 = "normal"
    move5= "Matcha Gotcha"
    typeM5 = "grass"
    move6 = "Rage Powder"
    typeM6 = "bug"
    move7 = "Life Dew"
    typeM7 = "water"
    move8 = "Trick Room"
    typeM8 = "psychic"
    notes = "Note: Gholdengo can use protect."
    replaySRC="https://replay.pokemonshowdown.com/gen9vgc2025regh-2454724809-7w3kle4q4aw76cnv1b7wio1prlestr4pw?turn=7"
    return render_template(path, levelTitle = levelName, pokemon1 = mon1, pokemon2 = mon2, targetOne = target1,targetTwo = target2, switchOne = switch1,switchTwo  = switch2, can1 = canOne, can2 = canTwo, tera1 = tera,tera2 = tera,moveOne = move1,typeMove1 = typeM1,moveTwo = move2,typeMove2 =typeM2,moveThree = move3,typeMove3 = typeM3,moveFour = move4,typeMove4 = typeM4,moveFive = move5,typeMove5 = typeM5,moveSix = move6,typeMove6 = typeM6,moveSeven = move7,typeMove7 = typeM7,moveEight = move8,typeMove8 = typeM8, Notes = notes, replay=replaySRC)

@main.route('/level4')
@login_required
def level4():
    path = 'level4.html'
    levelName = 'level4'
    mon1 = "Gholdengo"
    mon2 = "Dragonite"
    target1 = "Ursaluna"
    target2 = "Sneasler"
    switch1 = "Ursaluna"
    switch2 = "Incineroar"
    canOne = "cant"
    canTwo = "can"
    tera = "cant"
    move1= "Make It Rain"
    typeM1 = "steel"
    move2 = "Shadow Ball"
    typeM2 = "ghost"
    move3 = "Nasty Plot"
    typeM3 = "dark"
    move4 = "Protect"
    typeM4 = "normal"
    move5= "Low Kick"
    typeM5 = "fighting"
    move6 = "Extreme Speed"
    typeM6 = "normal"
    move7 = "Stomping Tantrum"
    typeM7 = "ground"
    move8 = "Tera Blast"
    typeM8 = "normal"
    notes = "Note: Sneasler & Ursaluna can protect."
    replaySRC="https://replay.pokemonshowdown.com/gen9vgc2025reghbo3-2454813993-v1cp3x8hlg6epmb6ey3xjre8c4cioobpw?turn=5"
    return render_template(path, levelTitle = levelName, pokemon1 = mon1, pokemon2 = mon2, targetOne = target1,targetTwo = target2, switchOne = switch1,switchTwo  = switch2, can1 = canOne, can2 = canTwo, tera1 = tera,tera2 = tera,moveOne = move1,typeMove1 = typeM1,moveTwo = move2,typeMove2 =typeM2,moveThree = move3,typeMove3 = typeM3,moveFour = move4,typeMove4 = typeM4,moveFive = move5,typeMove5 = typeM5,moveSix = move6,typeMove6 = typeM6,moveSeven = move7,typeMove7 = typeM7,moveEight = move8,typeMove8 = typeM8, Notes = notes, replay=replaySRC)

@main.route('/level5')
@login_required
def level5():
    path = 'level5.html'
    levelName = 'level5'
    mon1 = "Gholdengo"
    mon2 = "Whimsicott"
    target1 = "Volcarona"
    target2 = "Basculegion"
    switch1 = "Ursaluna"
    switch2 = "Archaludon"
    canOne = "cant"
    canTwo = "cant"
    tera = "cant"
    move1= "Make It Rain"
    typeM1 = "steel"
    move2 = "Shadow Ball"
    typeM2 = "ghost"
    move3 = "Power Gem"
    typeM3 = "rock"
    move4 = "Trick"
    typeM4 = "psychic"
    move5= "Tailwind"
    typeM5 = "flying"
    move6 = "Moonblast"
    typeM6 = "fairy"
    move7 = "Encore"
    typeM7 = "normal"
    move8 = "Fake Tears"
    typeM8 = "dark"
    notes = "Note: Volcarona just used Quiver Dance. \n Opponent does not have tera"
    replaySRC="https://replay.pokemonshowdown.com/gen9vgc2025reghbo3-2454818681-3ppmdhfismwfwx2ixqs6juwqqyr07o9pw?turn=5"
    return render_template(path, levelTitle = levelName, pokemon1 = mon1, pokemon2 = mon2, targetOne = target1,targetTwo = target2, switchOne = switch1,switchTwo  = switch2, can1 = canOne, can2 = canTwo, tera1 = tera,tera2 = tera,moveOne = move1,typeMove1 = typeM1,moveTwo = move2,typeMove2 =typeM2,moveThree = move3,typeMove3 = typeM3,moveFour = move4,typeMove4 = typeM4,moveFive = move5,typeMove5 = typeM5,moveSix = move6,typeMove6 = typeM6,moveSeven = move7,typeMove7 = typeM7,moveEight = move8,typeMove8 = typeM8, Notes = notes, replay=replaySRC)