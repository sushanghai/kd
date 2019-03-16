# -*- coding: utf-8 -*-
import configPath
from elasticsearch import Elasticsearch


class ElasticSearchMrg:
    def __init__(self):
        host_ = configPath.confFile().loadPath()[0]
        port_ = configPath.confFile().loadPath()[1]
        self.es = Elasticsearch("http://{0},{1}".format(host_,port_),timeout=10)
        print(self.es)
        self.index = "test"
        self.doc_type = "test"


ElasticSearchMrg.__init__()


