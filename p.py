import serial
from time import sleep
import binascii

s = serial.Serial('COM12',baudrate=952, bytesize=7, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE,timeout =2 )
#s2 = serial.Serial('COM2',baudrate=115200, bytesize=7, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE,timeout =2)
#r = serial.Serial('COM12',baudrate=952, bytesize=7, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE)
#res = s.read()
#print(res)

ss="04303032313030303030303D3F"
ssc="303032313030303030303D"
s3="04303032313030303030303D3F"
s4="04 30 30 32 33 30 30 30 30 30 30 3D 3D"
s5="04007909B600C8" # 04h, 00, 79h, 09h, B6h, 00h, C8h
s5c="007909B600"
s6="0021000000"
m=['-14', '0', '0', '3', '8', '0', '9', 'b', '6', '0', '0', '0', '0', '3', '1', '3', '5', '3', '9', '5', '4', '5', '9', '4', '7', '4', '3', '3', '6', 'f', 'd']
def sendme(hexs):
    for x in range(0,len(hexs),2)  :
        #print(s5[x:x+2])
        x=hexs[x:x+2]
        y=bytes.fromhex(x)
        s.write(bytes.fromhex(x))


def checksum(hexs):
    c=0
    for x in range(0,len(hexs),2)  :        
        y=hexs[x:x+2]
        #z=bytes.fromhex(hexs[x+2:x+4]).decode('ascii')
        print(y)
        #a=z.decode()+y.decode()*0x10
        #print(y,y.decode(),z.decode(),a,hex(a))
        c=c+int(y,16)
        #c=0 - c
        #c = c ^  int(y,16)        
    #if c>0xff : c=c  ^ 0xff
    #if c>0xff : c=c  - 0x100
    print("Checksum",hex(c))    
    c = c ^ 0xffff 
    cc = "%X" % (c+1)
    r="%s%s" % (hexs, cc[2:])
    #if cc[2:]=='FF':r="%s%s" % (hexs, '00')
    print("Checksum",hex(c),hex(c),hex(c ^ 0xff))
    print("Checksum",r)
    return r

def e(i):
    return 0x30+int(s[x],16)
def d(i):
    return  i-0x30
    
def mycode(s):
    r=''
    for x in range(0,len(s)):
        #print("=",s[x],hex(0x30+int(s[x],16)))
        r=r+"%X" % (0x30+int(s[x],16))
    
    return(r)

def cc(m):
    rr=[]
    #print(m[1:-2])    
    q=''.join(m[13:13+8*2])
    print(q)
    for x in range(0,len(q),2):
        i=int(q[x:x+2],16)
        #print(q[x:x+2],i,chr(i))
        rr.append(q[x:x+2])
    print("Coded",rr)
    return(rr)
        
def f():
    t=[]
    tt=[]
    while True:
        try:
            serialString = s.read()
            if len(serialString)>0:
                dd="%x" % d(serialString[0])
                #print("2",hex(serialString[0]),chr(serialString[0]),len(t),dd)
                t.append(dd)
            else:
                #print(t)
                return t
                break
        except KeyboardInterrupt:
            break                
    return t
def ff():
    t=[]
    tt=[]
    for i in range(0,31):
        try:
            serialString = s.read()
            #if len(serialString)>0:
            dd="%x" % d(serialString[0])
            #print("2",hex(serialString[0]),chr(serialString[0]),len(t),dd)
            t.append(dd)
            # # else:
            #print(t)
        except KeyboardInterrupt:
            break                
    return t    
fp=open("output.bin","wb")

def fsave(l,pos): 
    print("debug save",len(l),fp.tell())
    #fp.seek(pos)
    for x in l:
        print("Write",x)
        fp.write(binascii.unhexlify(x))

def job(start,i):    
    size=8
        
    #rmd="007909%s" % "B600"
    rmd="007909%X" % start
    
    print("Debug %x" % start)
    r=checksum(rmd)
    print("R1",r)

    rr=mycode(r)
    rr='04'+rr
    print(rr)
    while True:
        sendme(rr)
        flist=ff()
        print(flist,len(flist))
        if flist[0]=='-14':
            break
            sleep(1)
            print("Retry")


    bb=cc(flist)
    #print(bb[6:-1])

    fsave(bb,i)

#b=0xb600
#rmd="007909%X" % b
#print(rmd)


start=0xB600

n=0
#job(start,n)
#job(start+8,n+8)
#job(start+0x200,n)


for i in range (0,0x16,8):
    print("===",i)
    job(start+i,n+i)


#r=checksum(s5c)
#print(r)
#r=checksum(ssc)
#print(r)
#print("R1",r)
    