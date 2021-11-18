def read_file(filename):
    data_list=[]
    file=open(filename,"r")
    for line in file:
        data_list.append(line.split(","))
    file.close()
    return data_list
def fixlast(l):
    for x in l:
        # print(x[3])
        x[-1] = x[-1].strip()
    return l
def addprofit(l):
    for x in l:
        x.append(float(x[3])-float(x[2]))
    return l
def findlowhigh(l):
    highestval=0
    lowestval=10000000000000000
    lowname=''
    highname=''
    for x in l:
        if float(x[4])>highestval:
            highestval=float(x[4])
            highname = x[1]
        if float(x[4])<lowestval:
            lowestval=float(x[4])
            lowname=x[1]
    return [lowname,lowestval,highname,highestval]
def filemaker(l):
    t=open("moviefile.txt",'w')
    for x in l:
        t.write(str(x)+"\n")

def main():
    list=read_file('movies.csv')
    list=fixlast(list)
    list=addprofit(list)
    x=findlowhigh(list)
    filemaker(list)
    print("the movie with the most profit was " + str(x[2])+" with a profit of "+str(x[3]))
    print("the movie with the most profit was " + str(x[0])+" with a profit of "+str(x[1]))

main()
