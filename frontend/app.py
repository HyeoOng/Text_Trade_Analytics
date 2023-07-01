import FinanceDataReader as fdr
import pandas as pd
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 문자 인코딩 설정 변경
app.config['JSON_AS_ASCII'] = False


@app.route('/daily_stock_data', methods=['GET'])
def get_stock_data():
    # 종목명 또는 종목 심볼을 쿼리 파라미터로 받기
    stock_name = request.args.get('stock_name')

    # 종목명 또는 종목 심볼을 이용하여 주식 데이터 가져오기
    start_date = '2023-01-01'
    end_date = '2023-06-15'

    # 종목명으로 검색
    stock_data = fdr.DataReader(stock_name, start=start_date, end=end_date, exchange='KRX')

    if stock_data is None or stock_data.empty:
        # 종목 심볼으로 검색
        stock_listing = fdr.StockListing('KRX')  # KRX 시장에서 종목 리스트를 가져옴
        symbol = stock_listing.loc[stock_listing['Name'] == stock_name, 'Code'].values
        if len(symbol) > 0:
            stock_data = fdr.DataReader(symbol[0], start=start_date, end=end_date, exchange='KRX')

    if stock_data is None or stock_data.empty:
        return jsonify({'error': 'Invalid stock_name'}), 404

    # 인덱스를 날짜로 변경
    stock_data.index = pd.to_datetime(stock_data.index)

    # 날짜 범위 생성하여 인덱스에 할당
    date_range = pd.date_range(start=start_date, end=end_date)
    stock_data = stock_data.reindex(date_range)

    # 인덱스 이름 변경 및 컬럼 추가
    stock_data.index.name = 'Date'
    stock_data.reset_index(inplace=True)

    # 날짜 데이터를 "YYYY-MM-DD" 형식으로 변환
    stock_data['Date'] = stock_data['Date'].dt.strftime('%y/%m/%d')

    # JSON 형식으로 변환하여 반환
    json_data = stock_data.to_json(orient='records', force_ascii=False)
    return jsonify(json_data)


@app.route('/weekly_stock_data', methods=['GET'])
def get_weekly_stock_data():
    # 종목명 또는 종목 심볼을 쿼리 파라미터로 받기
    stock_name = request.args.get('stock_name')

    # 종목명 또는 종목 심볼을 이용하여 주식 데이터 가져오기
    start_date = '2023-01-01'
    end_date = '2023-06-15'

    # 종목명으로 검색
    stock_data = fdr.DataReader(stock_name, start=start_date, end=end_date, exchange='KRX')

    if stock_data is None or stock_data.empty:
        # 종목 심볼으로 검색
        stock_listing = fdr.StockListing('KRX')  # KRX 시장에서 종목 리스트를 가져옴
        symbol = stock_listing.loc[stock_listing['Name'] == stock_name, 'Code'].values
        if len(symbol) > 0:
            stock_data = fdr.DataReader(symbol[0], start=start_date, end=end_date, exchange='KRX')

    if stock_data is None or stock_data.empty:
        return jsonify({'error': 'Invalid stock_name'}), 404

    # 인덱스를 날짜로 변경
    stock_data.index = pd.to_datetime(stock_data.index)

    # 주간 주식 데이터로 집계
    weekly_stock_data = stock_data.resample('W').agg({
        'Open': 'first',
        'High': 'max',
        'Low': 'min',
        'Close': 'last',
        'Volume': 'sum'
    })

    # 인덱스 이름 변경 및 컬럼 추가
    weekly_stock_data.index.name = 'Date'
    weekly_stock_data.reset_index(inplace=True)

    # 인덱스를 날짜로 변경
    stock_data.index = pd.to_datetime(stock_data.index)

    # 날짜 범위 생성하여 인덱스에 할당
    date_range = pd.date_range(start=start_date, end=end_date)
    stock_data = stock_data.reindex(date_range)


    # 날짜 데이터를 "YYYY-MM-DD" 형식으로 변환
    weekly_stock_data['Date'] = weekly_stock_data['Date'].dt.strftime('%y/%m/%d')

    json_data = weekly_stock_data.to_json(orient='records', force_ascii=False)
    return jsonify(json_data)

@app.route('/monthly_stock_data', methods=['GET'])
def get_monthly_stock_data():
    # 종목명 또는 종목 심볼을 쿼리 파라미터로 받기
    stock_name = request.args.get('stock_name')

    # 종목명 또는 종목 심볼을 이용하여 주식 데이터 가져오기
    start_date = '2020-01-01'
    end_date = '2023-06-15'

    # 종목명으로 검색
    stock_data = fdr.DataReader(stock_name, start=start_date, end=end_date, exchange='KRX')

    if stock_data is None or stock_data.empty:
        # 종목 심볼으로 검색
        stock_listing = fdr.StockListing('KRX')  # KRX 시장에서 종목 리스트를 가져옴
        symbol = stock_listing.loc[stock_listing['Name'] == stock_name, 'Code'].values
        if len(symbol) > 0:
            stock_data = fdr.DataReader(symbol[0], start=start_date, end=end_date, exchange='KRX')

    if stock_data is None or stock_data.empty:
        return jsonify({'error': 'Invalid stock_name'}), 404

    # 인덱스를 날짜로 변경
    stock_data.index = pd.to_datetime(stock_data.index)

    # 주간 주식 데이터로 집계
    monthly_stock_data = stock_data.resample('M').agg({
        'Open': 'first',
        'High': 'max',
        'Low': 'min',
        'Close': 'last',
        'Volume': 'sum'
    })

    # 인덱스 이름 변경 및 컬럼 추가
    monthly_stock_data.index.name = 'Date'
    monthly_stock_data.reset_index(inplace=True)

    # 인덱스를 날짜로 변경
    stock_data.index = pd.to_datetime(stock_data.index)

    # 날짜 범위 생성하여 인덱스에 할당
    date_range = pd.date_range(start=start_date, end=end_date)
    stock_data = stock_data.reindex(date_range)


    # 날짜 데이터를 "YYYY-MM-DD" 형식으로 변환
    monthly_stock_data['Date'] = monthly_stock_data['Date'].dt.strftime('%Y/%m')


    json_data = monthly_stock_data.to_json(orient='records', force_ascii=False)
    return jsonify(json_data)


