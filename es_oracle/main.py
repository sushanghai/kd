# -*- coding: utf-8 -*-
import esConn


def main():
    esConn.ElasticSearchMrg.searchInfo()

def qurey():
    global name
    global age
    queryInfo = {
"query": {
"bool": {
"must": [
{
"term": {
"name": "guomeimei"
}
}
],
"must_not": [ ],
"should": [ ]
}
},
"from": 0,
"size": 10,
"sort": [ ],
"aggs": { }
}

    return (queryInfo)

if __name__ == "__main__":
    main()



