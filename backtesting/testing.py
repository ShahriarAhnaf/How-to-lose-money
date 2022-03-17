from backtesting import Backtest, Strategy
from backtesting.lib import crossover

from backtesting.test import SMA, GOOG


class SmaCross(Strategy):
    def init(self):
        price = self.data.Close
        self.ma1 = self.I(SMA, price, 10)
        self.ma2 = self.I(SMA, price, 20)

    def next(self):
        if crossover(self.ma1, self.ma2):
            self.buy()
        elif crossover(self.ma2, self.ma1):
            self.sell()


class EmaCross(Strategy):
    def init(self):
        price = self.data.Close
        self.ma1 = self.I(EMA, price, 5)
        self.ma2 = self.I(EMA, price, 20)

    def next(self):
        if crossover(self.ma1, self.ma2):
            self.buy()
        elif crossover(self.ma2, self.ma1):
            self.sell()


bt = Backtest(GOOG, SmaCross,
              exclusive_orders=True)
#ebt = Backtest(GOOG, EmaCross,
 #             exclusive_orders=True)

stats = bt.run()
print(stats)

#leStats = ebt.run()
bt.plot()
#ebt.plot()

