from flask import Flask, request, Response
import robin_stocks.robinhood as r


app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def respond():
    print(request.json);
    h = False
    if request.json['S']=='BUY':
        if h==True:
            return Response(status=502)
        r.order_buy_crypto_by_quantity('DOGE', 1070)
        h = False
    elif request.json['S']=='SELL':
        if h==False:
            return Response(status=502)
        r.order_sell_crypto_by_quantity('DOGE', 1060) 
        h = True;
    return Response(status=200)


if __name__ == '__main__':
    r.login('username@gmail.com','password')
    app.run(host='0.0.0.0',port=80, debug=True) # tradingview only support port 80, port needs to be open on your firewall
