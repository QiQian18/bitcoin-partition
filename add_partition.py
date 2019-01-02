import csv
import  datetime
import  random

#对地址分组
dict = {}
myList = [([0] * 100) for i in range(2666809)] #会占内存
count = 0
def read_hub_id():
    csvFile = open("user_hub.csv", "r")
    reader = csv.reader(csvFile)
    num = 0
    for lines in reader:
        dict[lines[0]]=num
        num +=1

def put_in_array(address,address2):
    global  myList
    global  count
    try:
        count+=1
        num = dict[address]
        row = int(address2)
        myList[row][num]=myList[row][num]+1
    except KeyError:
        pass

def input_tx():
    csvFile = open("transaction.csv", "r")
    reader = csv.reader(csvFile)
    for lines in reader:
        add_in = lines[1]
        add_out = lines[2]
        put_in_array(add_in,add_out)
        put_in_array(add_out,add_in)


def random_rate():
    weight=[]
    id=[]
    for i in range(0,100):
        id.append(i)
        rate = int(i/10)+1
        weight.append(rate)
    table = [z for x, y in zip(id, weight) for z in [x] * y]
    return table


def output_addre_part():
    print("strat write")
    max_num = 0
    group_id = -1
    csvFile = open("addre_group2.csv", "w", newline='')
    writer = csv.writer(csvFile)
    count =0
    table = random_rate()
    for i in range(len(myList)):
        for j in range(len(myList[0])):
            if myList[i][j]>max_num:
                max_num=myList[i][j]
                group_id=j
                count+=1
        if group_id == -1:
            group_id = random.choice(table)
        writer.writerow([i,group_id])
        max_num=0
        group_id = -1
    print(count)

if __name__ == '__main__':
    starttime = datetime.datetime.now()
    read_hub_id()       #读入hub的ID，一共有100个分组
    input_tx()          #根据transaction.csv表中的交易记录，计算和Hub的依赖度，把地址划到最大的那个分区
    output_addre_part() #输出地址划分的结果
    endtime = datetime.datetime.now()
    print(endtime-starttime)

