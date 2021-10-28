"""
### 如何你使用了源代码，请保留作者名字###
wiringpi for python3
编辑：蔡春海
LED灯模块实验
LED灯工作只要有高电平或是低电平来驱动工作就可以
"""
# 导入wiringpi库
from wiringpi import *

# 设置全局接口模式为wPi模式
#wiringPiSetup()

# 设置全局接口模式为BCM模式
wiringPiSetupGpio()

# 设置当前使用的接口为输出模式
pinMode(18,OUTPUT)  ##如果使用18一定要注意，因为18口的输出电压只有2.04V，而不是3.3

# 编写闪烁灯
while(1):
    digitalWrite(18,0) #点亮7号针脚上的LED灯(这里由于电路设置原理也有可能是拉低，也就是给低电平的时候是点亮）
    delay(500) #延时500毫秒
    digitalWrite(18,1) #关闭7号针脚上的LED灯
    delay(500)
    print(digitalRead(26))