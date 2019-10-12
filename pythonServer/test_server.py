import requests
import os

routes = ["/"]
url = os.getenv("url_server", default="http://localhost:8080")
 
def test_routes():
    for r in routes:
        req = requests.get(url)
        assert req.status_code == 200, "Erro in route {}".format(r)
if __name__ == "__main__":
    test_routes()
    print("Everything passed")