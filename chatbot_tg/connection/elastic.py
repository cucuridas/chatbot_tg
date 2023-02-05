import abc
import chatbot_tg.core.config 
from elasticsearch import Elasticsearch
from chatbot_tg.connection.conn_avbstract import connect
import logging

INDEX = "service_list"
BODY = {
  "id": "search_list",
  "params": {
    "test": '' 
  }

}

SEARCH_BODY = {
  "query": {
    "match": {
      "service": ""
    }
  }
}

class elasticsearchConnect(connect) : 
    def __init__(self) -> None:
        self.es = None

    def getConenction(self,elasticsearch_url) :
        es = Elasticsearch(elasticsearch_url)
        return es

    def checkConnection(self):
        if self.es == None:
            return False
        else: True

    def checkChannel(self):
        if self.es.ping() :
            pass
        else : 
            raise Exception("Elasticsearch connect fail")

xwx


class Search : 
    def __init__(self) -> None:
        if elasticsearchConnect.checkConnection() :
            logging.info("Empty connection")
            self.es = elasticsearchConnect.getConenction()
        else : 
            logging.info("Exist connection")
            

    def search(self,input) :
        SEARCH_BODY["query"]["match"]["service"] = input
        return self.es.search(index=INDEX,body=SEARCH_BODY)
    




