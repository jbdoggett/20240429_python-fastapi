import requests

def main() -> None:
    new_car = {"make":"horn", "model":"Accord", "year":1999,
               "color":"pale blue", "price":12345.67}
    resp = requests.post("http://127.0.0.1:8000/cars",json=new_car)
    print(resp.json())

if __name__ == "__main__":
    main()
