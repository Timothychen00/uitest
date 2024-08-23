with open("a.txt",'r',encoding='utf-8') as f1:
    data2=f1.readlines()
    proccessed_data=""
    for line in data2:
        if '.' in line:
            temp=line[line.index('.')+1:]
            temp=temp.replace('[','')
            temp=temp.replace(']','')
            temp=temp.split('(')[0].rstrip()+'-('+temp.split('(')[1]
            proccessed_data+=temp
    with open('a_output.txt','w',encoding='utf-8') as f2:
        f2.write(proccessed_data)
