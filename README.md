# yphinance

This is (currently) a test project to use small yet highly
efficient LLM's in combination with yfinance's api.</br>

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
