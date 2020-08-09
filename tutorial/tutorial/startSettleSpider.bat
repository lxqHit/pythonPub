@ECHO OFF
REM 启动爬取当日结算基金净值
cd /d D:/workspace/dev/test/tutorial/tutorial
call scrapy crawl theSettleValue
PAUSE