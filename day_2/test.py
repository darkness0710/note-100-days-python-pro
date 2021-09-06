import re

def get_data_coin(input):
    response = {
        'gia_mua': '',
        'gia_sl': '',
        'tp2': ''
    }
    try:
        arr = input.split('\n')
        response = {
            'gia_mua': '',
            'gia_sl': '',
            'tp2': ''
        }
        for value in arr:
            if 'Gia Mua' in value: # Check string "Gia Mua" có tồn tại trong chuỗi hay không?
                response['gia_mua'] = re.findall("\d+\.\d+", value)[0]
            if 'Gia SL' in value: # Check string "Gia SL" có tồn tại trong chuỗi hay không?
                response['gia_sl'] = re.findall("\d+\.\d+", value)[0]
            if 'TP2' in value: # Check string "TP2" có tồn tại trong chuỗi hay không?
                response['tp2'] = re.findall("\d+\.\d+", value)[0]
        return response
    except :
        return response

input = "✅ Symbol:  UNIUSDT\n ⏰ Thời gian vào lệnh:  9/6/2021 10:31:54 AM \n ▶️ Gia Mua:  30.04000000 \n ⏸ Gia SL :  27.0 \n ⏹ TP1:   31.5 \n ⏹ TP2:  34.5 \n ⏹ TP3:  39.1 \n ⏹ TP4:  45.1 \n ⏹ TP5:  60.1"
print(get_data_coin(input))
# B1. Lặp qua các dòng của text dựa vào giá trị xuống dòng \n
# B2. Kiểm tra dòng đó chứa kí tự cần tìm hay không?
# B3. Dùng regex lấy giá trị float trong chuỗi
# re.findall("\d+\.\d+", value)[0] -> Trả về mảng dữ liệu chứa giá trị float. Ví du:
# "TP2: 12.1" => Check chuỗi chứa TP2 sau đó trả về dạng mảng [12.1] và chúng ta cần lấy phần tử đầu tiên của mảng -> [12.1][0]