# _*_ coding:utf-8 _*_
__author__ = 'anyco'

all_report = []
x = 1
all_score = []
with open('/home/clikks/test/score.txt') as f:
    data = f.readlines()
    for i in data:
        person = i.split()
        all_report.append(person)

    for k in all_report:
        s = len(k)
        summit = 0
        all_report2 = sorted(k[1:])
        k[1:] = all_report2
        # all = int(k[1]) + all
        # print all
        while x < s:
            all = 0
            for n in all_report:
                all = int(n[x]) + all
            all_score.append(all)
            x += 1

        for j in range(1,s):
            k[j] = int(k[j])
            summit = summit + k[j]
            # all = int(j[1]) + all
        k.append(summit)
        averge = summit / s
        k.append(averge)
        print all_report
        # print all_report2
