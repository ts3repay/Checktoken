#! python3

import requests , os , sys , time 


if sys.platform in ["linux","linux2"]:
	W = '\033[0m'
	G = '\033[32;1m'
	R = '\033[31;1m'
	
else:
	W = ''
	G = ''
	R = ''


print(R + '''Check Token Facebook L7z ''')
print('พิมพ์ token.txt')
print(G + 'คำสั่ง : ', end='' + W)
put = input()

file = open(put , 'r')
readfile = file.read()
lista = readfile.split('\n')

# lista = ['kjlahsflhas' , 'ajskhkgas']

file.close()
print()
print(G + 'เริ่มเช็ค !')
print()
live = []
die = []

print(W + 'โทเค่นทั้งหมด: ' , G + str(len(lista)))
print()
print('+'.center(40 , '+'))
print()
# def chk(access):
	

x = 1
x2 =  .5
for access in lista:
	if x == 6:
		time.sleep(x2)
		x = 1
		x2 += .1
	if not access.isalnum():
		continue
	
	try:
		res = requests.get('https://graph.facebook.com/me?access_token=' + access)
	except Exception as exc:
		print(R + 'Error ... Skipping and' + G + ' Continue ...')
	


	if 'Error validating access token' in res.text:
		print( G + '' + W + access  , end='')
		print(R + ' DIE ')
		die.append(access)
	elif 'The access token could not be decrypted' in res.text:
		print( G + '' + W + access  , end='')
		print(R + ' ตาย')
		die.append(access)
	elif 'Malformed access token' in res.text:
		print( G + '' + W + access  , end='')
		print(R + 'ตาย')
		die.append(access)

	else:
		print( G + '' + W + access  , end='')
		print(G + ' รอด')
		live.append(access)
	x +=1


print('รอด = ', len(live))
print('ตาย = ', len(die) )

os.makedirs('output' , exist_ok=True)

livefile = open(os.path.join('.','output','live.txt') , 'a')

for i in live:
	livefile.write(i + '\n')
livefile.close()

diefile = open(os.path.join('.','output','die.txt'), 'a')
for i in die:
	diefile.write(i + '\n')
diefile.close()
print('Token ที่ตาย และรอดจะอยู่ใน '+ G + ' [Output] ' +W )
