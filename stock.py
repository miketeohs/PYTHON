import requests
import json
# https://stackoverflow.com/questions/72736578/how-to-get-live-stock-price
def get_stock_price(symbol):
        """get a stock price from yahoo finance"""

            url = "https://query1.finance.yahoo.com/v7/finance/quote?symbols=" + symbol
                headers = {'User-Agent': 'Mozilla/5.0'}
                    response = requests.get(url, headers=headers)
                        data = json.loads(response.text)

                                return data['quoteResponse']['result'][0]['regularMarketPrice']


                            print(get_stock_price('AAPL'))
