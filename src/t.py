
def conduc(a):
    b=int(a/90)
    if(a>0):
        print("最小正角为：\t"+str(a%360)+"°")
        print("最大负角为：\t"+str(a%360-360)+"°")
        print("象限或轴线性：",end="\t")
        if(a%90!=0):
            if(b%4==1):
                print("属于第二象限\n");
            elif(b%4==2):
                print("属于第三象限\n");
            elif(b%4==3):
                print("属于第四象限\n");
            elif(b%4==0):
                print("属于第一象限\n");
        else:
            if((a/90)%4==0):
                print("终边落在x轴正半轴上\n")
            elif((a/90)%4==1):
                print("终边落在y轴正半轴上\n")
            elif((a/90)%4==2):
                print("终边落在x轴负半轴上\n")
            else:
                print("终边落在y轴负半轴上\n")
    else:
        conduc(a+360)
print("---------------------------------\n")
print("    欢迎使用角度定性分析工具！\n")
print("---------------------------------\n")
while(True):
    a=int(input("输入角度：\t"))
    conduc(a)
    print("---------------------------------\n")
