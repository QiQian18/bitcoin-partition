import  datetime
import csv
#根据地址划分结果，对用户进行分组


tx_id=-1
connect=[]
def find_maxnum_groupid(tx):
    myList = [0] * 100
    for row in tx:
        myList[int(row[1])]+=1
    groupid=myList.index(max(myList))
    myList.clear()
    for row in tx:
        newrow=[row[0], groupid,row[2]]
        connect.append(newrow)


def read_tran():
    csvFile = open("user_add_group.csv", "r")
    reader = csv.reader(csvFile)
    tx=[]
    pre_tx_id="0"
    count =0
    for lines in reader:
        count += 1
        tx_id_num=lines[2]
        if tx_id_num!=pre_tx_id:
            pre_tx_id = tx_id_num
            find_maxnum_groupid(tx)
            tx.clear()
            tx.append(lines)
        else :
            tx.append(lines)
    find_maxnum_groupid(tx)

def write_dict():
    csvFile = open("finnal_group.csv", "w",newline='')
    writer = csv.writer(csvFile)
    for lines in connect:
        print(lines)
        writer.writerow(lines)

if __name__ == '__main__':
   start = datetime.datetime.now()
   read_tran()
   write_dict()
   print(datetime.datetime.now()-start)




