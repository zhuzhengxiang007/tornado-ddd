from urllib.parse import urlparse, parse_qs
import json

def RequestContext(_uri = ''):
    _return = dict()
    if '?' in _uri:
        parsed_url = urlparse(_uri)
        _params = parse_qs(parsed_url.query)
        for key,value in _params.items():
            _return[key] = ''.join(value)
    else:
        pass
    _return['request_context'] = json.dumps(_return)
    return _return

# 处理非默认类型
from datetime import datetime
def custom_serializer(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError("Type not serializable")

import Config.queue as queue_map
async def ReturnDict(redis,request,_return): 
    if _return == None:
        _return={'code':1,'msg':'ok','data':[]}
    request['response_context'] = json.dumps(_return)
    await redis.rpush(queue_map.SYSTEM_LOG_REDIS_QUEUE_KEY,json.dumps(request))
    return _return

def ReturnJson(code=1,msg='ok',data=[]):
    return {'code':code,'msg':msg,'data':data}

def CheckParams(data,keys):
    _ = None
    for _k in keys:
        if _k not in data:
            return ReturnJson(0,_k + '参数不存在')
    return _