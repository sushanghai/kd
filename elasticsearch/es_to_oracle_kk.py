# _*_ coding:utf-8 _*_
from datetime import datetime
from elasticsearch import Elasticsearch
import cx_Oracle as oracle
import xm_rdxlpath
import os

'读取数据库连接配置,读取查询的时间配置'
dburl = xm_rdxlpath.RdPath().rdoracl()
esurl = xm_rdxlpath.RdPath().rdes()
rdtime = xm_rdxlpath.RdPath().rdtime()
es_time = xm_rdxlpath.RdPath().rdtime().split(',')
#print(dburl)
#print(esurl)
#print(es_time)
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
conn =oracle.connect(dburl)
cursor=conn.cursor()
'es配置连接'
es = Elasticsearch([{'host':esurl,'port':9200}])
#print(es)
def from_es_to_orcl():
    for i in range(len(es_time)):
        #print(i)
        query_time = es_time[i]
        #print(query_time)

        # 查询数据
        query = {'query': {'bool': {'must': [{'term': {'b_kkqp_tj_rll.JGRQ': query_time}}],'must_not': [ ],'should': [ ]}},'from': 0,'size': 30000,'sort': [ ],'facets': { }}
        #query = {'query': {'match_all': {}}}
        res = es.search(index="kkqp_tj_rll_read", doc_type="b_kkqp_tj_rll",body=query,timeout=30)
        #print (res)
        for hit in res['hits']['hits']:
            #print(hit["_source"])
            dirct = hit["_source"]
            #print(dirct['number1'],dirct['name'],dirct['message'])
            sbbh = dirct['SBBH']
            jgrq = dirct['JGRQ']
            zll = dirct['ZLL']
            #print(sbbh,jgrq,zll)
            sql = "insert into test_rll(sbbh,jgrq,zll) values ('" + str(sbbh) + "','" + str(jgrq) + "','" + str(
                zll) + "')"
            print(sql)
            cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
if __name__ == '__main__':
    from_es_to_orcl()
