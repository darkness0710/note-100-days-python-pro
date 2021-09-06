import re



def get_data_coin(input):
    try:
        arr = input.split('\n')
        response = {
            'gia_mua': '',
            'gia_sl': '',
            'tp2': ''
        }
        for value in arr:
            if 'Gia Mua' in value:
                response['gia_mua'] = re.findall("\d+\.\d+", value)[0]
            if 'Gia SL' in value:
                response['gia_sl'] = re.findall("\d+\.\d+", value)[0]
            if 'TP2' in value:
                response['tp2'] = re.findall("\d+\.\d+", value)[0]
        return response
    except :
        return False

input = "✅ Symbol:  UNIUSDT\n ⏰ Thời gian vào lệnh:  9/6/2021 10:31:54 AM \n ▶️ Gia Mua:  30.04000000 \n ⏸ Gia SL :  27.0 \n ⏹ TP1:   31.5 \n ⏹ TP2:  34.5 \n ⏹ TP3:  39.1 \n ⏹ TP4:  45.1 \n ⏹ TP5:  60.1"
input_test = "✅Gia Mua:  30.04000000"

print(get_data_coin(input))
print(get_data_coin(input_test))