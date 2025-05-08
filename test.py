from flask import Flask, session, redirect, url_for, request, render_template_string
import random

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Used to sign session cookies

# ---------------------------
# Global Data (Card Data)
# ---------------------------
computer_card = [
    "Keyboard", "Mouse", "Monitor", "FireFox", "CPU", 
    "GPU", "Google", "Gaming PC", "Supercomputer", "NASA's computer"
]

# Each card’s stats: [description, HP, attack, defense, rarity]
computer_card_stats = [
    ["Click clack", 50, 25, 5, "Normal"], 
    ["Click.", 75, 15, 5, "Normal"], 
    ["Shows stuff.", 100, 10, 10, "Normal"], 
    ["Browse.", 15, 15, 1.25, "Normal"], 
    ["Finishes tasks quickly but vulnerable.", 25, 35, 2.5, "Uncommon"], 
    ["Great for taking down groups.", 30, 10, 2.5, "Uncommon"], 
    ["Better than FireFox.", 50, 20, 2, "Uncommon"], 
    ["Gaming", 70, 30, 12.5, "Epic"], 
    ["Superfast.", 55, 35, 15, "Epic"],
    ["Um", 120, 70, 25, "Legendary"]
]

pack_names = ["Computer Pack"]
all_packs = [computer_card]
give_start = 4  # Number of cards given initially

# ---------------------------
# Routes
# ---------------------------
@app.route('/')
def index():
    # If the game hasn't been initialized, show the welcome page.
    if 'done_intro' not in session or not session['done_intro']:
        return render_template_string('''
            <h1>Welcome to Card Battle!</h1>
            <p>Find a friend to play with you.</p>
            <form action="{{ url_for('start_intro') }}" method="post">
                <button type="submit">Start Intro</button>
            </form>
        ''')
    else:
        return redirect(url_for('menu'))

@app.route('/start_intro', methods=['POST'])
def start_intro():
    # Reset any previous session data and begin the introduction.
    session.clear()
    session['done_intro'] = False
    return redirect(url_for('intro1'))

# Intro step 1
@app.route('/intro1', methods=['GET', 'POST'])
def intro1():
    if request.method == 'POST':
        return redirect(url_for('intro2'))
    return render_template_string('''
        <h2>Welcome to Card Battle!</h2>
        <p>Find a friend to play with you.</p>
        <form method="post">
            <button type="submit">Continue</button>
        </form>
    ''')

# Intro step 2
@app.route('/intro2', methods=['GET', 'POST'])
def intro2():
    if request.method == 'POST':
        return redirect(url_for('intro3'))
    return render_template_string('''
        <h2>Decide Player Roles</h2>
        <p>Now decide who will be Player 1 and who will be Player 2.</p>
        <form method="post">
            <button type="submit">Continue</button>
        </form>
    ''')

# Intro step 3: Explain card distribution and deal the cards.
@app.route('/intro3', methods=['GET', 'POST'])
def intro3():
    if request.method == 'POST':
        # Deal cards to both players.
        p1_cards = []
        p2_cards = []
        for i in range(give_start):
            which_pack = random.choice(all_packs)
            random_num = random.randint(1, 100)
            if 1 <= random_num <= 60:
                whichcard = random.randint(0, 3)
            elif 61 <= random_num <= 90:
                whichcard = random.randint(4, 7)
            elif 91 <= random_num <= 99:
                whichcard = random.randint(8, 9)
            elif random_num == 100:
                whichcard = 9
            p1_cards.append(which_pack[whichcard])
        
        for i in range(give_start):
            which_pack = random.choice(all_packs)
            random_num = random.randint(1, 100)
            if 1 <= random_num <= 60:
                whichcard = random.randint(0, 3)
            elif 61 <= random_num <= 90:
                whichcard = random.randint(4, 7)
            elif 91 <= random_num <= 99:
                whichcard = random.randint(8, 9)
            elif random_num == 100:
                whichcard = 9
            p2_cards.append(which_pack[whichcard])
        
        session['p1_cards'] = p1_cards
        session['p2_cards'] = p2_cards
        session['p1_coins'] = 50
        session['p2_coins'] = 50
        session['done_intro'] = True
        return redirect(url_for('intro_result'))
    return render_template_string('''
        <h2>Card Distribution</h2>
        <p>Player 1 and Player 2, you will both receive 4 random cards.</p>
        <form method="post">
            <button type="submit">Deal Cards</button>
        </form>
    ''')

# Show the result of the intro (the dealt cards).
@app.route('/intro_result')
def intro_result():
    p1_cards = session.get('p1_cards', [])
    p2_cards = session.get('p2_cards', [])
    return render_template_string('''
        <h2>Cards Dealt!</h2>
        <p>Player 1 received: {{ p1_cards|join(", ") }}</p>
        <p>Player 2 received: {{ p2_cards|join(", ") }}</p>
        <a href="{{ url_for('menu') }}">Continue to Menu</a>
    ''', p1_cards=p1_cards, p2_cards=p2_cards)

