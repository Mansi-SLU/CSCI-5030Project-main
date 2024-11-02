# JoinSession.py
import client  # Import client functions from client.py

def join_session():
    print("Joining the game session...")
    client.send_message("A new player has joined the session.")

# Call join_session if running as a player
if __name__ == "__main__":
    join_session()
