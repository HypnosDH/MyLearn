import random
answer = random.randint(1 , 10)
guess = eval(input("請猜一個數字(1~10) ："))
while guess != answer:
    if guess > answer:
        print("太大了，小一點！")
    else:
        print("太小了，大一點！")
    guess = eval(input("請猜一個數字(1~10) ："))
else:
    print("恭喜！猜對了！")

