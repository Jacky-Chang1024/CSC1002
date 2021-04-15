import turtle
turtle.setup(1.0,1.0)    #将画布设置成与电脑屏幕1:1的大小
#直角坐标系
turtle.speed(7)  #速度控制
turtle.dot(20,'red')
turtle.write('o',align='left',font=('Times New Roman',50))
turtle.pensize(3)
turtle.goto(700,0)
turtle.write('x',align='left',font=('Times New Roman',50))
turtle.goto(-700,0)
turtle.home()
turtle.goto(0,350)
turtle.write('y',align="left",font=('Times New Roman',50))
turtle.goto(0,-350)
turtle.mainloop()
# ————————————————
# 版权声明：本文为CSDN博主「catぁ」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/weixin_45082954/article/details/104547461