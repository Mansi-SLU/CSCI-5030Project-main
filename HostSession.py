# HostSession.py
import threading
import server  # Import server setup from server.py

def start_host_session():
    # Start server in a new thread to avoid blocking
    server_thread = threading.Thread(target=server.start_server)
    server_thread.start()
    print("Game server is running...")

# Call start_host_session if running as host
if __name__ == "__main__":
    start_host_session()
