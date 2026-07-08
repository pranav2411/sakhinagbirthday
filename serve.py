import http.server
import socketserver
import os

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class BirthdayServerHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        # Initialize with the project directory
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        # Map root path and index.html requests to serve index.html
        if self.path == '/' or self.path == '/index.html':
            self.path = '/index.html'
        return super().do_GET()

if __name__ == '__main__':
    # Print welcome banner
    print("==================================================")
    print("       💖 HAPPY BIRTHDAY SAKHI SERVER 💖        ")
    print("==================================================")
    print(f"Starting local server at http://localhost:{PORT}")
    print("Keep this window open while using the website.")
    print("Press Ctrl+C to stop the server.")
    print("==================================================")

    # Allow port reuse immediately after closing the server
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), BirthdayServerHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nStopping birthday server. Goodbye! 👋")
