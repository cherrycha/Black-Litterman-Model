import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot  as  plt

#定义常量和全局变量
YEAR = "year"
MONTH = "month"
DAY = "day"
PERIOD=YEAR
Period=PERIOD
BEGIN = "2010/1/1"
Begin = BEGIN
END = "2017/12/31"
End = END

yearReturn = "lib/YearReturnRate/TRD_Year.csv"  # 沪深300成分股年回报率
yearReturn300 = "lib/300YearReturnRate/300YearReturnRate.csv"  # 沪深300股指年回报率
monthReturn300 = "lib/300YearReturnRate/300MonthReturnRate.csv"  # 沪深300估值月回报率
dayReturn300 = "lib/300YearReturnRate/300DayReturnRate.csv"  # 沪深300估值日回报率
yearNoRiskReturn = "lib/Nrrate/year_no_risk_return.csv"  # 无风险收益率年级
monthNoRiskReturn = "lib/Nrrate/month_no_risk_return.csv"  # 无风险收益率月级
dayNoRiskReturn = "lib/Nrrate/day_no_risk_return.csv"  # 无风险收益率日级



file = "TRD_Nrrate.csv"  # reader=csv.reader(f)


# 读取沪深300数据
def get_df_300return(period=Period):
    if period == YEAR:  # 读取年度数据
        df = pd.read_csv(yearReturn300, encoding='utf-8', delimiter=',')
    elif period == MONTH:  # 读取月度数据
        df = pd.read_csv(monthReturn300, encoding='utf-8', delimiter=',')
    else:  # 读取日数据
        df = pd.read_csv(dayReturn300, encoding='utf-8', delimiter=',')
    df[period] = pd.to_datetime(df[period])
    return df


'''读取无风险收益率数据 返回dataFrame'''

def get_no_risk_return(period=Period):
    if period == YEAR:  # 读取年度数据
        df = pd.read_csv(yearNoRiskReturn, encoding='utf-8', delimiter=',')
    elif period == MONTH:
        df = pd.read_csv(monthNoRiskReturn, encoding='utf-8', delimiter=',')
    else:
        df = pd.read_csv(dayNoRiskReturn, encoding='utf-8', delimiter=',')
    return df


'''方差计算'''
'''输入：开始节点 结束节点 数据周期'''
'''数据格式：第一列为时间，第二列为收益率，列名默认为return'''


def get_var_return(df, begin=Begin, end=End, period=Period, returnRow="return"):
    if period == YEAR:  # todo:
        df = df.loc[(df[period] >= begin) & (df[period] <= end)]
    elif period == MONTH:
        df = df.loc[(df[period] >= begin) & (df[period] <= end)]
    elif period == DAY:
        df = df.loc[(df[period] >= begin) & (df[period] <= end)]
        pass
    else:
        return 0
    # print(df) #debug用，查看样本数据
    return df[returnRow].var()


'''收益率均值计算 返回值为float'''
'''输入：开始节点 结束节点 数据周期 收益率列名'''
'''数据格式：第一列为时间，第二列为收益率，列名默认为return'''

def get_avg_return(df, begin=Begin, end=End, period=Period, returnRow="return"):
    if period == "year":  # todo:
        df = df.loc[(df[period] >= begin) & (df[period] <= end)]
    elif period == "month":
        df = df.loc[(df[period] >= begin) & (df[period] <= end)]
    elif period == "day":
        df = df.loc[(df[period] >= begin) & (df[period] <= end)]
    else:
        return 0
    # print(df) #debug用，查看样本数据
    return df[returnRow].mean()


df_300_year_return = get_df_300return(YEAR)
df_300_month_return = get_df_300return(MONTH)
df_300_day_return = get_df_300return(DAY)
df_day_no_risk_return=get_no_risk_return(DAY)
df_month_no_risk_return=get_no_risk_return(MONTH)
df_year_no_risk_return=get_no_risk_return(YEAR)


# print(df_300_month_return)
# print("-------------------------")
# print(df_300_year_return)



# df_year_return = pd.read_csv(yearReturn, encoding='utf-16le', delimiter='\t')
# col横 row竖

# print(df_300_year_return.describe)

#
# print(get_var_return(df_300_year_return, "2009/1/1", "2017/12/31", YEAR))
# print("---------------------------")
# print(get_var_return(df_300_month_return, "2009/12/01", "2017/12/31", MONTH))
# print("---------------------------")
# print(get_var_return(df_300_day_return, "2010/1/1", "2017/12/31", DAY))
# print(df_300_year_return['Year'])


def get_delta(begin=Begin, end=End, period=Period, returnRow="return"):
    df_no_risk_return = get_no_risk_return(period)
    df_market_return=get_df_300return(period)
    ERM = get_avg_return(df_market_return, begin, end, period)

    rf=get_avg_return(df_no_risk_return,begin,end,period,returnRow)
    var_market_return=get_var_return(df_market_return,begin,end,period,returnRow)
    delta=(ERM-rf)/var_market_return
    #调试
    print("ERM=",ERM)
    print("rf=",rf)
    print("var=",var_market_return)


    return delta

print("10-17年，年为周期")
print(get_delta(BEGIN,END,YEAR))
print("-----------------------")
print("10-17年，月为周期")
print(get_delta(BEGIN,END,MONTH))
print("-----------------------")
print("10-17年，日为周期")
print(get_delta(BEGIN,END,DAY))