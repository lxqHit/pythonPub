#coding:utf-8
import urllib.parse
from datetime import datetime, date, timedelta

# 获取估值的请求url
class GetNowValueUrl(object):
    # fund估值请求url构造
    def getGzFundUrl(self):
        # 所有基金请求url
        start_urls = []
        # 所有爬取基金的代码
        codes = [
            '001595', # 天弘中证银行
            '001632', # 天弘中证食品饮料
            '005918', # 天弘沪深300
            '001630', # 天弘中证计算机
            '001553', # 天弘中证证券保险
            '001549', # 天弘上证50
            '001618', # 天弘中证电子
            '001551', # 天弘中证医药
            '001559', # 天弘医疗健康
            '002979', # 广发金融地产
            '002982', # 广发养老产业
            '002974', # 广发信息技术
            '005693', # 广发中证军工
            '002984', # 广发中证环保产业
            '002977', # 广发中证全指可选消费
            '007882', # 易方达沪深300非银行金融
            '007029', # 易方达中证500
            '004744', # 易方达创业板
            '007301', # 国联安中证全指半导体
            '005940'  # 工银瑞信新能源汽车主题混合C
        ]
        # 拼接请求url
        orgUrl = "http://fundgz.1234567.com.cn/js/"
        for code in codes:
            url =  orgUrl + code + '.js'
            start_urls.append(url)

        return start_urls
