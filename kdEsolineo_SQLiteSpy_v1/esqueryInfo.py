# -*- coding: utf-8 -*-
import configPath
from elasticsearch import Elasticsearch
from elasticsearch import helpers
from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc

host_ = configPath.confFile().loadPath()[0]
port_ = configPath.confFile().loadPath()[1]
es_date = configPath.confFile().loadPath()[2].split(',')
#print(host_)
#print(port_)
#print(es_date)

for i in range(len(es_date)):
    #print(es_date[i])
    pass
idList =[]
class ElasticSearchMrg:
    def __init__(self):
        self.es = Elasticsearch("http://{0}:{1}".format(host_,port_),timeout=10)
        #print(self.es)
        self.index = "students"
        self.doc_type = "class"

    def searchInfo(self,query):
        try:
            res = self.es.search(index=self.index,doc_type=self.doc_type,body=query)
            #print(res)
            #result = res['hits']['total']
            result = res['hits']['hits']
            #for hit in result:
            #    print(hit)
            return result
            #print(result)
            #print(query)
            #count =  res['hits']['total']
            #print(count)
            #for i in range(0,count):
                #print(i)
            #    idList.append(res['hits']['hits'][i]['_id'])
            #print("查询到{0}条".format(count))
            #print(idList)
        except Exception as e:
            print(e)


def LoadConf():
   # query_all = {"query":{"bool":{"must":[{"term":{"a_mt_ves.date": query_time}}],"must_not":[],"should":[]}},"from":0,"size":10,"sort":[],"facets":{}}
    query_all = {"query":{"bool":{"must":[{"match_all":{}}],"must_not":[],"should":[]}},"from":0,"size":1000000,"sort":[],"aggs":{}}
    query_all_online ={"query":{"bool":{"must":[{"term":{"name.keyword":"Yang Yang"}}],"must_not":[],"should":[]}},"from":0,"size":10,"sort":[],"aggs":{}}
    return query_all,query_all_online
#es = ElasticSearchMrg()
#queryList = LoadConf()
#es.searchInfo(queryList[0])
