# coding: UTF-8
# 获取wind全球行业分类股票代码#

# 初始化接口#
from WindPy import *
import time

t = time.strftime ( "%Y%m%d", time.localtime () )
print ( t )

w.start ( )

# 获取全球股票代码#
AllAStock = w.wset ( "SectorConstituent", "date=20190313;sectorId=a001010100000000;field=wind_code" );
if AllAStock.ErrorCode != 0:
    print ( "Get Data failed! exit!" )
    exit ()

Zqdm = AllAStock.Data[0]
# print(AllAStock.Data)
# print (Zqdm)

# 获取中信行业一级分类信息
#Zxhy = w.wss ( Zqdm, "sec_name,industry_citic", "tradeDate=20190301;industryType=1" )
#print ( Zxhy )

Zxhy = w.wss(Zqdm, "industry_gics","industryType=1")
print ( Zxhy )
#!/usr/bin/env python
# -*- coding:utf-8 -*-