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
        while True:
            operation=""
            choice =0
            operation = input('Which Operation you want to perform? \n 1.Delete \n 2.Update \n 3.Search')
            if (operation == "Delete"):
                choice=input("1. Delete Article based on published date \n 2.Delete Article based on Article id")
                self._ArticleMapper.deleteOperation(choice)

            elif (operation == "Update"):
                choice = input("1. Update email of author based on author name \n 2.Update source for author based on author name")
                self._AuthorMapper.UpdateOperation(choice)

            elif (operation == "Search"):
                choice=input("1.Search all Sources \n 2.Search all authors \n 3.Search all authors for a source \n 4. Search all Articles \n 5.Search Articles based on Author name \n 6.Search Articles based on Source name ")
                if choice == "1":
                    self._SourceMapper.SearchOperation()
                elif choice == "2" or choice == "3":
                    self._AuthorMapper.SearchOperation(choice)
                elif choice == "4" or choice == "5" or choice == "6" :
                    self._ArticleMapper.SearchOperation(choice)
                else:
                    print("Wrong Choice entred")

            else:
                print("Wrong Choice entred")








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
