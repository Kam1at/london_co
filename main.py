#!/usr/bin/env python3
london_co = {
    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1"
    },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2"
    },
    "sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True
    }
}


def main():
    res = ""
    
    inp_name = input('Введите имя устройства: ')

    for k, v in london_co.items():
        if inp_name == k:
            res = v

    inp_par = input(f'Введите имя параметра {list(res.keys())}: ').lower()

    if inp_par in res.keys():
        for z, x in res.items():
            if inp_par == z:
                print(x)
    else:
        print('Такого параметра нет.')


main()

