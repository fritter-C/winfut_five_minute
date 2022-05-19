import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def main():
    winfut = pd.read_csv('winfut_five_minute.csv', sep=';')
    print(winfut.columns)
    winfut.Data = pd.to_datetime(winfut['Data'], format='%d/%m/%Y %H:%M')

    winfut['trading_day'] = [d.date() for d in winfut['Data']]
    trading_days = winfut.groupby(winfut.trading_day)

    x = []
    for group in trading_days.groups:
        aux = trading_days.get_group(group)
        high = aux['High'].max()
        low = aux['Low'].min()
        aux2 = ((aux.loc[aux['High'] == high]).iloc[-1])
        aux3 = ((aux.loc[aux['Low'] == low]).iloc[-1])

        # se for um dia de baixa adiciona a máxima do dia senão adiciona a mínima
        if aux['Open'].iloc[-1] > aux['Close'].iloc[0]:
            x.append(aux2['Candle'])
        else:
            x.append(aux3['Candle'])

    # specifying figure size
    fig = plt.figure(figsize=(10, 4))

    # adding sub plots
    ax1 = fig.add_subplot(1, 2, 1)

    # adding sub plots
    ax2 = fig.add_subplot(1, 2, 2)

    xl = np.unique(x)
    print(xl)
    y = []
    for value in xl:
        y.append(x.count(value))

    norm = [i / max(y) for i in y]
    lo = np.array(y)

    lo = lo.cumsum()
    print(y)
    print(x)
    ax1.bar(xl, norm, color="green")
    ax2.bar(xl, lo / lo.max(), color="blue")
    plt.show()


if __name__ == '__main__':
    main()
