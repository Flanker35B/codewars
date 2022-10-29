'''
8 kyu
Name: USD => CNY
https://www.codewars.com//kata/5977618080ef220766000022
Task: Create a function that converts US dollars (USD) to Chinese Yuan (CNY) . The input is the amount of USD as an 
integer, and the output should be a string that states the amount of Yuan followed by 'Chinese Yuan'


The conversion rate you should use is 6.75 CNY for every 1 USD. All numbers should be represented as a string with 2 
decimal places. (e.g. "21.00" NOT "21.0" or "21")
'''

def usdcny(usd):
    return str("%.2f" % round(usd*6.75,2)) + " Chinese Yuan"