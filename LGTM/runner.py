from src import pp 
import requests
if __name__ == "__main__":
    print("hello")
    res = requests.get('https://httpbin.org/get',
                   params={'q': 'python'})
    pp(res.json())