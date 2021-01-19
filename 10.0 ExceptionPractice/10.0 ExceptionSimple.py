try:
    n1 = eval(input("請輸入被除數："))
    n2 = eval(input("請輸入除數："))
    result = n1 / n2

except ZeroDivisionError:
    print("除數不可為 0，請重新輸入")
else:
    print("計算結果為:{}".format(result))
finally:
    print("謝謝您的使用！！")