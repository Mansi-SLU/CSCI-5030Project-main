#This will basically be responsible for transferring information back and forth to each player
import client
def update_game_state(state):
    # Send updated game state to server
    client.send_message(f"Update: {state}")