@app.route('/quarterly_stock_data', methods=['GET'])
def get_quarterly_stock_data():
    # 종목명 또는 종목 심볼을 쿼리 파라미터로 받기
    stock_name = request.args.get('stock_name')

    # 종목명 또는 종목 심볼을 이용하여 주식 데이터 가져오기
    start_date = '2000-01-01'
    end_date = '2023-06-15'

    # 종목명으로 검색
    stock_data = fdr.DataReader(stock_name, start=start_date, end=end_date, exchange='KRX')

    if stock_data is None or stock_data.empty:
        # 종목 심볼으로 검색
        stock_listing = fdr.StockListing('KRX')  # KRX 시장에서 종목 리스트를 가져옴
        symbol = stock_listing.loc[stock_listing['Name'] == stock_name, 'Code'].values
        if len(symbol) > 0:
            stock_data = fdr.DataReader(symbol[0], start=start_date, end=end_date, exchange='KRX')

    if stock_data is None or stock_data.empty:
        return jsonify({'error': 'Invalid stock_name'}), 404

    # 인덱스를 날짜로 변경
    stock_data.index = pd.to_datetime(stock_data.index)

    # 주간 주식 데이터로 집계
    quarterly_stock_data = stock_data.resample('Q').agg({
        'Open': 'first',
        'High': 'max',
        'Low': 'min',
        'Close': 'last',
        'Volume': 'sum'
    })

    # 인덱스 이름 변경 및 컬럼 추가
    quarterly_stock_data.index.name = 'Date'
    quarterly_stock_data.reset_index(inplace=True)

    # 인덱스를 날짜로 변경
    stock_data.index = pd.to_datetime(stock_data.index)

    # 날짜 범위 생성하여 인덱스에 할당
    date_range = pd.date_range(start=start_date, end=end_date)
    stock_data = stock_data.reindex(date_range)

    # 인덱스 이름 변경 및 컬럼 추가
    # stock_data.index.name = 'Date'
    # stock_data.reset_index(inplace=True)

    # 날짜 데이터를 "YYYY-MM-DD" 형식으로 변환
    quarterly_stock_data['Date'] = quarterly_stock_data['Date'].dt.to_period('Q').astype(str)
    quarterly_stock_data['Date'] = quarterly_stock_data['Date'].str.replace('Q', '/Q')

    # JSON 형식으로 변환하여 반환 (UTF-8 인코딩 적용)
    # json_data = monthly_stock_data.to_json(orient='records', force_ascii=False).encode('utf-8')
    # return jsonify(json_data)

    json_data = quarterly_stock_data.to_json(orient='records', force_ascii=False)
    return jsonify(json_data)


@app.route('/yearly_stock_data', methods=['GET'])
def get_yearly_stock_data():
    # 종목명 또는 종목 심볼을 쿼리 파라미터로 받기
    stock_name = request.args.get('stock_name')

    # 종목명 또는 종목 심볼을 이용하여 주식 데이터 가져오기
    start_date = '2000-01-01'
    end_date = '2023-06-15'

    # 종목명으로 검색
    stock_data = fdr.DataReader(stock_name, start=start_date, end=end_date, exchange='KRX')

    if stock_data is None or stock_data.empty:
        # 종목 심볼으로 검색
        stock_listing = fdr.StockListing('KRX')  # KRX 시장에서 종목 리스트를 가져옴
        symbol = stock_listing.loc[stock_listing['Name'] == stock_name, 'Code'].values
        if len(symbol) > 0:
            stock_data = fdr.DataReader(symbol[0], start=start_date, end=end_date, exchange='KRX')

    if stock_data is None or stock_data.empty:
        return jsonify({'error': 'Invalid stock_name'}), 404

    # 인덱스를 날짜로 변경
    stock_data.index = pd.to_datetime(stock_data.index)

    # 주간 주식 데이터로 집계
    yearly_stock_data = stock_data.resample('Y').agg({
        'Open': 'first',
        'High': 'max',
        'Low': 'min',
        'Close': 'last',
        'Volume': 'sum'
    })

    # 인덱스 이름 변경 및 컬럼 추가
    yearly_stock_data.index.name = 'Date'
    yearly_stock_data.reset_index(inplace=True)

    # 인덱스를 날짜로 변경
    stock_data.index = pd.to_datetime(stock_data.index)

    # 날짜 범위 생성하여 인덱스에 할당
    date_range = pd.date_range(start=start_date, end=end_date)
    stock_data = stock_data.reindex(date_range)

    # 인덱스 이름 변경 및 컬럼 추가
    # stock_data.index.name = 'Date'
    # stock_data.reset_index(inplace=True)

    # 날짜 데이터를 "YYYY-MM-DD" 형식으로 변환
    yearly_stock_data['Date'] = yearly_stock_data['Date'].dt.strftime('%Y')

    json_data = yearly_stock_data.to_json(orient='records', force_ascii=False)
    return jsonify(json_data)



if __name__ == '__main__':
    app.run()
