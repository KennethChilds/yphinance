import ollama
import yfinance as yf

stocks = yf.Ticker("baba")

data = stocks.info

    
# streaming ai respone w/ dolphin-phi
stream = ollama.chat(
    model='dolphin-phi',
    messages=[{'role': 'user', 'content': f"""
               based on the info in {data}, 
               what is the general trend 
               of the stock, and is it a 
               good buy?
               
               give absolute advice, give objectiv
               answers. there is a correct answer
               give it."""}],
    stream=True,
)
print(data, "\n")
for chunk in stream:
  print(chunk['message']['content'], end='', flush=True)