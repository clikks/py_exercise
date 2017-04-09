# _*_ coding:utf-8 _*_
__author__ = 'anyco'

all_report = [] #所有学生分数列表
all_score = []  #总成绩列表

with open('./score.txt') as f:
    data = f.readlines()

for i in data:
    all_report.append(i.split())
#处理每个人的成绩并以一个列表保存到all_report列表

for k in all_report:
    s = len(k)

    for j in range(1,s):
        k[j] = float(k[j])
    summit = sum(k[1:])
    averge = summit / s
    k.append(summit)
    k.append(averge)

all_report = sorted(all_report,key=lambda d:d[-2],reverse=True)
#计算每个学生的总成绩和平均分,并且根据分数高低排序

s = len(all_report[0])
x = 1
rank = 1

while x < s:
    all = 0
    for n in all_report:
        all += n[x]
        if rank <= len(all_report):
            n.insert(0, str(rank))
            rank += 1
    avg = all / len(all_report)
    all_score.append('%.1f' %avg)
    x += 1
#计算所有学生的每科平均分，总平均分,并添加名次

title = ['名次','姓名','语文','数学','英语','物理','化学','生物','政治','历史','地理','总分','平均分']
all_score.insert(0,'0\t平均')

with open('finnal_score.txt','w') as f:
    for i in title:
        f.write(i + '\t')
    f.write('\r')
    for i in all_score:
        f.write(i + '\t')
    f.write('\r')
    for i in all_report:
        f.write(i[0] + '\t' + str(i[1]) + '\t')
        for k in i[2:-2]:
            if k < 60:
                k = '不及格'
            f.write(str(k) + '\t')
        f.write(str(i[-2]) + '\t' + str(i[-1]) + '\r')
#处理学生不及格的成绩，并且将成绩格式化输出到文件中。