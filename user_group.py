import  datetime
import csv

#把tx中用户聚集到一个虚拟人
dict = {}
start = datetime.datetime.now()
print(start)
tx_id=-1
#读取CSV中的文件，转换成字典
def list2dict(tx):
    global  tx_id
    flag = False
    for temp in tx:
        try:
            ex_id = dict[temp]
            flag =True  #出现旧的ID需要合并
        except KeyError:
            continue  #对应的ID全是新的ID
    if flag:
        for id in tx:
            dict[id]=ex_id
    else :
        tx_id += 1
        for id in tx:
            dict[id]=tx_id
def read_tran():
    csvFile = open("transaction.csv", "r")
    reader = csv.reader(csvFile)
    tx=[]
    pre_tx_id="0"
    for lines in reader:
        tx_id_num=lines[0]
        if tx_id_num!=pre_tx_id:
            #list的tx转成dict,传入对应的ID
            pre_tx_id = tx_id_num
            list2dict(list(set(tx)))
            tx.clear()
            tx.append(lines[1])
        else :
            tx.append(lines[1])
    list2dict(list(set(tx)))



def write_dict():
    csvFile = open("user_group.csv", "w",newline='')
    writer = csv.writer(csvFile)
    for key,value in dict.items():
        writer.writerow([key,value])
if __name__ == '__main__':
   read_tran()
   print(datetime.datetime.now())
   write_dict()



