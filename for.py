import pio
n=int(input("测试次数："))
i=1
for i in range(n):
    pio.pio()
    i+=1
    print ("第",i,"次循环")
print ("测试完成")