# ---------------------------
# Main Menu
# ---------------------------
@app.route('/menu', methods=['GET', 'POST'])
def menu():
    if request.method == 'POST':
        option = request.form.get('option')
        if option == "1":
            # "Play" mode is not yet implemented.
            return render_template_string('''
                <h2>Play</h2>
                <p>Play mode is not implemented yet.</p>
                <a href="{{ url_for('menu') }}">Back to Menu</a>
            ''')
        elif option == "2":
            return redirect(url_for('choose_deck'))
        elif option == "3":
            return redirect(url_for('get_more_cards'))
    return render_template_string('''
        <h2>Main Menu</h2>
        <form method="post">
            <button type="submit" name="option" value="1">1. Play</button><br><br>
            <button type="submit" name="option" value="2">2. View your deck</button><br><br>
            <button type="submit" name="option" value="3">3. Get more cards</button>
        </form>
        <br>
        <a href="{{ url_for('restart') }}">Restart Game / Go Back to Intro</a>
    ''')

# ---------------------------
# View Deck
# ---------------------------
@app.route('/choose_deck', methods=['GET', 'POST'])
def choose_deck():
    if request.method == 'POST':
        player = request.form.get('player')
        if player in ['1', '2']:
            return redirect(url_for('view_deck', player_id=player))
    return render_template_string('''
        <h2>View Deck</h2>
        <form method="post">
            <label>Select Player:</label>
            <select name="player">
                <option value="1">Player 1</option>
                <option value="2">Player 2</option>
            </select>
            <button type="submit">View Deck</button>
        </form>
        <br>
        <a href="{{ url_for('menu') }}">Back to Menu</a>
    ''')

@app.route('/deck/<player_id>', methods=['GET'])
def view_deck(player_id):
    if player_id == "1":
        cards = session.get('p1_cards', [])
    elif player_id == "2":
        cards = session.get('p2_cards', [])
    else:
        cards = []
    return render_template_string('''
        <h2>Player {{ player_id }}'s Deck</h2>
        {% if cards %}
            <ul>
            {% for card in cards %}
                <li>
                    {{ card }} 
                    (<a href="{{ url_for('card_stats', player_id=player_id, card_name=card) }}">View Stats</a>)
                </li>
            {% endfor %}
            </ul>
        {% else %}
            <p>No cards available.</p>
        {% endif %}
        <a href="{{ url_for('menu') }}">Back to Menu</a>
    ''', player_id=player_id, cards=cards)

@app.route('/card/<player_id>/<card_name>', methods=['GET'])
def card_stats(player_id, card_name):
    if card_name in computer_card:
        index = computer_card.index(card_name)
        card = computer_card_stats[index]
        return render_template_string('''
            <h2>{{ card_name }} Stats</h2>
            <p><strong>Info:</strong> {{ card[0] }}</p>
            <p><strong>HP:</strong> {{ card[1] }}</p>
            <p><strong>Attack:</strong> {{ card[2] }}</p>
            <p><strong>Defense:</strong> {{ card[3] }}</p>
            <p><strong>Rarity:</strong> {{ card[4] }}</p>
            <a href="{{ url_for('view_deck', player_id=player_id) }}">Back to Deck</a>
        ''', card_name=card_name, card=card, player_id=player_id)
    else:
        return render_template_string('''
            <h2>Error</h2>
            <p>Invalid card.</p>
            <a href="{{ url_for('view_deck', player_id=player_id) }}">Back to Deck</a>
        ''', player_id=player_id)

# ---------------------------
# Get More Cards
# ---------------------------
@app.route('/get_more_cards', methods=['GET', 'POST'])
def get_more_cards():
    if request.method == 'POST':
        player = request.form.get('player')
        pack = request.form.get('pack')
        # Deal one new random card (using the same logic as before)
        which_pack = random.choice(all_packs)
        random_num = random.randint(1, 100)
        if 1 <= random_num <= 60:
            whichcard = random.randint(0, 3)
        elif 61 <= random_num <= 90:
            whichcard = random.randint(4, 7)
        elif 91 <= random_num <= 99:
            whichcard = random.randint(8, 9)
        elif random_num == 100:
            whichcard = 9
        new_card = which_pack[whichcard]
        
        if player == "1":
            p1_cards = session.get('p1_cards', [])
            p1_cards.append(new_card)
            session['p1_cards'] = p1_cards
        elif player == "2":
            p2_cards = session.get('p2_cards', [])
            p2_cards.append(new_card)
            session['p2_cards'] = p2_cards
        
        return render_template_string('''
            <h2>New Card Acquired!</h2>
            <p>Player {{ player }} received: {{ new_card }}</p>
            <a href="{{ url_for('menu') }}">Back to Menu</a>
        ''', player=player, new_card=new_card)
        
    return render_template_string('''
        <h2>Get More Cards</h2>
        <form method="post">
            <label>Select Player:</label>
            <select name="player">
                <option value="1">Player 1</option>
                <option value="2">Player 2</option>
            </select><br><br>
            <label>Select Pack:</label>
            <select name="pack">
                {% for pack in pack_names %}
                <option value="{{ pack }}">{{ pack }}</option>
                {% endfor %}
            </select><br><br>
            <button type="submit">Get Card</button>
        </form>
        <br>
        <a href="{{ url_for('menu') }}">Back to Menu</a>
    ''', pack_names=pack_names)

# ---------------------------
# Restart Route
# ---------------------------
@app.route('/restart', methods=['GET'])
def restart():
    session.clear()  # Clears all session data, including the intro flag and cards.
    return redirect(url_for('intro1'))

# ---------------------------
# Run the App
# ---------------------------
if __name__ == '__main__':
    app.run(debug=True)
