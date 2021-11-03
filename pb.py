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
    if i is not  None:
        return  i-0x30
    return None
    
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
    for i in range(0,31):
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
                    out=parse(c0)
                    
                    if out is None:
                        continue
                    print("222222222")
                    if 'COUNT0' in out:
                        if out['COUNT0']>0:
                            for i in range(0,out['COUNT0']*2):
                                serialString = s.read() 
                                s.write(serialString)
                                t.append(serialString)
                        c0=btoh(t)
                        out=parse(c0)  
                        print("3",out)                    
                    if 'COK' in out:
                        if out['COK']:
                            print("3","Redirect")
                            re(t)
                    
                    return t
            else:
                print("35 resent",out)
                #for x in t:
                #    r.write(x)
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
    return [d(int(a,16)),d(int(b,16))]
    
def a0(x):
    if len(x)>0:
        return(int(x.hex(),16))    
    else:
        return None
def ff():
    t=[]
    tt=[]
    for i in range(0,31):
        try:
            serialString = s.read() 
            s.write(serialString)             
            a=a0(serialString)
            
            if a is not None:
                print(a,hex(a),d(a))
                if a==4:
                    t=[]
                    t.append(serialString)
                    for i in range(0,12):
                        serialString = s.read() 
                        s.write(serialString)  
                        t.append(serialString)
                    #print("1",t)
                    c0=btoh(t)
                    out=parse(c0)
                    print("2",out)
                    if out is None:
                        continue
                    print("222222222")
                    if 'COUNT0' in out:
                        if out['COUNT0']>0:
                            for i in range(0,out['COUNT0']*2):
                                serialString = s.read() 
                                s.write(serialString)
                                t.append(serialString)
                        c0=btoh(t)
                        out=parse(c0)  
                        print("3",out)  
                        if out is None:
                            continue
                    if 'COK' in out:
                        if out['COK']:
                            print("3","Redirect")
                            rr=re(t)
                            for x in rr:
                                s.write(x)
                #s.write(serialString) 
            

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
        r.append(d(x))
    return r    
def parse(cmd):
    for x in cmd:
        print("Dee",len(x))
        if len(x)==0:
            return None
    result={}
    print("CMD K",cmd[0])    
    print("CMD null",cmd[1],cmd[2])    
    print("CMD Function",cmd[3],cmd[4])    
    print("CMD Byte Count ",cmd[5],cmd[6])    
    print("CMD High",cmd[7],cmd[8])        
    print("CMD Low",cmd[9],cmd[10])  
    print("CMD CKM",cmd[11],cmd[12])
    result['K']=cmd[0]
    result['CKM']=[int(cmd[11],16)-0x30,int(cmd[12],16)-0x30]
    result['CKMS']="%X%X" % (int(cmd[11],16)-0x30,int(cmd[12],16)-0x30)
    result['NULL']=c2d(cmd[1],cmd[2])
    #result['NULL0']=int("%d%d" % (result['NULL'][0],result['NULL'][1]),16)
    result['FUNCTION']=c2d(cmd[3],cmd[4])
    result['COUNT']=c2d(cmd[5],cmd[6])
    result['COUNT0']=int("%d%d" % (result['COUNT'][0],result['COUNT'][1]),16)
    result['HIGH']=c2d(cmd[7],cmd[8])
    result['LOW']=c2d(cmd[9],cmd[10])
    result['BIN']=''.join(btog(cmd[1:-2]))
    result['BINO']=''.join(btog(cmd[1:]))
    result['CKMO']=result['BIN']+result['CKMS']    
    result['COK']=False
    if result['NULL'][0]==0 and result['NULL'][1]==0:
        result['CC']=checksum(result['BIN'])
        if result['CC']==result['CKMO'] : 
            result['COK']=True 
        
    print(result)
    return result
    
#c1=['1c', '30', '30', '32', '34', '30', '30', '30', '30', '30', '30', '3d', '3c']
#parse(c1)
ff()
ff()
ff()
ff()

#r=checksum(s5c)
#print(r)
#r=checksum(ssc)
#print(r)
#print("R1",r)
    