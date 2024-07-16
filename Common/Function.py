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

# from Common.Redis import RedisService
import Config.queue as queue_map
async def ReturnDict(redis,request,code=1,msg='ok',data=[]): 
    _return = {'code':code,'msg':msg,'data':data}
    request['response_context'] = json.dumps(_return)
    redis.rpush(queue_map.SYSTEM_LOG_REDIS_QUEUE_KEY,json.dumps(request))
    return _return
    