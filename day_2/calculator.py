import decimal
class Caculator:
    @staticmethod
    def excute(x_input, y):
        if y > 0 and y <= 1:
            x = Caculator.get_x_value_by_y(x_input, y)
            if x >= y:
                x = Caculator.get_max_of_x(x, y)
            else:
                x = ''
                y = ''    
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
    
    def get_max_of_x(x, y):
        count = 1
        while (True):
            tmp_y = count * y
            if tmp_y > x:
                x = (count - 1) * y
                break
            count += 1
        
        return x



# x = 7.89 và y = 0.02
print(Caculator.excute(7.89, 0.02))

# x = 2.2222 và y = 0.99
print(Caculator.excute(2.2222, 0.99))
