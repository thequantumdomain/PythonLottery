import requests
import sqlite3
import time
from collections import defaultdict

def fetch_random_users(size):
    url = "https://random-data-api.com/api/users/random_user"
    params = {"size": size}
    response = requests.get(url, params=params)
    return response.json()

def init_db():
    conn = sqlite3.connect('winners.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS winner
                      (id INTEGER PRIMARY KEY, email TEXT, state TEXT UNIQUE)''')
    conn.commit()
    return conn

def update_winner(conn, user_data):
    cursor = conn.cursor()
    cursor.execute('''INSERT OR REPLACE INTO winner (id, email, state) VALUES (?, ?, ?)''',
                   (user_data['id'], user_data['email'], user_data['address']['state']))
    conn.commit()
    print(f"Updated winner table: {user_data['email']} from {user_data['address']['state']} added.")

def main():
    conn = init_db()
    unique_states = set()

    print("Starting lottery system...")
    while len(unique_states) < 25:
        users = fetch_random_users(5)
        for user in users:
            state = user['address']['state']
            if state not in unique_states:
                update_winner(conn, user)
                unique_states.add(state)
                print(f"New winner from {state}: {user['email']}")

        time.sleep(10)  # Wait for 10 seconds before fetching again

    # Fetch and print final winners from the database
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM winner")
    winners = cursor.fetchall()
    print("\nFinal Winners:")
    for winner in winners:
        print(winner)

    conn.close()

if __name__ == "__main__":
    main()
