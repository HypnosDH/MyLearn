x = 5
y = 10

def func():
    global x
    x = 17
    y = 21
    print("x = %s, y=%s" %(x , y))

print("out func x = %s, y=%s" %(x , y))
func()
print("out func x = %s, y=%s" %(x , y))