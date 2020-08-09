#coding:utf-8
import urllib.parse

class GetUrl(object):
    # 天弘基金请求url构造
    def getThFundUrl(self):
        # 所有天弘基金请求url
        start_urls = []
        # 所有爬取天弘基金的代码
        codes = [
            '001595', # 中证银行
            '001632', # 中证食品饮料
            '005918', # 沪深300
            '001630', # 中证计算机
            '001553', # 中证证券保险
            '001549', # 上证50
            '001618', # 中证电子
            '001551', # 中证医药
            '001559'  # 医疗健康
        ]
        # 拼接请求url
        orgUrl = "http://fund.eastmoney.com/f10/F10DataApi.aspx"
        for code in codes:
            params = {'type': 'lsjz', 'code': code, 'page': 1, 'per': 20, 'sdate': '2015-01-01', 'edate': '2020-03-20'}
            query_string = urllib.parse.urlencode(params)
            url =  orgUrl + '?' + query_string
            start_urls.append(url)

        return start_urls

    # 广发基金请求url构造
    def getGfFundUrl(self):
        # 所有广发基金请求url
        start_urls = []
        # 所有爬取广发基金的代码
        codes = [
            '002979', # 金融地产
            '002982', # 养老产业
            '002974', # 信息技术
            '005693', # 中证军工
            '002984', # 中证环保产业
            '002977', # 中证全指可选消费
            '006479'  # 纳斯达克
        ]
        # 拼接请求url
        orgUrl = "http://fund.eastmoney.com/f10/F10DataApi.aspx"
        for code in codes:
            params = {'type': 'lsjz', 'code': code, 'page': 1, 'per': 20, 'sdate': '2015-01-01', 'edate': '2020-03-20'}
            query_string = urllib.parse.urlencode(params)
            url =  orgUrl + '?' + query_string
            start_urls.append(url)

        return start_urls
    
    # 其他基金请求url构造
    def getElseFundUrl(self):
        # 所有其他基金请求url
        start_urls = []
        # 所有爬取其他基金的代码
        codes = [
            '007882', # 易方达沪深300非银行金融
            '007029', # 易方达中证500
            '004744', # 易方达创业板
            '007301', # 国联安中证全指半导体
            '005940'  # 工银瑞信新能源汽车主题混合C
        ]
        # 拼接请求url
        orgUrl = "http://fund.eastmoney.com/f10/F10DataApi.aspx"
        for code in codes:
            params = {'type': 'lsjz', 'code': code, 'page': 1, 'per': 20, 'sdate': '2015-01-01', 'edate': '2020-03-20'}
            query_string = urllib.parse.urlencode(params)
            url =  orgUrl + '?' + query_string
            start_urls.append(url)

        return start_urls

    # 后续添加的基金请求url构造
    def getAddNewFundUrl(self):
        # 所有基金请求url
        start_urls = []
        # 所有爬取基金的代码
        codes = [
            '007882', # 易方达沪深300非银行金融
            '007029' # 易方达中证500
        ]
        # 拼接请求url
        orgUrl = "http://fund.eastmoney.com/f10/F10DataApi.aspx"
        for code in codes:
            params = {'type': 'lsjz', 'code': code, 'page': 1, 'per': 20, 'sdate': '2015-01-01', 'edate': '2020-03-20'}
            query_string = urllib.parse.urlencode(params)
            url =  orgUrl + '?' + query_string
            start_urls.append(url)

        return start_urls