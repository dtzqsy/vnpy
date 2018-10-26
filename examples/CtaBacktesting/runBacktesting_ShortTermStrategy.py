# encoding: UTF-8

"""
展示如何执行策略回测。
"""

from __future__ import division

import os

from vnpy.trader.app.ctaStrategy.ctaBacktesting import BacktestingEngine, MINUTE_DB_NAME,DAILY_DB_NAME

import vnpy.trader.app.ctaStrategy.strategy.strategyShortTerm as STS
#----------------------------------------------------------------------
def calculateDailyResult_init():
    """主函数，供其他python程序进行模块化程序初始化调用"""
    #from vnpy.trader.app.ctaStrategy.strategy.strategyShortTerm import ShortTermStrategy
    reload(STS)
    # 创建回测引擎
    engine = BacktestingEngine()
    
    # 设置引擎的回测模式为K线
    engine.setBacktestingMode(engine.BAR_MODE)
    
    # 设置产品相关参数
    engine.setSlippage(0)      # 股指1跳
    engine.setRate(0)          # 万0.3
    engine.setSize(10)         # 股指合约大小 
    engine.setPriceTick(1)     # 股指最小价格变动
    engine.setCapital(30000)
    
    # 在引擎中创建策略对象
    d = {}
    engine.initStrategy(STS.ShortTermStrategy, d)
    return engine

#----------------------------------------------------------------------
'''根据计算每日结果，输出到CSV中'''
def calculateDailyResult_to_CSV(engine,date,pos,csvfile):
    """主函数，供其他python程序进行模块化程序调用"""
    # 设置回测用的数据起始日期
    engine.setStartDate('20090327')
    engine.strategy.strategyStartpos = pos
    
    # 设置使用的历史数据库
    engine.setDatabase(DAILY_DB_NAME, 'RB9999')
    
    # 开始跑回测
    engine.runBacktesting()
    
    # 显示回测结果到CSV中 用于在K线上显示交易信号
    df= engine.calculateDailyResult_to_CSV(csvfile)    
  
    # 显示回测结果  用于文华的ctrl+G的快捷键功能
    os.system('cls')
    print(u"RB9999 短期结构交易系统")
    print('start date:'+date)
    engine.showBacktestingResultLikeWH(df)
#----------------------------------------------------------------------
'''获得策略需要的初始化时间'''
def get_strategy_init_days(engine):
    return engine.strategy.initDays        
    
if __name__ == '__main__' :
    #or  __name__ == 'runBacktesting_WH':
    from vnpy.trader.app.ctaStrategy.strategy.strategyShortTerm import ShortTermStrategy
    # 创建回测引擎
    engine = BacktestingEngine()
    # 设置引擎的回测模式为K线
    engine.setBacktestingMode(engine.BAR_MODE)

    # 设置回测用的数据起始日期
    engine.setStartDate('20090329')
    
    # 设置产品相关参数
    engine.setSlippage(0)      # 股指1跳
    engine.setRate(0)          # 万0.3
    engine.setSize(10)         # 股指合约大小 
    engine.setPriceTick(1)     # 股指最小价格变动
    engine.setCapital(30000)
    
    # 设置使用的历史数据库
    engine.setDatabase(DAILY_DB_NAME, 'RB9999')
    
    # 在引擎中创建策略对象
    d = {}
    engine.initStrategy(ShortTermStrategy, d)

    engine.strategy.strategyStartpos = 0    
    # 开始跑回测
    engine.runBacktesting()
    
    # 计算回测结果
    engine.calculateBacktestingResult()
    # 显示回测结果
    engine.showBacktestingResult()