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
        self._SourceMapper = SourceMapper ()
        self._AuthorMapper = AuthorMapper ()
        self._ArticleMapper = ArticleMapper ()

    def _initServer(self):
        with socket.socket (socket.AF_INET, socket.SOCK_STREAM) as service_socket:
            service_socket.bind((self._HOST, self._PORT)) 
            service_socket.listen () 
            print(f"Server is listening on {self._HOST}: {self. _PORT}.")
            conn, addr = service_socket.accept ()
            while True:
                response = conn.recv (1024).decode ()
                print ("Response from Client:", response) 
                if (response.lower () == "exit". lower ()):
                    conn.close ()
                    print('Connection closed from:', addr)
                break
    def _getDataFromApi(self) :
        _uri = self._ENDPoint+"?access_key="+self._APIKey
        response = requests.get ("https://raw.githubusercontent.com/Utsav-Virani/DataSet/main/APIRes.json").json ()
        db = Database.getClassInstance ()
        db. connect ()
        print("Database Connected to the Backnd")
        self._SourceMapper.create ()
        self._AuthorMapper.create ()
        self._ArticleMapper.create ()
        print(len (response ["data"]))
        for item in response["data"]:
            if type(item) is dict and "book _details" in item.keys ():
                self._SourceMapper.insert (item ["book_details"])
        for item in response ["data"]:
            if type(item) is dict and "reviews" in item.keys():
                self._AuthorMapper.insert (item["reviews"])
        for item in response["data"]:
            if type(item) is dict and "product" in item.keys ():
                book_id = self._bookMapper.selectDataFromTitle (params="id", title=item["book_details"]["title"]) [0]
                review_id = self._reviewMapper.selectDataFromName(params="id", reviewer_name=item ["reviews"] ["reviewer_name"]) [0] 
                if bool(book_id) and bool(review_id):
                    self._productMapper.insert (item['product'], book_id, review_id)
        print("Task Completed.....")
    def serverInfo(self):
        print(f" [SERVER-STARTED-LISTENING] Server is available on {self._HOST}: {self._PORT}.")

def main():
    HOST = "127.0.0.1"
    PORT = 65432
    server0bject = Server(HOST, PORT)
    # serverObject._initServer()
    serverObject._getDataFromApi()


if name == '__main__':
    main()
