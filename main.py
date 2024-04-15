import ollama
import yfinance as yf

msft = yf.Ticker("MSFT")

data = yf.download("MSFT", period="1mo")
    
# streaming ai respone w/ dolphin-phi
stream = ollama.chat(
    model='dolphin-phi',
    messages=[{'role': 'user', 'content': f"""
               based on the info in {data}, 
               what is the general trend of the price?"""}],
    stream=True,
)

for chunk in stream:
  print(chunk['message']['content'], end='', flush=True)