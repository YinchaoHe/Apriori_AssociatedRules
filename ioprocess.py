import csv
from matplotlib import pyplot as plt

def csv2martix():
    n = 18
    m = 435
    dp = [[0 for i in range(n)] for j in range(m)]  # 定义矩阵dp来存储数据
    line = 0  # 矩阵的行
    column = 0  # 矩阵的列
    T = []
    M = []  # M存储不包含0的结果，是2D array
    with open('vote.csv', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            for column in range(0, 18):
                dp[line][column] = int(row[column])  # 将csv中数据放入矩阵中，若写入的为零表示此人没有这个性质
            line += 1
    for r in range(0, 435):
        for c in range(0, 18):
            if dp[r][c] != 0:
                T.append(dp[r][c])
        M.append(T)
        T = []

    return M

def write2csv(min_supports, min_confis, result_list_support, result_list_confi):
    with open("runtime.csv", "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["mininum_support", "run_time(s)"])

        for i in range(len(min_supports)):
            writer.writerow([min_supports[i], result_list_support[i][0]])

    with open("rulenumber.csv", "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["mininum_confi", "rulenumber"])
        for i in range(len(min_supports)):
            writer.writerow([min_supports[i], result_list_support[i][1]])

def generate_graph():
    runtime_csv = 'runtime.csv'
    with open(runtime_csv) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        minum_supports, runtimes = [], []
        for row in reader:
            try:
                min_support = row[0]
                runtime = row[1]

            except ValueError:
                print(min_support, 'missing data')
            else:
                minum_supports.append(float(min_support))
                runtimes.append(float(runtime))

    rulenumber_csv = 'rulenumber.csv'
    with open(rulenumber_csv) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        minum_supports, rulenumbers = [], []
        for row in reader:
            try:
                min_confi = row[0]
                confi_runtime = row[1]

            except ValueError:
                print(min_confi, 'missing data')
            else:
                minum_supports.append(float(min_confi))
                rulenumbers.append(float(confi_runtime))

    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.subplot(2,2,1)
    plt.plot(minum_supports, runtimes, c='red', alpha=1)
    plt.title(" runtime X minimnun_support", fontsize=24)
    plt.xlabel('minimun_support', fontsize=16)
    plt.ylabel("runtime", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.subplot(2,2,4)
    plt.plot(minum_supports, rulenumbers, c='red', alpha=1)
    plt.title("rulenumber X minimnun_support", fontsize=24)
    plt.xlabel('minimun_support', fontsize=16)
    plt.ylabel("rulenumber", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

def rule2txt(assio_rule_list, minu_sppoort, flag, rulenumber, minu_confi, l):
    if flag == minu_sppoort:
        f = open("asso_rule.txt", 'w')
    else:
        f = open("asso_rule.txt", 'a')
    f.write("minum_support:" + str(minu_sppoort) + " the amount of rules:" + str(rulenumber) + " the min_confi: " + str(minu_confi))
    f.write("\n")
    for i in range(len(l)):
        f.write("l[" + str(i) + "]: " + str(len(l[i])) + "     ")
    f.write("\n")
    for rule in assio_rule_list:
        f.write(str(rule[0]) + " ——> " + str(rule[1]) + ", confi:" + str(rule[2]))
        f.write("\n")
    f.write("\n")
    f.write("\n")
    f.close()

