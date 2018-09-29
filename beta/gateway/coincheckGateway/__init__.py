# encoding: UTF-8

from __future__ import absolute_import
from vnpy.trader import vtConstant
from .coincheckGateway import CoincheckGateway, CoincheckTradeApi , CoincheckSocketDataApi

gatewayClass = CoincheckGateway
gatewayName = 'COINCHECK'
gatewayDisplayName = u'COINCHECK'
gatewayType = vtConstant.GATEWAYTYPE_BTC
gatewayQryEnabled = True

