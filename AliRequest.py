# -*- coding: utf-8 -*-

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkalidns.request.v20150109 import DescribeDomainRecordsRequest
from aliyunsdkalidns.request.v20150109 import UpdateDomainRecordRequest
import json
import argparse
import sys


def getAcsClient():
    # TODO: replace yourself access id
    return AcsClient("your access id", " your access token")


def getDomainRecordId(domainName, RR):
    """
    :param domainName: 域名,如m.aliyun.com,填aliyun.com
    :param RR:主机记录，就是域名前缀，如abc.aliyun.com,填abc
    :return:
    """

    request = DescribeDomainRecordsRequest.DescribeDomainRecordsRequest()
    request.set_DomainName(domainName)
    client = getAcsClient()
    response = client.do_action_with_exception(request)
    print response
    jsonObj = json.loads(response)
    records = jsonObj["DomainRecords"]["Record"]
    for record in records:
       if record['RR'] == RR:
          return record['RecordId']
    return None


def updateDomainRecord(recordId, ip, RR, Type):
    """
    :param recordId:
    :param ip: 域名要映射的公网ip
    :param RR: 主机记录
    :param Type: 记录类型。如：Ａ,将域名指向一个ipv4地址。其他类型说明请参阅阿里云官方说明文档
    :return:
    """
    request = UpdateDomainRecordRequest.UpdateDomainRecordRequest()
    request.set_RecordId(recordId)
    request.set_RR(RR)
    request.set_Value(ip)
    request.set_Type(Type)

    client = getAcsClient()
    try:
        client.do_action_with_exception(request)
    except ServerException as e:
        print "update domain record error: %s, %s" % (e.get_error_code(), e.get_error_msg())
        return -1

    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default=None)
    args = parser.parse_args()
    ip = args.ip
    if ip is None:
        print "The ip argument is None!"
        sys.exit(-1)
    else:
        # TODO replace your domain name
        recordId = getDomainRecordId("your domain name", "www")
        if recordId is not None:
            retCode = updateDomainRecord(recordId, ip, "www", "A")
            sys.exit(retCode)
        sys.exit(-1)