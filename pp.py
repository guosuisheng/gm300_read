
#print(chr(i))
#sendme(ss)
#checksum(s5c)
#r=checksum(s6)


r=checksum(s5c)
print("R1",r)
rr=mycode(r)
rr='04'+rr
print(rr)
sendme(rr)


for i in range(0,1):
    for x in range(0,len(s5),2)  :
        #print(s5[x:x+2])
        x=s5[x:x+2]
        s.write(bytes.fromhex(x))

    #serialString = s.read()
    #print(serialString,len(serialString))

#s.write(bytes.fromhex(ss))
#s.write(bytes.fromhex("04"))
#serialString = s.read()
#print(serialString,len(serialString))

#serialString = s.read()
#print(serialString)

t=[]
tt=[]
while True:
    
    try:
        serialString = s.read()
        #r.write(serialString)
        #res=r.read()
        #if int(serialString[0])>0:
        if len(serialString)>0:
            #s.write(serialString)
            #r.write(serialString)
            #res=r.read()
            #t.append(serialString)
            #tt.append(res)
            dd="%x" % d(serialString[0])
            print("2",hex(serialString[0]),chr(serialString[0]),len(t),dd)
            #print(t)
            #print(tt)
            t.append(dd)
        else:
            #print("1",serialString,len(serialString))
            #print("2",res,len(res))
            #for x in t:
            #    r.write(x)
            #t=[]
            #for y in range(0,100):
            #    res=r.read()
            #    if int(res)>0:
            #        tt.append(res)
            #    else:
            #        break
            print(t)
            break

        s.write(serialString)
        while True:
            res=r.read()
            s.write(res)
            if len(res)==0:
        #        print("Write")
                break
        '''
        #if len(serialString)>0:
        #    print("1",hex(serialString[0]),len(serialString))
            #r.write(serialString)
        # serialPort.reset_input_buffer()
        # serialPort.reset_output_buffer()
        # serialString = serialPort.read(10).hex()
        '''
        t=[]
        if s.in_waiting > 0:
            for i in range(0,30):
                serialString = s.read()
                print("1",serialString,len(serialString))
                #if len(serialString)>0:
                #   t.append(serialString)
            
            #r.write(serialString)
            #t.append(serialString)
            #serialString = s.read()
 
            #sleep(1)
        sr2 = r.read()
        while len(sr2)>0:
            sr2=r.read()
            print("2",len(sr2))
            s.write(sr2)
            #sleep(1)
    
        #if len(serialString)==0:
        #    s.write(bytes.fromhex("04303032313030303030303D3F"))
    except KeyboardInterrupt:
        break
'''
