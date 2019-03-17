

def query():
    global name
    global age
    queryInfo1 = {
"query": {
"bool": {
"must": [
{
"term": {
"_id": "1"
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
    return (queryInfo1)
   # print(queryInfo1)
