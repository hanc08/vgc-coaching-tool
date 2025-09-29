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
    return render_template('tutorial.html')

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
def level1():
    path = 'level1.html'
    levelName = 'level1'
    mon1 = "Urshifu"
    mon2 = "Miraidon"
    target1 = "Weezing"
    target2 = "Tatsugiri"
    switch1 = "Whimsicott"
    switch2 = "Incineroar"
    canOne = "cant"
    canTwo = "can"
    tera = "can"
    move1= "Surging Strikes"
    typeM1 = "water"
    move2 = "Close Combat"
    typeM2 = "fighting"
    move3 = "Aqua Jet"
    typeM3 = "water"
    move4 = "U-Turn"
    typeM4 = "bug"
    move5= "Electro Drift"
    typeM5 = "electric"
    move6 = "Draco Meteor"
    typeM6 = "dragon"
    move7 = "Volt Switch"
    typeM7 = "electric"
    move8 = "Dazzling Gleam"
    typeM8 = "fairy"
    replaySRC="https://replay.pokemonshowdown.com/gen9vgc2025regibo3-2410389774-lkdj5v33mo8n6jgngbqkwx9tsk9eht2pw?turn=10"
    return render_template(path, levelTitle = levelName, pokemon1 = mon1, pokemon2 = mon2, targetOne = target1,targetTwo = target2, switchOne = switch1,switchTwo  = switch2, can1 = canOne, can2 = canTwo, tera1 = tera,tera2 = tera,moveOne = move1,typeMove1 = typeM1,moveTwo = move2,typeMove2 =typeM2,moveThree = move3,typeMove3 = typeM3,moveFour = move4,typeMove4 = typeM4,moveFive = move5,typeMove5 = typeM5,moveSix = move6,typeMove6 = typeM6,moveSeven = move7,typeMove7 = typeM7,moveEight = move8,typeMove8 = typeM8, replay=replaySRC)