'''
6 kyu
Name: Ease the StockBroker

https://www.codewars.com/kata/54de3257f565801d96001200/python
Task: Clients place orders to a stockbroker as strings. The order can be simple or multiple or empty.

Type of a simple order: Quote/white-space/Quantity/white-space/Price/white-space/Status

where Quote is formed of non-whitespace character, Quantity is an int, Price a double (with mandatory decimal point "." ), 
Status is represented by the letter B (buy) or the letter S (sell).
'''


def balance_statement(lst):
    error = list()
    buy = 0
    sell = 0
    for order in lst.split(", "):
        temp = order.split(" ")

        if len(temp) == 4:

            if temp[2].count(".") == 1:
                temp2 = temp[2].split(".")
                if temp2[1] == "":
                    error.append(order)
                    continue
                if temp2[0] == "": temp2[0] = 0
            else:
                error.append(order)
                continue

            if not temp[1].isdigit() or (temp[3].find("B") == 0 or temp[3].find("S") == 0) == False:
                error.append(order)
                continue

            if temp[3] == "B":
                buy += int(temp[1]) * float(temp[2])
            else:
                sell += int(temp[1]) * float(temp[2])

        else:
            error.append(order)

    return "Buy: {} Sell: {}".format(round(buy), round(sell)) if len(error) == 0 or len(
        lst) == 0 else "Buy: {} Sell: {}; Badly formed {}: {} ;".format(round(buy), round(sell), len(error),
                                                                        " ;".join(error))