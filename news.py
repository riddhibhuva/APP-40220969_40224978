import socket
import requests
import json
from SourceMapper import SourceMapper
from AuthorMapper import AuthorMapper
from ArticleMapper import ArticleMapper
from Connect import Database


class Server:
    def __init__(self, HOST, PORT):
        self. HOST = HOST
        self._PORT = PORT
        self._APIKey = ""
        self._ENDPoint = ""
        self._SourceMapper = SourceMapper()
        self._AuthorMapper = AuthorMapper()
        self._ArticleMapper = ArticleMapper()

    def _initServer(self):
        with socket.socket (socket.AF_INET, socket.SOCK_STREAM) as service_socket:
            service_socket.bind((self._HOST, self._PORT))
            service_socket.listen ()
            print(f"Server is listening on {self._HOST}: {self. _PORT}.")
            conn, addr = service_socket.accept ()
            while True:
                response = conn.recv(1024).decode()
                print ("Response from Client:", response)
                if (response.lower() == "exit".lower()):
                    conn.close ()
                    print('Connection closed from:', addr)
                break

    def _getDataFromApi(self) :
        _uri = self._ENDPoint+"?access_key="+self._APIKey
        response = requests.get ("https://raw.githubusercontent.com/AyushiChaudhary23/NewsData/main/db.json").json ()
        db = Database.getClassObject()
        db. connect()
        print("Database Connected to the Backend")
        self._SourceMapper.createTable()
        self._AuthorMapper.createTable()
        self._ArticleMapper.createTable()
        print(len(response["News"]))
        for item in response["News"]:
            if type(item) is dict and "Sources" in item.keys():
                self._SourceMapper.insertRow(item ["Sources"])
        for item in response ["News"]:
            if type(item) is dict and "Authors" in item.keys():
                self._AuthorMapper.insertRow(item["Authors"])
        for item in response["News"]:
            if type(item) is dict and "Articles" in item.keys():
                self._ArticleMapper.insertRow(item["Articles"])
        print("Task Completed.....")

    def serverInfo(self):
        print(f" Server up and listening on {self._HOST}: {self._PORT}.")

def main():
    HOST = "127.0.0.1"
    PORT = 65432
    server0bject = Server(HOST, PORT)
    # serverObject._initServer()
    server0bject._getDataFromApi()


if __name__ == "__main__":
    main()
