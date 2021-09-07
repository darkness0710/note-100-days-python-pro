import decimal
class Caculator:
    @staticmethod
    def excute(x_input, y):
        if y > 0 and y <= 1:
            x = Caculator.get_x_value_by_y(x_input, y)
        else:
            x = ''
            y = ''
        
        return {
            'x': x,
            'y': y
        }
    
    def get_x_value_by_y(x_input, y):
        if y == 1:
            x = int(x_input)
        else:
            count_number_after_dot_of_y = abs(decimal.Decimal(str(y)).as_tuple().exponent)
            count_number_after_dot_of_x = abs(decimal.Decimal(str(x_input)).as_tuple().exponent)

            if count_number_after_dot_of_x == count_number_after_dot_of_y:
                x = x_input
            if count_number_after_dot_of_x > count_number_after_dot_of_y:
                number_after_dot_of_x = str(decimal.Decimal(str(x_input))).split(".")[1]
                x = str(int(x_input)) + '.' + number_after_dot_of_x[slice(count_number_after_dot_of_y)]
            if count_number_after_dot_of_x < count_number_after_dot_of_y:
                bonus = count_number_after_dot_of_y - count_number_after_dot_of_x
                x = x_input
                # bonus_text = ''
                # for i in range(0, bonus):
                #     bonus_text += '0'
                # x = str(x_input) + bonus_text

            x = float(x)
        return x

# x = 9.67 và y = 1
print(Caculator.excute(9.67, 1))

# x = 9.67 và y = 0.1
print(Caculator.excute(9.67, 0.1))

# x = 9.67 và y = 0.01
print(Caculator.excute(9.67, 0.01))

# x = 9.67 và y = 0.001
print(Caculator.excute(9.67, 0.001))

# x = 9.6789 và y = 1
print(Caculator.excute(9.6789, 1))

# x = 9.6789 và y = 0.1
print(Caculator.excute(9.6789, 0.1))

# x = 9.6789 và y = 0.01
print(Caculator.excute(9.6789, 0.01))

# x = 9.6789 và y = 0.001
print(Caculator.excute(9.6789, 0.001))

# x = 9.6789 và y = 0.0001
print(Caculator.excute(9.6789, 0.0001))

# x = 9.6789 và y = 0.00001
print(Caculator.excute(9.6789, 0.00001))