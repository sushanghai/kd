# _*_ coding:utf-8 _*_
from datetime import datetime
from elasticsearch import Elasticsearch
import cx_Oracle as oracle
import xm_rdxlpath
import os

'读取数据库连接配置,读取查询的时间配置'
dburl = xm_rdxlpath.RdPath().rdoracl()
esurl = xm_rdxlpath.RdPath().rdes()
rddate = xm_rdxlpath.RdPath().rddate()
es_date = xm_rdxlpath.RdPath().rddate().split(',')
#print(dburl)
#print(esurl)
#print(es_date)

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
conn =oracle.connect(dburl)
cursor=conn.cursor()
'es配置连接'
es = Elasticsearch([{'host':esurl,'port':9200}])
#print(es)
def from_es_to_orcl():
    for i in range(len(es_date)):
        #print(i)
        query_time = es_date[i]
        #print(query_time)

        # 查询总的在线数量
        query = {"query":{"bool":{"must":[{"term":{"a_mt_ves.date": query_time}}],"must_not":[],"should":[]}},"from":0,"size":10,"sort":[],"facets":{}}
        #query = {'query': {'match_all': {}}}
        res = es.search(index="a_mt_ves", doc_type="a_mt_ves",body=query,timeout=30)
        #print (res)
        total_query = res['hits']['total']
        print(query_time,total_query)
        # 查询离线总数
        query__offline = {"query": {
            "bool": {"must": [{"term": {"a_mt_ves.date": query_time}}, {"term": {"a_mt_ves.sbztlx": "3"}}],
                     "must_not": [], "should": []}}, "from": 0, "size": 10, "sort": [], "facets": {}}
        offline_res = es.search(index="a_mt_ves", doc_type="a_mt_ves", body=query__offline, timeout=30)
        offline_num = offline_res['hits']['total']
        print(query_time, offline_num)


        #查询一类点总的在线数
        query1__total={"query":{"bool":{"must":[{"term":{"a_mt_ves.date":query_time}},{"term":{"a_mt_ves.jkqylx":"1"}}],"must_not":[],"should":[]}},"from":0,"size":10,"sort":[],"facets":{}}
        res1 = es.search(index="a_mt_ves", doc_type="a_mt_ves", body=query1__total, timeout=30)
        total_query1 = res1['hits']['total']
        print(query_time, total_query1)
        # 查询一类离线总数
        query1_offline = {"query":{"bool":{"must":[{"term":{"a_mt_ves.date":query_time}},{"term":{"a_mt_ves.sbztlx":"3"}},{"term":{"a_mt_ves.jkqylx":"1"}}],"must_not":[],"should":[]}},"from":0,"size":10,"sort":[],"facets":{}}
        offline_res1 = es.search(index="a_mt_ves", doc_type="a_mt_ves", body=query1_offline, timeout=30)
        offline_num1 = offline_res1['hits']['total']
        print(query_time, offline_num1)


        # 查询二类点总的在线数
        query2__total = {"query": {
            "bool": {"must": [{"term": {"a_mt_ves.date": query_time}}, {"term": {"a_mt_ves.jkqylx": "2"}}],
                     "must_not": [], "should": []}}, "from": 0, "size": 10, "sort": [], "facets": {}}
        res2 = es.search(index="a_mt_ves", doc_type="a_mt_ves", body=query2__total, timeout=30)
        total_query2 = res2['hits']['total']
        print(query_time, total_query2)
        # 查询二类离线总数
        query2_offline = {"query": {"bool": {
            "must": [{"term": {"a_mt_ves.date": query_time}}, {"term": {"a_mt_ves.sbztlx": "3"}},
                     {"term": {"a_mt_ves.jkqylx": "2"}}], "must_not": [], "should": []}}, "from": 0, "size": 10,
                           "sort": [], "facets": {}}
        offline_res2 = es.search(index="a_mt_ves", doc_type="a_mt_ves", body=query2_offline, timeout=30)
        offline_num2 = offline_res2['hits']['total']
        print(query_time, offline_num2)


        # 查询三类点总的在线数
        query3__total = {"query": {
            "bool": {"must": [{"term": {"a_mt_ves.date": query_time}}, {"term": {"a_mt_ves.jkqylx": "3"}}],
                     "must_not": [], "should": []}}, "from": 0, "size": 10, "sort": [], "facets": {}}
        res3 = es.search(index="a_mt_ves", doc_type="a_mt_ves", body=query3__total, timeout=30)
        total_query3 = res3['hits']['total']
        print(query_time, total_query3)

        # 查询三类离线总数
        query3_offline = {"query": {"bool": {
            "must": [{"term": {"a_mt_ves.date": query_time}}, {"term": {"a_mt_ves.sbztlx": "3"}},
                     {"term": {"a_mt_ves.jkqylx": "3"}}], "must_not": [], "should": []}}, "from": 0, "size": 10,
                           "sort": [], "facets": {}}
        offline_res3 = es.search(index="a_mt_ves", doc_type="a_mt_ves", body=query3_offline, timeout=30)
        offline_num3 = offline_res3['hits']['total']
        print(query_time, offline_num3)

        sql = "insert into online_rate(time,TOTAL,OFFLINET,ONETOTAL,OFFLINEONE,TWOTOTAL,OFFLINETWO,THREETOTAL,OFFLINETHREE) values ('" + str(query_time) + "','" + str(total_query) + "','" + str(
            offline_num) + "','" + str(total_query1) + "','" + str(offline_num1) + "','" + str(total_query2) + "','" + str(offline_num2) + "','" + str(total_query3) + "','" + str(offline_num3) + "')"

        print(sql)
        cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
if __name__ == '__main__':
    from_es_to_orcl()