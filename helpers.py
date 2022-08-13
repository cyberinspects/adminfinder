def threadlister(path,thno):
	listfromfile=[]
	with open(path,'r') as file:
		lines=file.readlines()
		for line in lines:
			line=line.replace('\n','')
			listfromfile.append(line)

	listlen=len(listfromfile)
	thrd=thno
	items_for_one_thread=int(listlen/thrd)+1
	mainlist=[]
	index=0
	for sublist in range(thrd):
		a=[]
		for item in range(int(items_for_one_thread)):
			if index<listlen:
				a.append(listfromfile[index])
				index=index+1
			else:
				break
		if a!= []:
			mainlist.append(a)
		else:
			break
	return mainlist




