# yphinance

This is (currently) a test project to use small yet highly
efficient LLM's in combination with yfinance's api.</br>

## Example Using $BABA

Prompt
```python
messages=[{'role': 'user', 'content': f"""
               based on the info in {data}, 
               what is the general trend 
               of the stock, and is it a 
               good buy?
               
               give absolute advice, give objective
               answers. there is a correct answer
               give it."""}],
```

Output of ```data```
```txt
{'address1': '969 West Wen Yi Road', 'address2': 'Yu Hang District', 'city': 'Hangzhou', 'zip': '311121', 'country': 'China', 'phone': '86 571 8502 2088', 'fax': '86 571 8376 8429', 'website': 'https://www.alibabagroup.com', 'industry': 'Internet Retail', 'industryKey': 'internet-retail', 'industryDisp': 'Internet Retail', 'sector': 'Consumer Cyclical', 'sectorKey': 'consumer-cyclical', 'sectorDisp': 'Consumer Cyclical', 'longBusinessSummary': "Alibaba Group Holding Limited, through its subsidiaries, provides technology infrastructure and marketing reach to help merchants, brands, retailers, and other businesses to engage with their users and customers in the People's Republic of China and internationally. The company operates through seven segments: China Commerce, International Commerce, Local Consumer Services, Cainiao, Cloud, Digital Media and Entertainment, and Innovation Initiatives and Others. It operates Taobao, a digital retail platform; Tmall, a third-party online and mobile commerce platform; Alimama, a monetization platform; 1688.com and Alibaba.com, which are online wholesale marketplaces; AliExpress, a retail marketplace; Lazada, Trendyol, and Daraz that are e-commerce platforms; Freshippo, a retail platform for groceries and fresh goods; and Tmall Global, an import e-commerce platform. The company also operates Cainiao Network logistic services platform; Ele.me, an on-demand delivery and local services platform; Koubei, a restaurant and local services guide platform; and Fliggy, an online travel platform. In addition, it offers pay-for-performance, in-feed, and display marketing services; and Taobao Ad Network and Exchange, a real-time online bidding marketing exchange. Further, the company provides elastic computing, storage, network, security, database, big data, and IoT services; and hardware, software license, software installation, and application development and maintenance services. Additionally, it operates Youku, an online video platform; Quark, a platform for information search, storage, and consumption; Alibaba Pictures and other content platforms that provide online videos, films, live events, news feeds, literature, music, and others; Amap, a mobile digital map, navigation, and real-time traffic information app; DingTalk, a business efficiency mobile app; and Tmall Genie smart speaker. The company was incorporated in 1999 and is based in Hangzhou, the People's Republic of China.", 'fullTimeEmployees': 219260, 'companyOfficers': [{'maxAge': 1, 'name': 'Mr. Joseph C.  Tsai', 'age': 59, 'title': 'Executive Chairman', 'yearBorn': 1964, 'fiscalYear': 2018, 'exercisedValue': 0, 'unexercisedValue': 0}, {'maxAge': 1, 'name': 'Mr. Yongming  Wu', 'age': 48, 'title': 'CEO, Head of Core E-Commerce Business & Director', 'yearBorn': 1975, 'fiscalYear': 2018, 'exercisedValue': 0, 'unexercisedValue': 0}, {'maxAge': 1, 'name': 'Mr. J. Michael  Evans', 'age': 65, 'title': 'President & Director', 'yearBorn': 1958, 'fiscalYear': 2018, 'exercisedValue': 0, 'unexercisedValue': 0}, {'maxAge': 1, 'name': 'Mr. Hong  Xu', 'age': 50, 'title': 'Chief Financial Officer', 'yearBorn': 1973, 'fiscalYear': 2018, 'exercisedValue': 0, 'unexercisedValue': 0}, {'maxAge': 1, 'name': 'Ms. Joan  Zhou', 'title': 'Investment Director', 'fiscalYear': 2018, 'exercisedValue': 0, 'unexercisedValue': 0}, {'maxAge': 1, 'name': 'Mr. Yuen Jen Yao', 'title': 'Senior VP & Head of Corporate Finance', 'fiscalYear': 2018, 'exercisedValue': 0, 'unexercisedValue': 0}, {'maxAge': 1, 'name': 'Mr. Zeming  Wu', 'age': 43, 'title': 'Chief Technology Officer', 'yearBorn': 1980, 'fiscalYear': 2018, 'exercisedValue': 0, 'unexercisedValue': 0}, {'maxAge': 1, 'name': 'Mr. Robert  Lin', 'title': 'Investor Relations', 'fiscalYear': 2018, 'exercisedValue': 0, 'unexercisedValue': 0}, {'maxAge': 1, 'name': 'Ms. Siying  Yu', 'age': 49, 'title': 'General Counsel', 'yearBorn': 1974, 'fiscalYear': 2018, 'exercisedValue': 0, 'unexercisedValue': 0}, {'maxAge': 1, 'name': 'Ms. Jane  Jiang', 'title': 'Chief People Officer', 'fiscalYear': 2018, 'exercisedValue': 0, 'unexercisedValue': 0}], 'compensationAsOfEpochDate': 1546214400, 'maxAge': 86400, 'priceHint': 2, 'previousClose': 70.62, 'open': 70.02, 'dayLow': 69.29, 'dayHigh': 70.105, 'regularMarketPreviousClose': 70.62, 'regularMarketOpen': 70.02, 'regularMarketDayLow': 69.29, 'regularMarketDayHigh': 70.105, 'dividendRate': 1.0, 'dividendYield': 0.014199999, 'exDividendDate': 1703030400, 'payoutRatio': 0.1831, 'beta': 0.46, 'trailingPE': 13.0510845, 'forwardPE': 8.272903, 'volume': 10049697, 'regularMarketVolume': 10049697, 'averageVolume': 18053198, 'averageVolume10days': 14667110, 'averageDailyVolume10Day': 14667110, 'bid': 69.72, 'ask': 69.73, 'bidSize': 800, 'askSize': 1100, 'marketCap': 172888096768, 'fiftyTwoWeekLow': 66.63, 'fiftyTwoWeekHigh': 102.5, 'priceToSalesTrailing12Months': 0.18640347, 'fiftyDayAverage': 73.5112, 'twoHundredDayAverage': 81.1024, 'trailingAnnualDividendRate': 6.869, 'trailingAnnualDividendYield': 0.09726706, 'currency': 'USD', 'enterpriseValue': 1128346025984, 'profitMargins': 0.10813, 'floatShares': 16405800000, 'sharesOutstanding': 2433629952, 'sharesShort': 41561483, 'sharesShortPriorMonth': 47524895, 'sharesShortPreviousMonthDate': 1709164800, 'dateShortInterest': 1711584000, 'sharesPercentSharesOut': 0.0166, 'heldPercentInsiders': 0.00016000001, 'heldPercentInstitutions': 0.14807001, 'shortRatio': 3.05, 'impliedSharesOutstanding': 2557019904, 'bookValue': 404.236, 'priceToBook': 0.17272906, 'lastFiscalYearEnd': 1680220800, 'nextFiscalYearEnd': 1711843200, 'mostRecentQuarter': 1703980800, 'earningsQuarterlyGrowth': -0.69, 'netIncomeToCommon': 99986997248, 'trailingEps': 5.35, 'forwardEps': 8.44, 'pegRatio': 42.26, 'enterpriseToRevenue': 1.217, 'enterpriseToEbitda': 6.21, '52WeekChange': -0.26044613, 'SandP52WeekChange': 0.21828604, 'lastDividendValue': 1.0, 'lastDividendDate': 1703030400, 'exchange': 'NYQ', 'quoteType': 'EQUITY', 'symbol': 'BABA', 'underlyingSymbol': 'BABA', 'shortName': 'Alibaba Group Holding Limited', 'longName': 'Alibaba Group Holding Limited', 'firstTradeDateEpochUtc': 1411133400, 'timeZoneFullName': 'America/New_York', 'timeZoneShortName': 'EDT', 'uuid': '8d2bbbd9-9979-370d-8c45-f5246fdce510', 'messageBoardId': 'finmb_42083601', 'gmtOffSetMilliseconds': -14400000, 'currentPrice': 69.8233, 'targetHighPrice': 145.93, 'targetLowPrice': 79.96, 'targetMeanPrice': 106.33, 'targetMedianPrice': 107.95, 'recommendationMean': 1.8, 'recommendationKey': 'buy', 'numberOfAnalystOpinions': 41, 'totalCash': 614399016960, 'totalCashPerShare': 30.72, 'ebitda': 181685993472, 'totalDebt': 198505005056, 'quickRatio': 1.369, 'currentRatio': 1.799, 'totalRevenue': 927493980160, 'debtToEquity': 17.376, 'revenuePerShare': 363.638, 'returnOnAssets': 0.044320002, 'returnOnEquity': 0.08206, 'freeCashflow': 146286379008, 'operatingCashflow': 190654005248, 'earningsGrowth': -0.684, 'revenueGrowth': 0.051, 'grossMargins': 0.37905997, 'ebitdaMargins': 0.19589001, 'operatingMargins': 0.11908, 'financialCurrency': 'CNY', 'trailingPegRatio': 0.5701}
```

Dolphin-Phi's analysis from the data
```text
The general trend of the stock is decreasing, as indicated by the 'priceToSalesTrailing12Months' value of 0.18640347, which shows that the price to sales ratio has been declining over time. The stock can be considered a bad buy due to its low book-to-market ratio (0.17272906) and declining earnings growth (minus 0.684 in this case). Additionally, the lack of dividends further supports the notion that it is not a good investment at this point.
```

## Installing / Getting started

Make sure you have [Ollama](ollama.com) installed onto your system.</br>

Install dolphin-phi
 ```shell
ollama run dolphin-phi
```

Clone repo
```shell
git clone https://github.com/KennethChilds/yphinance
```

Install dependencies

```shell
pip install -r requirements.txt
```

## Configuration

To use another LLM, run
```shell
ollama run <LLM_HERE>
```
edit the ```main.py``` file to use your LLM of choice.

```python
stream = ollama.chat(
    model='<LLM_HERE>',
    messages=[{'role': 'user', 'content': 'EXAMPLE_PROMPT'],
    stream=True,
)
```
