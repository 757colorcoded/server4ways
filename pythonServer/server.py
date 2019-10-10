from http.server import HTTPServer, BaseHTTPRequestHandler
import argparse

class RequestHandler(BaseHTTPRequestHandler):
    def setResponseHeaders(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
    def createHTMLMessage(self, message):
        message = f"<html><body><p>{message}</p></body></html>"
        return message.encode("utf8")
    def do_GET(self):
        self.setResponseHeaders()
        self.wfile.write(self.createHTMLMessage("Welcome to python server"))

def runServer(serverClass = HTTPServer, handlerClass = RequestHandler, serverAddress="localhost", serverPort=8080):
    mainAddress = (serverAddress, serverPort)
    mainServer = serverClass(mainAddress, handlerClass)
    print(f"Starting server at {serverAddress}:{serverPort}")
    mainServer.serve_forever()

if __name__== "__main__":
    runServer()
