#!/usr/bin/env python
#coding=utf-8

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkiot.request.v20180120.CreateRuleRequest import CreateRuleRequest

client = AcsClient('<accessKeyId>', '<accessSecret>', 'cn-shanghai')

request = CreateRuleRequest()
request.set_accept_format('json')


request.set_Name("Name124")
request.set_DataType("1")

response = client.do_action_with_exception(request)
# python2:  print(response) 
print(response)
