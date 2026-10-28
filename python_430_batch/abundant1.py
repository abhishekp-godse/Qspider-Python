def sum_of_divisor(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum+=i
            return sum
        
def check_num(num):
    if sum_of_divisor(num)>num:
        return"abundant"
    elif sum_of_divisor(num)<num:
        return"deficient"
    else:
        return "perfect"

    print (check_num(12))
    print (check_num(6))
    print (check_cnum(5))

    num=int(input("Enter a number\n"))
    
    print (check_num(num))