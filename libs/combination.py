# encode: utf-8

import sys
import math

def is_prime(r):
	for i in prime_list:
		if r%i == 0:
			return False
		else:
			continue
	return True

n = int(sys.argv[1])
prime_list = [2]
for i in range(3, n+1):
	if is_prime(i):
		prime_list.append(i)

def prime(l):
	res = []
	for i in range(len(prime_list)):
		res.append(0)
	while 1:
		for i in range(len(l)):
			if l[i] == 1:
				continue
			for j in range(len(prime_list)):
				if l[i]%prime_list[j] == 0:
					l[i] = l[i]/prime_list[j]
					res[j]+= 1
					break
				else:
					continue
		flag = 0
		for i in range(len(l)):
			if l[i] == 1:
				flag+=1
		if flag == len(l):
			break;
	return res
			

def combination(n, r):
	if r > n:
		print 'ERROR! you cannot calculate combination C(n, r) with r > n !'
		return
	if r > (n/2):
		return combination(n, n-r)
	elif r == 0:
		return 1
	else:
		return cal_comb(n, r)
		
def production(pl, pr):
	res = 1
	#print prime_list
	for i in range(len(pl)):
		res *= math.pow(pl[i], pr[i])
	return int(res)
		
def cal_comb(n, r):
	molecular = []
	denominator = []
	for i in range(0, r):
		molecular.append(n-i)
		denominator.append(r-i)
	prime_molecular = prime(molecular)
	prime_denominator = prime(denominator)
	prime_res = []
	#print prime_molecular
	#print prime_denominator
	for i in range(len(prime_molecular)):
		prime_res.append(prime_molecular[i]-prime_denominator[i])
	#print prime_res
	log = ''
	for i in range(len(prime_res)):
		if prime_res[i] != 0:
			if i != 0:
				log += '*'
			if prime_res[i] == 1:
				log += str(prime_list[i])
			else:
				log += '('+str(prime_list[i])+'^'+str(prime_res[i])+')'
	print log
	return production(prime_list, prime_res);
	
	
print combination(int(sys.argv[1]), int(sys.argv[2]))
