from http.server import SimpleHTTPRequestHandler, HTTPServer
import webbrowser

def start_home_page_server(port=1000):
    # HTML content for the home page with CSS styles
    home_page_content = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>welcome to Dine Tech</title>
        <style>
            body {
                font-family: "Comic Sans MS", cursive, sans-serif;
                background: url("https://images.pexels.com/photos/616401/pexels-photo-616401.jpeg?cs=srgb&dl=pexels-lukas-616401.jpg&fm=jpg") no-repeat center center fixed;
                background-size: cover;
                text-align: center;
                margin: 50px;
                color: purple;
            }
            h1 {
                color: purple;
            }
            p {
                font-size: 18px;
                color: #333;
            }
            ul {
                list-style-type: none;
                padding: 0;
            }
            li {
                display: inline-block;
                margin: 10px;
            }
            a {
                display: block;
                padding: 10px 20px;
                text-decoration: none;
                color: #fff;
                background-color: #28a745; /* Green color */
                border-radius: 5px;
            }
            a:hover {
                background-color: #218838; /* Darker green color on hover */
            }
        </style>
    </head>
    <body>
        <h1>Welcome to DineTech</h1>
        <p>You are:</p>
        <ul>
            <li><a href="/customer">Customer</a></li>
            <li><a href="/restaurant">Restaurant</a></li>
        </ul>
    </body>
    </html>
    '''

    # Define the handler to serve the HTML content
    class RequestHandler(SimpleHTTPRequestHandler):
        def do_GET(self):
            if self.path == '/customer':
                self.send_response(301)
                self.send_header('Location', 'http://localhost:2000/')  # Replace with the actual user webpage URL
                self.end_headers()
            elif self.path == '/restaurant':
                self.send_response(301)
                self.send_header('Location', 'http://localhost:10000/')  # Replace with the actual restaurant webpage URL
                self.end_headers()
            else:
                # Serve the home page content
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(home_page_content.encode())

    # Create the server
    server = HTTPServer(('localhost', port), RequestHandler)
    webbrowser.open_new_tab(f'http://localhost:{port}/')

    # Start serving
    server.serve_forever()

if __name__ == '__main__':
    start_home_page_server()
