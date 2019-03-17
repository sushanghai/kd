# -*- coding: utf-8 -*-
import configPath
from elasticsearch import Elasticsearch
from elasticsearch import helpers
import  queryInfo
from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc


query = queryInfo.query()

host_ = configPath.confFile().loadPath()[0]
port_ = configPath.confFile().loadPath()[1]
#print(host_)
#print(port_)
idList =[]
class ElasticSearchMrg:
    def __init__(self):
        self.es = Elasticsearch("http://{0}:{1}".format(host_,port_),timeout=10)
        #print(self.es)
        self.index = "students"
        self.doc_type = "class"

    def searchInfo(self,query):
        res = self.es.search(index=self.index,doc_type=self.doc_type,body=query)
        #print(res)
        #print(query)
        count =  res['hits']['total']
        #print(count)
        for i in range(0,count):
            #print(i)
            idList.append(res['hits']['hits'][i]['_id'])
        print("查询到{0}条".format(count))
        #print(idList)
    def updateID(self,number1):
        #print(idList)
        sucessCount = 0
        actions = []
        for id_ in idList:
            #print(id_)
            action = {
                '_op_type':'update',
                '_index':self.index,
                '_type':self.doc_type,
                '_id':id_,
                'doc':{"number1":number1}
            }
            actions.append(action)
            try:
                if(len(actions)==3):
                    print(actions)
                    helpers.bulk(self.es,actions)
                    sucessCount = sucessCount+len(actions)
                    print("总共把{0}条name更新为{1}".format(sucessCount,number1))
                    del actions[:]
            except Exception as e:
                print(e)
        try:
            if(len(actions) > 0):
                print(actions)
               # helpers.bulk(self.es,actions,timeout=30)
                helpers.bulk(self.es,actions)
                sucessCount = sucessCount + len(actions)
                print("总共把{0}条name更新为{1}".format(sucessCount,number1))
                del actions[:]

        except Exception as e:
            print(e)
#       print(actions)

   # def updateInfo(self,name):

es = ElasticSearchMrg()
es.searchInfo(query)
es.updateID("1")



