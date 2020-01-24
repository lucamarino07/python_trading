from __future__ import (absolute_import, division, print_function, unicode_literals)

import backtrader as bt
import backtrader.indicators as btind
import backtrader.analyzers as btanalyzers
import datetime
import os.path
import sys


class Cross_Medie(bt.Strategy):
    params = (('Med_vel', 50), ('Med_len', 100))

    def __init__(self):
        self.sma_vel = btind.SMA(period=self.p.Med_vel)
        self.sma_len = btind.SMA(period=self.p.Med_len)

        self.buysig = btind.CrossOver(self.sma_vel, self.sma_len)

        self.dataclose = self.datas[0].close

    def next(self):
        if self.position.size:
            if self.buysig < 0:
                self.close()
                self.sell()
            elif self.buysig > 0:
                self.close()
                self.buy()
        else:
            if self.buysig > 0:
                self.buy()
            elif self.buysig < 0:
                self.sell()

    def stampa(self, txt, dt=None):
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            return
        if order.status in [order.Completed]:
            if order.isbuy():
                self.stampa('ACQ ESEGUITO, QTY: %.2f, PREZZO: %.2f, COSTO: %.2f, COMM %.2f' % (
                    order.executed.size,
                    order.executed.price,
                    order.executed.value,
                    order.executed.comm
                ))

                self.buyprice = order.executed.price
                self.buycomm = order.executed.comm
            else:
                self.stampa('VEND ESEGUITO, QTY: %.2f, PREZZO: %.2f, COSTO: %.2f, COMM %.2f' % (
                    order.executed.size,
                    order.executed.price,
                    order.executed.value,
                    order.executed.comm
                ))

            self.bar_executed = len(self)

        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.stampa('Ordine Cancellato')

        self.order = None

    def notify_trade(self, trade):
        if not trade.isclosed:
            return
        self.stampa('PROFITTO OPERAZIONE, LORDO %.2f, NETTO %.2f' %
                    (trade.pnl, trade.pnlcomm))

if __name__ == '__main__':
    cerebro = bt.Cerebro()

    cerebro.addstrategy(Cross_Medie)

    capitale_iniziale = 100000


    import pandas as pd
    modpath = os.path.basename(os.path.abspath(sys.argv[0]))
    datapath = 'ISP.csv'
    print(pd.read_csv(datapath))

    data = bt.feeds.YahooFinanceCSVData(
        dataname=datapath,
        fromdate=datetime.datetime(2015, 1, 1),
        todate=datetime.datetime(2018, 12, 31),
        reverse=False
    )

    cerebro.adddata(data)
    cerebro.broker.setcash(capitale_iniziale)
    cerebro.addsizer(bt.sizers.FixedSize, stake=1000)
    cerebro.broker.setcommission(commission=0.0002)

    print('Valore iniziale Portafoglio: %.2f' % cerebro.broker.getvalue())

    cerebro.run()
    print('Valore Finale Portafoglio: %.2f' % cerebro.broker.getvalue())


