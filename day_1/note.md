# Refer course
https://www.udemy.com/course/100-days-of-code/

# Quiz start

### Question 1:
- What's the output for the following code?
`print(len("95637+12"))`
    - A. 15
    - B. 95649
    - **C. 8**
    - D. 95659
    - E. I don't know

> Hàm len đếm số phần tử trong chuỗi => Đáp án là 8


### Question 2:
- Read the code below, what will be printed in the output?
    ```
    score = 67
    if score < 80 and score > 70:
        print("A")
    elif score < 90 or score > 80:
        print("B")
    elif score > 60:
        print("C")
    else:
        print("D")
    ```
    - A
    - **B**
    - C
    - D

> Để ý phép OR

### Question 3:
- Read the code below, what will be printed in the output?
    ```
    def a_function(a_parameter):    
        a_variable = 15    
        return a_parameter 
    a_function(10)
    print(a_variable)
    ```
    - **NameError**
    - 5
    - 10
    - 15

> Chưa khai báo biến ...

### Question 4:
- Read the code below, what will be printed in the output?
    ```
    def outer_function(a, b):
      def inner_function(c, d):
        return c + d
      return inner_function(a, b)
 
    result = outer_function(5, 10)
    print(result)
    ```
    - SyntaxError
    - 5
    - **15**
    - (5, 10)

### Question 5:
- Read the code below, what will be printed in the output?
    ```
    Given a Car Class has the following attributes and methods, which line of code in the answers will produce an error?
    Attributes:
        num_of_seats
        speed
    Methods:
        drive()
        break()
    ```
    - car.drive()
    - car.num_of_seats = 2
    - **car.break = 0**
    - print(car.speed)

### Question 6:
- What word would you use to describe my_toyota and my_fiat?
    ```
    my_toyota = Car()
    my_fiat = Car()
    ```
    - Class
    - Attribute
    - **Object**
    - Method

### Question 7:
- What is the output of this code?
    ```
    def foo(a, b=4, c=6):
    print(a, b, c)
 
    foo(20, c=12)
    ```
    - 20, 4, 6
    - No output
    - 20, 12
    - **20, 4, 12**

### Question 8:
- What is the output of this code?
    ```
    def all_aboard(a, *args, **kw): 
    print(a, args, kw)
 
    all_aboard(4, 7, 3, 0, x=10, y=64)
    ```
    - 4 (7, 3, 0) {10, 64}
    - 4 7 3 0 {'x': 10, 'y': 64}
    - **4 (7, 3, 0) {'x': 10, 'y': 64}**
    - 4, 7, 3, 0, x=10, y=64