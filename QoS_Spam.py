basevalue = 200
intfNumber = '4'

countycount = 300
seqno = 0
while seqno < countycount:
    seqno +=1
    value = str(seqno+basevalue)
    policer = 'CustEth%s-%sKbps'%(intfNumber,value)
    shaperate = seqno*basevalue
    qosconfig = '''policy-map type quality-of-service %s
    class class-default
       set dscp 46
       set traffic-class 2
       police cir %s kbps bc 15 kbytes'''%(policer,value)
    intfStr = '''interface Ethernet%s.%s
    encapsulation dot1q vlan %s
    ip address 10.20.%s.1/24
    service-policy type qos input %s
    shape rate %s'''%(intfNumber,value,value,value,policer,shaperate)
    print qosconfig
    print intfStr
 
