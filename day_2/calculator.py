class Caculator:
    @staticmethod
    def excute(x_input, y):
        if y > 0 and y <= 1:
            if y == 0.1:
                x = Caculator.get_x_value(x_input, 9.6)
            elif y == 1:
                x = Caculator.get_x_value(x_input, 9)
            elif y == 0.001:
                x = Caculator.get_x_value(x_input, 9.67)
        else:
            x = ''
            y = ''
        
        return {
            'x': x,
            'y': y
        }
    
    def get_x_value(x_input, x_caculator):
        return x_input if x_caculator > x_input else x_caculator

# # x = 10 và y = 1
print(Caculator.excute(10, 1))

# # x = 1 và y = 1
print(Caculator.excute(1, 1))

# # x = 1 và y = 2
print(Caculator.excute(1, 2))