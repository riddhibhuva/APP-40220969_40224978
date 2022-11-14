import socket
import requests
import json
from ChannelMapper import ChannelMapper
from ReporterMapper import ReporterMapper
from ArticleMapper import ArticleMapper
from Connect import Database
from ChannelModel import ChannelModel
from ReporterModel import ReporterModel
from ArticleModel import ArticleModel
from fastapi import FastAPI


class Server:
    def __init__(self, HOST, PORT):
        self.HOST = HOST
        self._PORT = PORT
        self._APIKey = ""
        self._ENDPoint = ""
        self._ChannelMapper = ChannelMapper()
        self._ReporterMapper = ReporterMapper()
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
        self._ChannelMapper.createTable()
        self._ReporterMapper.createTable()
        self._ArticleMapper.createTable()

        # channelmodelObj = ChannelModel()
        # reportermodelObj = ReporterModel()
        # articlemodelObj = ArticleModel()


        print(len(response["News"]))

        for item in response["News"]:
            for data in item["Channel"]:  #Call all set methods inside constructors and pass the data object in the constructor
                # channelmodelObj.set_channel_id(data['Channel_id'])
                # channelmodelObj.set_channel_name(data['Channel_name'])
                channelmodelObj = ChannelModel(data)
                self._ChannelMapper.insertRow(channelmodelObj)

        for item in response ["News"]:
            for data in item["Reporters"]:
                # reportermodelObj.set_reporter_id(data['Reporter_id'])
                # reportermodelObj.set_reporter_name(data['Reporter_name'])
                # reportermodelObj.set_Email(data['email'])
                # reportermodelObj.set_channel_id(data['Channel_id'])
                reportermodelObj = ReporterModel(data)
                self._ReporterMapper.insertRow(reportermodelObj)

        for item in response["News"]:
            for data in item["Articles"]:
                # articlemodelObj.set_article_id(data['Article_id'])
                # articlemodelObj.set_title(data['Title'])
                # articlemodelObj.set_content(data['Content'])
                # articlemodelObj.set_url(data['Url'])
                # articlemodelObj.set_published_at(data['Published_at'])
                # articlemodelObj.set_country(data['Country'])
                # articlemodelObj.set_reporter_id(data['Reporter_id'])
                articlemodelObj = ArticleModel(data)
                self._ArticleMapper.insertRow(articlemodelObj)

        print("Task Completed.....")
        while True:
            operation=""
            choice =0
            operation = input('Which Operation you want to perform?  \n 3.Search \n 4.Exit')

            if operation == "Search":
                choice=input("  1. Search all Articles \n 2. Search all Reporters working for a Channel"
                             " \n 3. Search Articles written by specific Reporter "
                             "\n 4.Search Articles based of specific Channel ")
                # if choice == "1":
                #     self._ChannelMapper.SearchOperation()
                # elif choice == "2" :
                #     self._ReporterMapper.SearchAllOperation()
                if choice == "1":
                    Sname = input("Enter Channel name for which you want to see authors : ")
                    channelmodelObj.set_channel_name(Sname)
                    self._ReporterMapper.SearchReporterOperation(channelmodelObj)
                elif choice == "2" :
                    self._ArticleMapper.SearchAllOperation()
                elif choice == "3" :
                    Aname = input("Enter name of Reporter for whom you want to search articles : ")
                    reportermodelObj.set_reporter_name(Aname)
                    self._ArticleMapper.SearchReporterArticlesOperation(reportermodelObj)
                elif choice == "4" :
                    Sname = input("Enter Channel name for which you want to search articles : ")
                    channelmodelObj.set_channel_name(Sname)
                    self._ArticleMapper.SearchChannelArticlesOperation(channelmodelObj)
                else:
                    print("Wrong Choice entered")

            elif (operation == "Exit"):
                exit()

            else:
                print("Wrong Choice entered")

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
