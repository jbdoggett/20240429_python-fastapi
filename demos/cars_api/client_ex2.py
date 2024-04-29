import requests

def main() -> None:
    new_car = {"make":"Ford", "model":"Bronco", "year":1975, "color":"jet blue", "price":1234.56}
    resp = requests.post("http://127.0.0.1:8000/cars",json=new_car)
    print(resp.json())

if __name__ == "__main__":
    main()
