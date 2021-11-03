import serial
from time import sleep
import binascii

s = serial.Serial('COM3',baudrate=952, bytesize=7, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE,timeout =2)
#s2 = serial.Serial('COM2',baudrate=115200, bytesize=7, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE,timeout =2)
r = serial.Serial('COM12',baudrate=952, bytesize=7, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE,timeout =2)
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
        #print(y)
        #a=z.decode()+y.decode()*0x10
        #print(y,y.decode(),z.decode(),a,hex(a))
        c=c+int(y,16)
        #c=0 - c
        #c = c ^  int(y,16)        
    #if c>0xff : c=c  ^ 0xff
    #if c>0xff : c=c  - 0x100
    #print("Checksum",hex(c))    
    c = c ^ 0xffff 
    cc = "%X" % (c+1)
    r="%s%s" % (hexs, cc[2:])
    #if cc[2:]=='FF':r="%s%s" % (hexs, '00')
    #print("Checksum",hex(c),hex(c),hex(c ^ 0xff))
    #print("Checksum",r)
    return r

def e(i):
    return 0x30+int(s[x],16)
def d(i):    
    return "%X" % (i-0x30)
    
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
                print("2",hex(serialString[0]),chr(serialString[0]),len(t),dd)
                t.append(dd)
            else:
                #print(t)
                return t
                break
        except KeyboardInterrupt:
            break                
    return t
def re(t):
    for x in t:
        r.write(x)
    for i in range(0,3221):
        try:
            serialString = r.read()
            print("33",serialString) 
            if len(serialString)>0:
                if int(serialString[0])==0x1c:
                    t=[]
                    t.append(serialString)                
                    for i in range(0,12):
                        serialString = r.read()
                        r.write(serialString)
                        print("32",serialString)
                        t.append(serialString)
                        #s.write(serialString)
                    print(t)
                    c0=btoh(t)
                    print(c0)
                    rd=parse(c0)
                    for y in range(0,int(rd['COUNT'])*4):
                        serialString = r.read()
                        #if len(serialString)==0 or a0(serialString)==4 : return
                        r.write(serialString)
                        print("2 aa",serialString,a0(serialString))
                        t.append(serialString)                    
                    return t
            else:
                print("35 resent",t)
                for x in t:
                    r.write(x)
        except KeyboardInterrupt:
            break  
    return  
def btoh(l):
    r=[]
    for x in l:    
        r.append(x.hex())
    return r
def c2c(a,b):
    return chr(int(a,16))+chr(int(b,16))
def c2d(a,b):
    return "%s%s" % (d(int(a,16)),d(int(b,16)))

def a0(x):
    if len(x)>0:
        return(int(x.hex(),16))    
def ff():
    t=[]
    tt=[]
    for i in range(0,31):
        try:
            serialString = s.read()
            s.write(serialString)            
            
            #if len(serialString)>0:
                #dd="%x" % d(serialString[0])
                #print("1",hex(serialString[0]),len(t),dd)
                #t.append(d)
            if a0(serialString)==4:
                #s.write(serialString)
                t=[]
                t.append(serialString)
                for i in range(0,12):
                    serialString = s.read()
                    if len(serialString)==0 or a0(serialString)==4 : return
                    s.write(serialString)
                    print("2 aa",serialString,a0(serialString))
                    t.append(serialString)
                    #s.write(serialString)
                #print(t,hex(t[3][0]),t[4])
                #if t[4]==b'>':
                #    for i in range(0,4):
                #        serialString = s.read()
                #        s.write(serialString)
                #        print("2 ss",serialString)
                #        t.append(serialString)
                c0=btoh(t)
                print(c0)
                rd=parse(c0)
                for y in range(0,int(rd['COUNT'])*4):
                    serialString = s.read()
                    #if len(serialString)==0 or a0(serialString)==4 : return
                    s.write(serialString)
                    print("2 aa",serialString,a0(serialString))
                    t.append(serialString)
                c0=btoh(t)
                print(c0)
                rd=parse(c0)

                    
                rr=re(t)
                 
                 
                for x in rr:
                    s.write(x)
                print("Done")
                    #return
                    
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


#start=0xb600
start=0x6000 
n=0
#job(start,n)
#job(start+8,n+8)
#job(start+456,i+456)

'''
for i in range (0,0xfff,8):
    print("===",i)
    job(start+i,n+i)

ff()
ff()
ff()
ff()
ff()
ff()
ff()
ff()
'''
def mycik(binlist):
    c=0
    for x in binlist  :        
        print(x)
        c=c+x
    print("Checksum",hex(c))    
    c = c ^ 0xffff 
    cc = "%X" % (c+1)
    #r="%s%s" % (hexs, cc[2:])
    print("Checksum",hex(c),hex(c),hex(c ^ 0xff))
    return
def btog(l):
    r=[]
    for x in l:    
        r.append(chr(int(x,16)))
    return r
def bot2(l):
    r=[]
    for x in l:           
        r.append(d(int(x,16)))
    return r 
    
def parse(cmd):
    result={}
    print("CMD K",cmd[0])    
    print("CMD null",cmd[1],cmd[2])    
    print("CMD Function",cmd[3],cmd[4],c2c(cmd[3],cmd[4]))    
    print("CMD Byte Count ",cmd[5],cmd[6],c2c(cmd[5],cmd[6]))    
    print("CMD High",cmd[7],cmd[8])        
    print("CMD Low",cmd[9],cmd[10])  
    print("CMD CKM",cmd[11],cmd[12]) 
    #result['CKM']=[int(cmd[11],16)-0x30,int(cmd[12],16)-0x30]
    result['CKM']=c2d(cmd[11],cmd[12])
    result['CKMS']="%X%X" % (int(cmd[11],16)-0x30,int(cmd[12],16)-0x30)
    result['NULL']=c2d(cmd[1],cmd[2])
    #result['NULL0']=int("%d%d" % (result['NULL'][0],result['NULL'][1]),16)
    result['FUNCTION']=c2d(cmd[3],cmd[4])
    result['COUNT']=c2d(cmd[5],cmd[6])
    #result['COUNT0']=int("%d%d" % (result['COUNT'][0],result['COUNT'][1]),16)
    result['HIGH']=c2d(cmd[7],cmd[8])
    result['LOW']=c2d(cmd[9],cmd[10])
    print(cmd[1:-2])
    result['BIN']=''.join(bot2(cmd[1:-2]))
    result['BINO']=''.join(bot2(cmd[1:]))
    result['CKM0']=result['BIN']+result['CKM']    
    result['COK']=False
    if result['NULL']=='00':
        result['CC']=checksum(result['BIN'])
        if result['CC']==result['CKM0'] : 
            result['COK']=True 
        
    print(result)
    return result
    
#c1=['1c', '30', '30', '32', '34', '30', '30', '30', '30', '30', '30', '3d', '3c']
#c2=['04', '30', '30', '32', '31', '30', '30', '30', '30', '30', '30', '3d', '3f']
c3=['04', '30', '30', '32', '3e', '30', '32', '30', '30', '30', '30', '30', '30']
parse(c3)
ff()
ff()
ff()
ff()

#r=checksum(s5c)
#print(r)
#r=checksum(ssc)
#print(r)
#print("R1",r)
    