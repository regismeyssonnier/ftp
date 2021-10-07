from ftplib import FTP
import sys
import random
import os

def get_up(ftp, nb):
	dde = 0
	while(dde < nb):
		c = ftp.cwd('..')
		print c + ' ' + str(dde)
		dde = dde + 1

	
def path_to_file(ftp, path, folder, start, end):
	
	c = ftp.cwd(path) 
	print c
	c = ftp.mkd(folder)
	print c
	nb = str(random.randint(1, 1000000))
	f = open(nb,"w") 
	f.write((folder + ' ' + nb)*1000)
	f.close()
	c = ftp.storbinary('STOR ' + folder + '/' + nb , open(nb, 'rb'))
	print c
	os.remove(nb)

def path_to_file5(ftp, folder, start, end):
	
	c = ftp.mkd(folder)
	print c
	nb = str(random.randint(1, 1000000))
	f = open(nb,"w") 
	f.write((folder + ' ' + nb)*1000)
	f.close()
	c = ftp.storbinary('STOR ' + folder + '/' + nb , open(nb, 'rb'))
	print c
	os.remove(nb)

	#c = ftp.cwd(folder) 
	#print c
	#start = start + 1
	#path_to_file(ftp, folder, start+1, end)

def PF(ftp, path, folder, start, end):

	if(start < end):
		path_to_file(ftp, path, folder, start, end)

		PF(ftp, path + '/' + folder, 'R', start+1, end);
		PF(ftp, path + '/' + folder, 'R2', start+1, end);
		PF(ftp, path + '/' + folder, 'RA', start+1, end);
		PF(ftp, path + '/' + folder, 'RI', start+1, end);
		PF(ftp, path + '/' + folder, 'RD', start+1, end);
		PF(ftp, path + '/' + folder, 'RS', start+1, end);
				

display = 1
ip = raw_input('Server ip address :')

try:
	ftp = FTP(ip)
	l = ftp.login() 
except:
	print "Erreur : ", sys.exc_info()[1]
else:
	c = ftp.retrlines('LIST') 
	print c
	i = 0
	while(i < 100):
		try :
			folder = raw_input("Enter folder: ")
			if (folder == "&"):
				i = 100
			elif (folder == "!h"):
				print "/********-HELP-***********/"
				print "download : !"
				print "stor     : %"
				print "delete   : :"
				print "rmd      : ["
				print "mkd      : ]"
				print "folder   : folderName"
				print "/********-----************/"
			elif (folder == "!"):
				f = raw_input("download - Enter file: ")
				c = ftp.retrbinary('RETR ' + f, open("Download/" + f, 'wb').write)
				print c
			elif (folder == "!fl"):
				xx = int(raw_input("Flood - Enter NBTIMES: "))
				nx = raw_input("Flood - Enter FOLDERNAME: ")
				pt = raw_input("Flood - Enter FloOd FOLDERNAME: ")

				xXl = 0
				while(xXl < xx):
					#nxa = nx + str(xXl)
					#dd = random.randint(1, 1000)
					#PF(ftp, nxa, 0, dd)

					#ftp=0
					path=pt
					folder = nx + str(xXl)
					start=0
					end=random.randint(1, 1000)
					PF(ftp, path, folder, start, end)
					
					#dde = 0
					#while(dde < dd):
					#	c = ftp.cwd('..')
					#	dde = dde + 1

					#print c

					

					#c = ftp.mkd(nxa)
					#print c
					#nb = str(random.randint(1, 1000000))
					#f = open(nb,"w") 
					#f.write((nxa + ' ' + nb)*1000)
					#f.close()
					#c = ftp.storbinary('STOR ' + nxa + '/' + nb , open(nb, 'rb'))
					#print c
					#os.remove(nb)
					xXl = xXl + 1
					
			elif (folder == "!disp"):
				if(display):
					display = 0
					print "No Listing after ftp command"
				else:
					display = 1
					print "Listing after ftp command"
				
				
			elif (folder == "%"):
				f = raw_input("stor - Enter file: ")
				c = ftp.storbinary('STOR ' + f, open(f, 'rb'))
				print c
				if(display):
					c = ftp.retrlines('LIST') 
					print c
			elif (folder == ":"):
				f = raw_input("delete - Enter file: ")
				c = ftp.delete(f) 
				print c
				if(display):
					c = ftp.retrlines('LIST') 
					print c
			elif (folder == "["):
				f = raw_input("rmd - Enter folder: ")
				c = ftp.rmd(f) 
				print c
				if(display):
					c = ftp.retrlines('LIST') 
					print c
			elif (folder == "]"):
				f = raw_input("create - Enter folder: ")
				c = ftp.mkd(f) 
				print c
				if(display):
					c = ftp.retrlines('LIST') 
					print c
			else:
				if(folder[0:3] != "!no"):
					c = ftp.cwd(folder) 
					print c
					c = ftp.retrlines('LIST') 
					print c
				else:
					c = ftp.cwd(folder[3:len(folder)]) 
					print c
					


		except :
 			print "Erreur : ", sys.exc_info()[1]
		
		i = i + 1
		

	ftp.quit()
	


