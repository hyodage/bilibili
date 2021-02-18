import json
import requests
# 登录
def dologinOne():
    someVideourl = "https://www.bilibili.com/video/BV1Mv411i7SL"
    headers = {
      'authority': 'www.bilibili.com',
      'cache-control': 'max-age=0',
      'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
      'sec-ch-ua-mobile': '?0',
      'upgrade-insecure-requests': '1',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
      'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
      'sec-fetch-site': 'same-site',
      'sec-fetch-mode': 'navigate',
      'sec-fetch-user': '?1',
      'sec-fetch-dest': 'document',
      'referer': 'https://space.bilibili.com/',
      'accept-language': 'en,zh-CN;q=0.9,zh;q=0.8',
      'cookie': 'finger=158939783; CURRENT_FNVAL=80; _uuid=D8E8EC5E-090A-E378-390B-6B7CCD4EF8CA38347infoc; blackside_state=1; rpdid=|(umll|u|R|~0J\'uYukJY|~RY; DedeUserID=396914707; DedeUserID__ckMd5=06a901d4711b599e; LIVE_BUVID=AUTO9416125333361138; sid=j9yqozn5; fingerprint=786f5c66d501446c940d9ccc7116be63; SESSDATA=a16ea77a%2C1628222948%2C9e12e*21; bili_jct=f91dccbf7e1103afcd2c96a30e7e8857; CURRENT_QUALITY=80; buvid3=5BC250A1-A860-4BD4-A7FC-54FC3D26CA0618569infoc; PVID=1; finger=158939783; bsource=search_google; fingerprint3=6ce82396a9848cb5f877c78dee82c2e5; fingerprint_s=08567af00e4a862d28f5100bf4ae55c3; buvid_fp=5BC250A1-A860-4BD4-A7FC-54FC3D26CA0618569infoc; buvid_fp_plain=5BC250A1-A860-4BD4-A7FC-54FC3D26CA0618569infoc'
    }
    requests.request("GET", someVideourl, headers=headers)
# 获取硬币
def getCoin():
    getCoinUrl = "https://account.bilibili.com/site/getCoin"
    headers = {
      'authority': 'account.bilibili.com',
      'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
      'accept': 'application/json, text/plain, */*',
      'sec-ch-ua-mobile': '?0',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
      'sec-fetch-site': 'same-origin',
      'sec-fetch-mode': 'cors',
      'sec-fetch-dest': 'empty',
      'referer': 'https://account.bilibili.com/account/coin',
      'accept-language': 'en,zh-CN;q=0.9,zh;q=0.8',
      'cookie': 'CURRENT_FNVAL=80; _uuid=D8E8EC5E-090A-E378-390B-6B7CCD4EF8CA38347infoc; blackside_state=1; rpdid=|(umll|u|R|~0J\'uYukJY|~RY; DedeUserID=396914707; DedeUserID__ckMd5=06a901d4711b599e; LIVE_BUVID=AUTO9416125333361138; sid=j9yqozn5; fingerprint=786f5c66d501446c940d9ccc7116be63; SESSDATA=a16ea77a%2C1628222948%2C9e12e*21; bili_jct=f91dccbf7e1103afcd2c96a30e7e8857; CURRENT_QUALITY=80; buvid3=5BC250A1-A860-4BD4-A7FC-54FC3D26CA0618569infoc; PVID=1; bsource=search_google; fingerprint3=6ce82396a9848cb5f877c78dee82c2e5; fingerprint_s=08567af00e4a862d28f5100bf4ae55c3; buvid_fp=5BC250A1-A860-4BD4-A7FC-54FC3D26CA0618569infoc; buvid_fp_plain=5BC250A1-A860-4BD4-A7FC-54FC3D26CA0618569infoc'
    }
    response = requests.request("GET", getCoinUrl, headers=headers).text
    dict_data = json.loads(response)
    if dict_data['code'] == 0:
        return '硬币数量:'+str(dict_data['data']['money'])

def dologinOne2():
    url = "https://www.bilibili.com/video/BV1Mv411i7SL?from=search&seid=14621071900608754747"
    headers = {
      'authority': 'www.bilibili.com',
      'cache-control': 'max-age=0',
      'upgrade-insecure-requests': '1',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
      'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
      'sec-fetch-site': 'same-site',
      'sec-fetch-mode': 'navigate',
      'sec-fetch-user': '?1',
      'sec-fetch-dest': 'document',
      'referer': 'https://search.bilibili.com/',
      'accept-language': 'zh-CN,zh;q=0.9',
      'cookie': 'buvid3=057BBCF8-5F18-35DE-CA65-53E91A0E4CB899703infoc; CURRENT_FNVAL=80; _uuid=21BFCBDA-CE8E-D677-42B8-EBEC0F85BD2D01623infoc; blackside_state=1; bsource=search_baidu; finger=194759311; sid=jb1au2pt; fingerprint=553d80279b93635a2754dbb6a361bbe6; buvid_fp=057BBCF8-5F18-35DE-CA65-53E91A0E4CB899703infoc; DedeUserID=383750898; DedeUserID__ckMd5=5bc18b29cd8d7af9; SESSDATA=8c8355b2%2C1629192256%2C930d1*21; bili_jct=bbe61ab1b3d79fad20c055b660c7cbce; fingerprint3=da3563fa014d074b656badc66c6754a6; fingerprint_s=ae2934f9fac7ba440d654f37714f1624; buvid_fp_plain=057BBCF8-5F18-35DE-CA65-53E91A0E4CB899703infoc; PVID=1'
    }
    requests.request("GET", url, headers=headers)
def getCoin2():
    url = "https://account.bilibili.com/site/getCoin"
    headers = {
        'authority': 'account.bilibili.com',
        'accept': 'application/json, text/plain, */*',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://account.bilibili.com/account/coin',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': 'buvid3=057BBCF8-5F18-35DE-CA65-53E91A0E4CB899703infoc; CURRENT_FNVAL=80; _uuid=21BFCBDA-CE8E-D677-42B8-EBEC0F85BD2D01623infoc; blackside_state=1; bsource=search_baidu; sid=jb1au2pt; fingerprint=553d80279b93635a2754dbb6a361bbe6; buvid_fp=057BBCF8-5F18-35DE-CA65-53E91A0E4CB899703infoc; DedeUserID=383750898; DedeUserID__ckMd5=5bc18b29cd8d7af9; SESSDATA=8c8355b2%2C1629192256%2C930d1*21; bili_jct=bbe61ab1b3d79fad20c055b660c7cbce; fingerprint3=da3563fa014d074b656badc66c6754a6; fingerprint_s=ae2934f9fac7ba440d654f37714f1624; buvid_fp_plain=057BBCF8-5F18-35DE-CA65-53E91A0E4CB899703infoc'
    }
    response = requests.request("GET", url, headers=headers).text
    dict_data = json.loads(response)
    if dict_data['code'] == 0:
        return '硬币数量:' + str(dict_data['data']['money'])
dologinOne()
dologinOne2()
Durl="https://oapi.dingtalk.com/robot/send?access_token=50eddf1bb199ca683ae5ea4ba00b6a918af530d1779e94f70183f4f61b995dd9"
msg={
    "msgtype":"text",
    "text":{
        "content":'B站:'+getCoin()+' | '+getCoin2(),
    }
}
requests.post(Durl,
    headers={'Content-Type':'application/json'},
    data=json.dumps(msg)
)
