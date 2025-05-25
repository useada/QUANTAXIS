import QUANTAXIS as QA
import data_init

# ======================================================================================================================
datamodelx = data_init.datamodelx(QA.MARKET_TYPE.STOCK_CN, QA.FREQUENCE.DAY)
datamodelx.create_table()
datamodelx.quit()

datamodelx = data_init.datamodelx(QA.MARKET_TYPE.FUTURE_CN, QA.FREQUENCE.DAY)
datamodelx.create_table()
datamodelx.quit()

datamodelx = data_init.datamodelx(QA.MARKET_TYPE.INDEX_CN, QA.FREQUENCE.DAY)
datamodelx.create_table()
datamodelx.quit()

datamodelx = data_init.datamodelx(QA.MARKET_TYPE.OPTION_CN, QA.FREQUENCE.DAY)
datamodelx.create_table()
datamodelx.quit()

datamodelx = data_init.datamodelx('etf_cn', QA.FREQUENCE.DAY)
datamodelx.create_table()
datamodelx.quit()

datamodelx = data_init.datamodelx('lof_cn', QA.FREQUENCE.DAY)
datamodelx.create_table()
datamodelx.quit()

# ======================================================================================================================
datamodelx = data_init.datamodelx(QA.MARKET_TYPE.STOCK_CN, QA.FREQUENCE.ONE_MIN)
datamodelx.create_table()
datamodelx.quit()

datamodelx = data_init.datamodelx(QA.MARKET_TYPE.FUTURE_CN, QA.FREQUENCE.ONE_MIN)
datamodelx.create_table()
datamodelx.quit()

datamodelx = data_init.datamodelx(QA.MARKET_TYPE.INDEX_CN, QA.FREQUENCE.ONE_MIN)
datamodelx.create_table()
datamodelx.quit()

datamodelx = data_init.datamodelx(QA.MARKET_TYPE.OPTION_CN, QA.FREQUENCE.ONE_MIN)
datamodelx.create_table()
datamodelx.quit()

datamodelx = data_init.datamodelx('etf_cn', QA.FREQUENCE.ONE_MIN)
datamodelx.create_table()
datamodelx.quit()

datamodelx = data_init.datamodelx('lof_cn', QA.FREQUENCE.ONE_MIN)
datamodelx.create_table()
datamodelx.quit()

# ======================================================================================================================
datamodelx = data_init.datamodelx(QA.MARKET_TYPE.STOCK_CN, QA.FREQUENCE.FIVE_MIN)
datamodelx.create_table()
datamodelx.quit()

datamodelx = data_init.datamodelx(QA.MARKET_TYPE.FUTURE_CN, QA.FREQUENCE.FIVE_MIN)
datamodelx.create_table()
datamodelx.quit()

datamodelx = data_init.datamodelx(QA.MARKET_TYPE.INDEX_CN, QA.FREQUENCE.FIVE_MIN)
datamodelx.create_table()
datamodelx.quit()

datamodelx = data_init.datamodelx(QA.MARKET_TYPE.OPTION_CN, QA.FREQUENCE.FIVE_MIN)
datamodelx.create_table()
datamodelx.quit()

datamodelx = data_init.datamodelx('etf_cn', QA.FREQUENCE.FIVE_MIN)
datamodelx.create_table()
datamodelx.quit()

datamodelx = data_init.datamodelx('lof_cn', QA.FREQUENCE.FIVE_MIN)
datamodelx.create_table()
datamodelx.quit()

# ======================================================================================================================
datamodelx = data_init.datamodelx(QA.MARKET_TYPE.STOCK_CN, QA.FREQUENCE.FIFTEEN_MIN)
datamodelx.create_table()
datamodelx.quit()

datamodelx = data_init.datamodelx(QA.MARKET_TYPE.FUTURE_CN, QA.FREQUENCE.FIFTEEN_MIN)
datamodelx.create_table()
datamodelx.quit()

datamodelx = data_init.datamodelx(QA.MARKET_TYPE.INDEX_CN, QA.FREQUENCE.FIFTEEN_MIN)
datamodelx.create_table()
datamodelx.quit()

datamodelx = data_init.datamodelx(QA.MARKET_TYPE.OPTION_CN, QA.FREQUENCE.FIFTEEN_MIN)
datamodelx.create_table()
datamodelx.quit()

datamodelx = data_init.datamodelx('etf_cn', QA.FREQUENCE.FIFTEEN_MIN)
datamodelx.create_table()
datamodelx.quit()

datamodelx = data_init.datamodelx('lof_cn', QA.FREQUENCE.FIFTEEN_MIN)
datamodelx.create_table()
datamodelx.quit()

# ======================================================================================================================
datamodelx = data_init.datamodelx(QA.MARKET_TYPE.STOCK_CN, QA.FREQUENCE.TICK)
datamodelx.create_table()
datamodelx.quit()

datamodelx = data_init.datamodelx(QA.MARKET_TYPE.FUTURE_CN, QA.FREQUENCE.TICK)
datamodelx.create_table()
datamodelx.quit()

datamodelx = data_init.datamodelx(QA.MARKET_TYPE.INDEX_CN, QA.FREQUENCE.TICK)
datamodelx.create_table()
datamodelx.quit()

datamodelx = data_init.datamodelx(QA.MARKET_TYPE.OPTION_CN, QA.FREQUENCE.TICK)
datamodelx.create_table()
datamodelx.quit()

# datamodelx = data_init.datamodelx('etf_cn', QA.FREQUENCE.TICK)
# datamodelx.create_table()
# datamodelx.quit()

datamodelx = data_init.datamodelx('lof_cn', QA.FREQUENCE.TICK)
datamodelx.create_table()
datamodelx.quit()
