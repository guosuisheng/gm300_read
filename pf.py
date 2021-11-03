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
def ff2(n):
    t=[]
    tt=[]
    for i in range(0,n):
        try:
            serialString = s.read()
            #if len(serialString)>0:
            dd="%x" % d(serialString[0])
            #print("2",dd)
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
    print("Finale",rr)
    while True:
        sendme(rr)
        flist=ff()
        print(flist,len(flist))
        if flist[0]=='-14':
            break
            sleep(1)
            print("Retry")
    bb=cc(flist)
    print("Finale",' '.join(bb))
    with open ("b.txt","a") as fp:
        fp.write(' '.join(bb)+"\n")

def gwrite(start,b):
    b=b.replace(' ','')
    # 04h, 00h, 59h, 09h, B6h, 00h, 00h, FFh, FFh, FFh, FFh, FFh, FFh, FFh, FFh, F0h
    rmd="005909%X00" %start # first ,follow with 8 byte you want to write
    #rmd=rmd+'FFFFFFFFFFFFFFFF'
    #rmd=rmd+'2F01F101F1570057'
    rmd=rmd+b
    print("Debug %x %s" % (start,rmd))
    r=checksum(rmd)
    print("R1",r)
    rr=mycode(r)
    rr='04'+rr
    print("Finale",rr)    
    sendme(rr)
    flist=ff2(13)
    bb=cc(flist)
    print(flist)

def gwrite2(start,b):
    b=b.replace(' ','')
    # 04h, 00h, 59h, 09h, B6h, 00h, 00h, FFh, FFh, FFh, FFh, FFh, FFh, FFh, FFh, F0h
    l=len(b)
    ll=int(l/2)+1
    print("D",l,ll)
    #rmd="005916%X00" %start # first ,follow with 8 byte you want to write
    rmd="0059%.2X%X00" % (ll,start) # first ,follow with 8 byte you want to write

    #rmd=rmd+'FFFFFFFFFFFFFFFF'
    #rmd=rmd+'2F01F101F1570057'
    rmd=rmd+b
    print(rmd)
    
    print("Debug %x %s" % (start,rmd))
    r=checksum(rmd)
    print("R1",r)
    
    rr=mycode(r)
    rr='04'+rr
    print("Finale",rr)    
    sendme(rr)
    flist=ff2(13)
    bb=cc(flist)
    print(flist)

#b=0xb600
#rmd="007909%X" % b
#print(rmd) 0.8
#402.6 + 0x99 * 5
#  450.9 - x ) = 40.5   x=410.4   y=81            450.9
# (443.5  - 402.95 )/ 0.5         y=66            438.9
#      0x3f1 *5 +402950                              75
#
#>>> 0x1f1 * 0x127 + 403000000 + 0 =403146615
# (423000000 - 403000000) / 0x127
# (423000000  - 403000000-0x0 ) / (0x127 * 6250) = 10.84 (spand index)
#  (403020000- 403000000-0x0 ) / (  6250) =  hex in eeprom
#  (423000000 - 403000000-0x0 ) / (6250)
#  (50100000-42000000)/ (0107*  5000)

# 403 0x0000 0x0127 hex(0x00 ^ 0x00 ^ 0x01 ^ 0x27 ^ 0xff) = 0xd9  
# position 0x2e0 00 00 0127 eeprom position 0xb600+0x2e0 = 0xb8e0
# 
# 430 0x177b 0x0141 hex(0x17 ^ 0x7b ^ 0x01 ^ 0x41 ^ 0xf5) = 0xd8
# gwrite2(0xb8e0,"17 7b 01 41")
# gwrite2(0xff00,"f5")
start=0xb8e0

n=0
#job(start,n)
#job(start+8,n+8)
job(start,n)
job(0xff00,n)
#job(start+8,n)
#job(start+16,n)
#f="2F 01 f1 01 00 57 00 57 00 00 00 00 30 00 00 00 00 00 00 00".replace(" ","")
#print(f)
#fa=len(f)/2
#print(hex(len(f)),fa)
#gwrite2(start,f)

#  0059097800002F01F1010057005756
# 040059097800002F01F1010057005756

#gwrite(start,   '2f 01 3C 02 00  57 00 57 ')
#gwrite(start+8, '57 00 00 00 00 00 30 00')
#gwrite(start+16,'00 00 00 00 00 0f 2f 01')

#f=checksum("2F 01 00 01 00 57 00 57 00 00 00 00 30 00 00 00 00 00 00 00".replace(" ",""))
#f=checksum("2f 02 f1 02 f1 57 00 57 00 00 00 00 00 30 00 00 00 00 00 00 ".replace(" ",""))

#print(f)
#gwrite2(start,f)
#for i in range (0,0x30,8):
#    print("===",i)
#    job(start+i,n+i)


#r=checksum(s5c)
#print(r)
#r=checksum(ssc)
#print(r)
#print("R1",r)
    