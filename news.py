import socket
import requests
from flask import Flask 
from flask_cors import CORS
from fastapi import FastAPI
from Connect import Database
from Models.SourceModel import SourceModel
from Models.AuthorModel import AuthorModel
from Models.ArticleModel import ArticleModel
from Mappers.SourceMapper import SourceMapper
from Mappers.AuthorMapper import AuthorMapper
from Mappers.ArticleMapper import ArticleMapper


__ENDPoint = "https://raw.githubusercontent.com/AyushiChaudhary23/NewsData/main/db.json"

__SourceMapper = SourceMapper()
__AuthorMapper = AuthorMapper()
__ArticleMapper = ArticleMapper()

# class Server:
#     def __init__(self, HOST, PORT):
#         self. HOST = HOST
#         self._PORT = PORT
#         self._APIKey = ""
#         self._ENDPoint = ""
#         self._SourceMapper = SourceMapper()
#         self._AuthorMapper = AuthorMapper()
#         self._ArticleMapper = ArticleMapper()

#     def _initServer(self):
#         with socket.socket (socket.AF_INET, socket.SOCK_STREAM) as service_socket:
#             service_socket.bind((self._HOST, self._PORT))
#             service_socket.listen ()
#             print(f"Server is listening on {self._HOST}: {self. _PORT}.")
#             conn, addr = service_socket.accept ()
#             while True:
#                 response = conn.recv(1024).decode()
#                 print ("Response from Client:", response)
#                 if (response.lower() == "exit".lower()):
#                     conn.close ()
#                     print('Connection closed from:', addr)
#                 break


def _getDataFromApi(self) :
    # _uri = self._ENDPoint+"?access_key="+self._APIKey
    response = requests.get (__ENDPoint).json ()
    db = Database.getClassObject()
    db. connect()
    print("Database Connected to the Backend")
    self._SourceMapper.createTable()
    self._AuthorMapper.createTable()
    self._ArticleMapper.createTable()

    sourcemodelObj = SourceModel()
    authormodelObj = AuthorModel()
    articlemodelObj = ArticleModel()

    print(len(response["News"]))

    for item in response["News"]:
        for data in item["Sources"]:
            sourcemodelObj.set_source_id(data['Source_id'])
            sourcemodelObj.set_source_name(data['Source_name'])
            self._SourceMapper.insertRow(sourcemodelObj)
    for item in response ["News"]:
        for data in item["Authors"]:
            authormodelObj.set_author_id(data['Author_id'])
            authormodelObj.set_author_name(data['Author_name'])
            authormodelObj.set_Email(data['email'])
            authormodelObj.set_source_id(data['Source_id'])
            self._AuthorMapper.insertRow(authormodelObj)
    for item in response["News"]:
        for data in item["Articles"]:
            articlemodelObj.set_article_id(data['Article_id'])
            articlemodelObj.set_title(data['Title'])
            articlemodelObj.set_content(data['Content'])
            articlemodelObj.set_url(data['Url'])
            articlemodelObj.set_published_at(data['Published_at'])
            articlemodelObj.set_country(data['Country'])
            articlemodelObj.set_author_id(data['Author_id'])
            self._ArticleMapper.insertRow(articlemodelObj)
    print("Task Completed.....")
    while True:
        operation=""
        choice =0
        operation = input('Which Operation you want to perform? \n 1.Delete \n 2.Update \n 3.Search \n 4.Exit')
        if (operation == "Delete"):
            choice=input(" 1.Delete Article based on published date \n 2.Delete Article based on Article id")
            if choice == "1":
                Ddate = input("Enter the date for which you want to delete records : ")
                articlemodelObj.set_published_at(Ddate)
                self._ArticleMapper.deleteArticlebydateOperation(articlemodelObj)
            elif choice == "2":
                Aid = input("Enter the ID of which you want to delete the article : ")
                articlemodelObj.set_author_id(Aid)
                print(authormodelObj.author_id)
                self._ArticleMapper.deleteArticlebyidOperation(articlemodelObj)
            else:
                print("Wrong Choice entered")

        elif (operation == "Update"):
            choice = input(" 1.Update email of author based on author name \n 2.Update source for author based on author name")
            if choice == "1":
                Aname = input("Enter name of author for whom you want to change email : ")
                authormodelObj.set_author_name(Aname)
                email = input("Enter new email : ")
                authormodelObj.set_Email(email)
                self._AuthorMapper.UpdateEmailOperation(authormodelObj)
            elif choice == "2":
                Aname = input("Enter name of author for whom you want to change source : ")
                authormodelObj.set_author_name(Aname)
                Sname = input("Enter new source name : ")
                sourcemodelObj.set_source_name(Sname)
                self._AuthorMapper.UpdateSourceOperation(authormodelObj, sourcemodelObj)
            else:
                print("Wrong Choice entered")

        elif (operation == "Search"):
            choice=input(" 1.Search all Sources \n 2.Search all authors \n 3.Search all authors for a source \n 4.Search all Articles \n 5.Search Articles based on Author name \n 6.Search Articles based on Source name ")
            if choice == "1":
                self._SourceMapper.SearchOperation()
            elif choice == "2" :
                self._AuthorMapper.SearchAllOperation()
            elif choice == "3":
                Sname = input("Enter Source name for which you want to see authors : ")
                sourcemodelObj.set_source_name(Sname)
                self._AuthorMapper.SearchAuthorOperation(sourcemodelObj)
            elif choice == "4" :
                self._ArticleMapper.SearchAllOperation()
            elif choice == "5" :
                Aname = input("Enter name of author for whom you want to search articles : ")
                authormodelObj.set_author_name(Aname)
                self._ArticleMapper.SearchAuthorArticlesOperation(authormodelObj)
            elif choice == "6" :
                Sname = input("Enter source name for which you want to search articles : ")
                sourcemodelObj.set_source_name(Sname)
                self._ArticleMapper.SearchSourceArticlesOperation(sourcemodelObj)
            else:
                print("Wrong Choice entered")

        elif (operation == "Exit"):
            exit()

        else:
            print("Wrong Choice entered")


app = Flask(__name__)
CORS(app)

@app.route("/Sources")
def getAllSources():
    data = __SourceMapper.SearchOperation()
    respdata = {}
    for i in data:
        respdata[i[0]] = i
    return respdata


@app.route("/Authors")
def getAllAuthors():
    data = __AuthorMapper.SearchAllOperation()
    respdata = {}
    for i in data:
        respdata[i[0]] = i
    return respdata

@app.route("/Articles")
def getAllArticles():
    data = __ArticleMapper.SearchAllOperation()
    respdata = {}
    for i in data:
        respdata[i[0]] = i
    return respdata

@app.route("/Authors/<Source_name>")
def getAllAuthorsofSource(sourcemodelObj):
    data = __AuthorMapper.SearchAuthorOperation()
    respdata = {}
    for i in data:
        respdata[i[0]] = i
    return respdata

@app.route("/Authors/<Source_name>")
def getAllArticlesofAuthor(sourcemodelObj):
    data = __ArticleMapper.SearchAuthorArticlesOperation()
    respdata = {}
    for i in data:
        respdata[i[0]] = i
    return respdata


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
