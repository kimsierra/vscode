import pandas as pd
import numpy as np
from datetime import datetime

def create_band(
        _df, _col = 'Adj Close', 
        _start = "2010-01-01",
        _end = datetime.now(),
        _cnt = 20):
    df = _df.copy()
    # 인텍스가 Date인가?
    if 'Date' in df.columns:
        df.set_index('Date', inplace=True)

    # index를 시계열 데이터로 변경
    df.index = pd.to_datetime(df.index, format = "%Y-%m-%d")

    # 시작시간과 종료시간을 시계열로 변경
    try:
        start = datetime.strptime(_start, "%Y-%m-%d")
        if type(_end) == "str":
            _end = datetime.strptime(_end, '%Y-%m-%d')
        else:
            end = _end
    except:
        return "인자값의 타입이 잘못되었습니다.(예 : YYYY-mm-dd)"
    
    # 결측치와 무한대 값을 제외
    flag = df.isin([np.nan, np.inf, -np.inf]).any(axis=1)
    df = df.loc[~flag,]

    # 기준이 되는 컬럼을 제외하고 모두 삭제
    result = df[[_col]]

    # 이동평균선, 상단밴드, 하단밴드 생성
    result['center'] = result[_col].rolling(_cnt).mean()
    result['ub'] = result['center'] + (2 *result[_col].rolling(_cnt).std())
    result['lb'] = result['center'] - (2 *result[_col].rolling(_cnt).std())

    # 시작시간과 종료시간으로 필터링
    result = result.loc[start:end,]

    return result


def create_trade(_df):
    # 기준이 되는 컬럼의 이름을 변수에 저장
    col = _df.columns[0]

    df = _df.copy()

    # 거래 내역이라는 컬럼을 생성
    df['trade'] = ""

    # 거래 내역 추가
    for i in df.index:
        # 상단밴드보다 기준이 되는 컬럼의 값이 높거나 같은 경우
        if df.loc[i,col] >= df.loc[i, 'ub']:
            df.loc[i, 'trade']= ""
        # 하단밴드보다 col의 값이 작거나 같은 경우
        elif df.loc[i, col] <= df.loc[i, 'lb']:
            df.loc[i, 'trade'] = "buy"
        #밴드 사이에 col의 값이 존재한다면
        else:
            df.loc[i,'trade'] = df.shift().loc[i, 'trade']
    return df


def create_rtn(_df):
    # 기준이 되는 컬럼을 변수에 저장
    col = _df.columns[0]
    # 복사본 생성
    df = _df.copy()
    # 수익률 파생변수 생성
    df['rtn'] = 1

    # 수익률 계산하는 반복문
    for i in df.index:
        # 구매한 날
        if (df.shift().loc[i, 'trade']=='')&(df.loc[i, 'trade']=='buy'):
            buy = df.loc[i, col]
            print(f"매수일 : {i}, 매수가 : {buy}")
        # 판매한 날
        elif (df.shift().loc[i,'trade']=='buy')&(df.loc[i,'trade']== ""):
            sell = df.loc[i,col]
            rtn = sell / buy
            print(f"매도일 : {i}, 매도가 : {sell}, 수익률 : {rtn}")
            df.loc[i,'rtn'] = rtn
    # 누적 수익률 계산
    df['acc_rtn'] = df['rtn'].cumprod()
    acc_rtn = df.iloc[-1,]['acc_rtn']
    return df, acc_rtn