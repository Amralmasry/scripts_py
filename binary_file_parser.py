import zlib

f=open("bootcode.bin","rb")
data = f. read(1)
counter = 0
databytes = bytearray()
while data :
	databytes+=data   
	counter+=1
	data = f. read(1)
f.close()

print(counter)
crc = zlib.crc32(databytes)
print(crc) 


f=open("bootcode.bin","wb")
sizebytes= counter.to_bytes(4,'big')
f.write(sizebytes)
f.close()

f=open("bootcode.bin","ab")
crcbytes= crc.to_bytes(4,'big')
f.write(crcbytes)
f.close()

f=open("bootcode.bin","ab")
f.write(databytes)
f.close()

f=open("bootcode.bin","ab")
f.write(bytes("invalid !", 'utf-8'))
f.close()

