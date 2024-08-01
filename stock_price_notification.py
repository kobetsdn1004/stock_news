import yfinance as yf
import requests
import os
from datetime import datetime
import pytz

def send_line_notify(message):
    line_notify_token = os.environ['LINE_NOTIFY_TOKEN']
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {line_notify_token}'}
    data = {'message': message}
    try:
        response = requests.post(line_notify_api, headers=headers, data=data)
        if response.status_code == 200:
            print(f"Line Notify sent. Status code: {response.status_code}")
        else:
            print(f"Failed to send Line Notify. Status code: {response.status_code}, Response: {response.text}")
    except Exception as e:
        print(f"Error sending Line Notify: {e}")

# 股票代碼列表
stocks = ['0050.TW', '00929.TW', '2883.TW', '2330.TW', '2324.TW', '2357.TW', '2382.TW', '2376.TW']
													  

def get_stock_info(symbol):
    import yfinance as yf
import requests
import os
from datetime import datetime
import pytz

def send_line_notify(message):
    line_notify_token = os.environ['LINE_NOTIFY_TOKEN']
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {line_notify_token}'}
    data = {'message': message}
    try:
        response = requests.post(line_notify_api, headers=headers, data=data)
        if response.status_code == 200:
            print(f"Line Notify sent. Status code: {response.status_code}")
        else:
            print(f"Failed to send Line Notify. Status code: {response.status_code}, Response: {response.text}")
    except Exception as e:
        print(f"Error sending Line Notify: {e}")

# 股票代碼列表
stocks = ['0050.TW', '00929.TW', '2883.TW', '2330.TW', '2324.TW', '2357.TW', '2382.TW', '2376.TW']
													  

def get_stock_info(symbol):
    url = f"https://mis.twse.com.tw/stock/api/getStockInfo.jsp?ex_ch=tse_{symbol.replace('.TW', '')}.tw"
    try:
        response = requests.get(url)
        data = response.json()
        if data and data['msgArray']:
            stock_name = data['msgArray'][0]['n']
        else:
            stock_name = "未知股票"
    except Exception as e:
        stock_name = "未知股票"
        print(f"獲取股票名稱時出錯: {e}")
    return stock_name, current_price, percentage

# 取得今天的日期
today = datetime.now().strftime("%Y年%m月%d日")
message = f"\n今天日期{today} 股價通知:\n\n"


for stock in stocks:
    try:
        name, price, percentage = get_stock_info(stock)
        message += f"{name} ({stock}): 當前價格 {price:.2f}, 相對最高點 {percentage:.2f}%\n"
    except Exception as e:
        print(f"獲取股票 {stock} 數據時出錯: {e}")
        message += f"{stock}: 無法獲取數據\n"


# 發送 LINE 通知
print(message) # 打印整個內容以便調試
send_line_notify(message)
, current_price, percentage

# 取得今天的日期
today = datetime.now().strftime("%Y年%m月%d日")
message = f"\n今天日期{today} 股價通知:\n\n"


for stock in stocks:
    try:
        name, price, percentage = get_stock_info(stock)
        message += f"{name} ({stock}): 當前價格 {price:.2f}, 相對最高點 {percentage:.2f}%\n"
    except Exception as e:
        print(f"獲取股票 {stock} 數據時出錯: {e}")
        message += f"{stock}: 無法獲取數據\n"


# 發送 LINE 通知
print(message) # 打印整個內容以便調試
send_line_notify(message)
