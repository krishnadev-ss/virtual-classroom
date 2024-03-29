import threading
import test2 as ts
import ui as uk

if __name__ == "__main__":
    mouse_thread = threading.Thread(target=ts.mouse)
    mouse_thread.daemon = True
    mouse_thread.start()

    uk.open_landing_page()
