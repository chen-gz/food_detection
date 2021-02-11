from sklearn import svm
import csv
from sklearn.utils import shuffle

from sklearn.metrics import classification_report
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
import numpy as np
import matplotlib.pyplot as plt

food_file_path, non_food_file_path = 'food.csv', 'no_food.csv'
# food_file_path2, non_food_file_path2 = 'food2.csv', 'no_food2.csv'
food_raw_data, non_food_raw_data = [], []
# food_raw_data2, non_food_raw_data2 = [], []

train_raw_food, train_raw_non_food = [], []
test_raw_food, test_raw_non_food = [], []

train_vector_x, train_vector_y, train_vector_num = [], [], []
test_vector_x, test_vector_y = [], []

useful_tag_list, useful_dict = [], {}

correlation_dict = {}

p_food = 0


def get_raw_data():
    global food_raw_data, non_food_raw_data

    with open(food_file_path) as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            food_raw_data.append(row)
    with open(non_food_file_path) as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            non_food_raw_data.append(row)

    # with open(food_file_path2) as f:
    #     csv_reader = csv.reader(f)
    #     for row in csv_reader:
    #         food_raw_data2.append(row)
    # with open(non_food_file_path2) as f:
    #     csv_reader = csv.reader(f)
    #     for row in csv_reader:
    #         non_food_raw_data2.append(row)


def shuffle_raw_data():
    global food_raw_data, non_food_raw_data
    # non_food_raw_data = non_food_raw_data[:15000]
    # non_food_raw_data = non_food_raw_data[:len(food_raw_data)]
    food_raw_data = shuffle(food_raw_data)
    non_food_raw_data = shuffle(non_food_raw_data)
    # non_food_raw_data = non_food_raw_data[:15000]
    non_food_raw_data = non_food_raw_data[:len(food_raw_data)]
    # non_food_raw_data = non_food_raw_data[00000]

    

def div_train_test_raw_data(ratio=0.75):
    global food_raw_data, non_food_raw_data, train_raw_food, \
        train_raw_non_food, test_raw_food, test_raw_non_food, \
        food_raw_data2, non_food_raw_data2
    # remove some non_food_raw_data
    # non_food_raw_data = non_food_raw_data[:10000]
    train_food_len = int(len(food_raw_data) * ratio)
    train_non_food_len = int(len(non_food_raw_data) * ratio)
    train_raw_food = food_raw_data[0:train_food_len]
    train_raw_non_food = non_food_raw_data[0:train_non_food_len]
    test_raw_food = food_raw_data[train_food_len:]
    test_raw_non_food = non_food_raw_data[train_non_food_len:]

    # train_raw_food = food_raw_data
    # test_raw_food = food_raw_data2

    # train_raw_non_food = non_food_raw_data
    # test_raw_non_food = non_food_raw_data2

def save_raw_data_train_test():
    global food_raw_data, non_food_raw_data, train_raw_food, \
        train_raw_non_food, test_raw_food, test_raw_non_food
    with open('train_food.csv', 'w') as f:
        write = csv.writer(f)
        write.writerows(train_raw_food)
    with open('train_non_food.csv', 'w') as f:
        write = csv.writer(f)
        write.writerows(train_raw_non_food )

    with open('test_food.csv', 'w') as f:
        write = csv.writer(f)
        write.writerows(test_raw_food )
    with open('test_non_food.csv', 'w') as f:
        write = csv.writer(f)
        write.writerows(test_raw_non_food)

    for i in train_raw_food:
        i = i[1:]
    for i in train_raw_non_food:
        i = i[1:]
    for i in test_raw_food:
        i = i[1:]
    for i in test_raw_non_food:
        i = i[1:]
    print(len(train_raw_food))


    


def count_dict(raw_data, threshold=0.5):
    counter_dict = {}  # only collect from train data
    for i in raw_data:
        for j in range(0, len(i) - 1, 2):
            tmp = str(i[j]).strip()
            if float(i[j + 1]) > threshold:
                if tmp not in counter_dict:
                    counter_dict[tmp] = 1
                else:
                    counter_dict[tmp] += 1
            else:
                # if tmp not in counter_dict:
                #     counter_dict[tmp] = 0
                pass
    return counter_dict


def get_use_tag(use_all=False, threshold=0.5):
    global useful_tag_list, food_raw_data, non_food_raw_data, useful_dict
    useful_tag_list, useful_dict = [], {}
    food_tag_dict = count_dict(train_raw_food)
    non_food_tag_dict = count_dict(train_raw_non_food)

    if use_all:
        for i in non_food_tag_dict.keys():
            if i not in food_tag_dict.keys():
                food_tag_dict[i] = non_food_tag_dict[i]
            else:
                food_tag_dict[i] += non_food_tag_dict[i]
        # food_tag_dict.update(non_food_tag_dict)

    appear_times = 0
    appear_list = []
    for i in food_tag_dict.keys():
        appear_times += food_tag_dict[i]
        appear_list.append(food_tag_dict[i])
    appear_list.sort(reverse=True)
    useful_bound = int(appear_times * threshold)
    bound = 0
    pre_sum = 0
    for i in range(len(appear_list)):
        pre_sum += appear_list[i]
        if pre_sum > useful_bound:
            bound = appear_list[i]
            break
    for i in food_tag_dict.keys():
        if food_tag_dict[i] > bound:
            useful_tag_list.append(i)
    counter = 0
    for i in useful_tag_list:
        useful_dict[i] = counter
        counter += 1


def get_correlation():
    global train_raw_food, correlation_dict
    food_tag_dict = count_dict(train_raw_food)
    merged_dict = count_dict(train_raw_non_food)

    for i in food_tag_dict.keys():
        if i not in merged_dict.keys():
            merged_dict[i] = food_tag_dict[i]
        else:
            merged_dict[i] += food_tag_dict[i]

    for i in food_tag_dict.keys():
        if i not in correlation_dict.keys():
            correlation_dict[i] = food_tag_dict[i] / len(food_raw_data)
            # correlation_dict[i] = food_tag_dict[i] / merged_dict[i]
        else:
            print("error in get correlation function")


def construct_train_test_set():
    global train_raw_food, train_raw_non_food, test_raw_food, \
        test_raw_non_food, train_vector_x, train_vector_y, \
        test_vector_x, test_vector_y, train_vector_num
    train_vector_x, train_vector_y, train_vector_num = [], [], []
    test_vector_x, test_vector_y = [], []
    vector_x = []
    vector_y = []
    for i in train_raw_food:
        tmp = [0 for i in range(len(useful_tag_list))]
        for j in range(0, len(i) - 1, 2):
            if i[j] in useful_dict.keys():
                tmp[useful_dict[i[j]]] = float(
                    i[j + 1]) * correlation_dict[i[j]] + p_food * (1 - float(i[j + 1]))
            else:
                # TODO: should be changed to random probability
                pass
        vector_x.append(tmp)
        vector_y.append("food")
        train_vector_num.append(1)

    for i in train_raw_non_food:
        tmp = [0 for i in range(len(useful_tag_list))]
        for j in range(0, len(i) - 1, 2):
            if i[j] in useful_dict.keys():
                tmp[useful_dict[i[j]]] = float(
                    i[j + 1]) * correlation_dict[i[j]] + p_food * (1 - float(i[j + 1]))
            else:
                # TODO: should be changed to random probability
                pass
        vector_x.append(tmp)
        vector_y.append("no food")
        train_vector_num.append(-1)

    train_vector_x, train_vector_y = vector_x, vector_y

    vector_x, vector_y = [], []

    for i in test_raw_food:
        tmp = [0 for i in range(len(useful_tag_list))]
        for j in range(0, len(i) - 1, 2):
            if i[j] in useful_dict.keys():
                tmp[useful_dict[i[j]]] = float(
                    i[j + 1]) * correlation_dict[i[j]] + p_food * (1 - float(i[j + 1]))
            else:
                # TODO: should be changed to random probability
                pass
        vector_x.append(tmp)
        vector_y.append("food")

    for i in test_raw_non_food:
        tmp = [0 for i in range(len(useful_tag_list))]
        for j in range(0, len(i) - 1, 2):
            if i[j] in useful_dict.keys():
                tmp[useful_dict[i[j]]] = float(
                    i[j + 1]) * correlation_dict[i[j]] + p_food * (1 - float(i[j + 1]))
            else:
                # TODO: should be changed to random probability
                pass
        vector_x.append(tmp)
        vector_y.append("no food")
    test_vector_x, test_vector_y = vector_x, vector_y


def confision_matrix(ground_true, predict, print_result=False):
    TP, FP, FN, TN = 0, 0, 0, 0
    for i in range(len(ground_true)):
        if ground_true[i] == "food" and predict[i] == "food":
            TP += 1
        elif ground_true[i] == "no food" and predict[i] == "food":
            FP += 1
        elif ground_true[i] == "food" and predict[i] == "no food":
            FN += 1
        elif ground_true[i] == "no food" and predict[i] == "no food":
            TN += 1
    TPR = TP / (TP + FN)
    FPR = FP / (FP + TN)
    if print_result:
        print("TP: ", TP, "FN: ", FN, "TN: ", TN, "FP :", FP)
    # print("Sensitivity = ", TP/(TP+FN), end="   ")
    # print("Specificity = ", TN/(TN+FP))
    # print("Precision = ", TP/(TP+FP), end="   ")
    # print("Accuracy = ", (TP + TN)/(TP+TN+FN+FP))
    return TPR, FPR


def clarifai_result():
    global test_raw_food, test_raw_non_food
    TPR_list = []
    FPR_list = []
    for k in range(10):
        TP, FP, FN, TN = 0, 0, 0, 0
        ratio = k / 10
        # print(ratio)
        for i in test_raw_food:
            have = False
            for j in range(len(i)):
                if i[j] == "food" and float(i[j + 1]) > ratio:
                    have = True
            if not have:
                FN += 1
            else:
                TP += 1

        for i in test_raw_non_food:
            have = False
            for j in range(len(i)):
                if i[j] == "food" and float(i[j + 1]) > ratio:
                    have = True
            if not have:
                TN += 1
            else:
                FP += 1

        TPR = TP / (TP + FN)
        FPR = FP / (FP + TN)
        TPR_list.append(TPR)
        FPR_list.append(FPR)
        if k == 9 or k == 8 or k == 7 or k ==6:
        # if k == 7 or k == 6 or k == 5 or k == 4:
            plt.scatter([FPR], [TPR], marker='o', c='green')
        # print("TRP :", TPR)
        # print("FPR :", FPR)
    return TPR_list, FPR_list
        #
    #     print("clarify result**********")
    #     print("TP: ", TP, "FN: ", FN, "TN: ", TN, "FP :", FP)
    #     print("Sensitivity = ", TP / (TP + FN), end="   ")
    #     print("Specificity = ", TN / (TN + FP))
    #     print("Precision = ", TP / (TP + FP), end="   ")
    #     print("Accuracy = ", (TP + TN) / (TP + TN + FN + FP))
    #     print("burden = ", (TP + FP) / (TP +TN+FN+FP))
    # plt.scatter([1 - 0.789866667, 1 - 0.684, 1 - 0.55786, 1-0.4512], [0.584493042, 0.666003976, 0.753479125, 0.833664679], marker='o', c='green')


def get_p_food_before_balance():
    # food_num_ori = 0
    # with open("#food_ori.csv") as f:
    #     csv_reader = csv.reader(f)
    #     for row in csv_reader:
    #         food_num_ori += 1

    # no_food_num_ori = 0
    # with open("#no food_ori.csv") as f:
    #     csv_reader = csv.reader(f)
    #     for row in csv_reader:
    #         no_food_num_ori += 1
    # p_food = food_num_ori / no_food_num_ori
    # return p_food
    # p_food = len(train_raw_food) / (len(train_raw_food) + len(train_raw_non_food))
    # return p_food
    pass


def init(use_all=True):
    global p_food, train_raw_food, train_raw_non_food
    get_raw_data()
    shuffle_raw_data()
    div_train_test_raw_data(0.75)
    save_raw_data_train_test()
    clarifai_result()
    p_food = len(train_raw_food) / (len(train_raw_food) + len(train_raw_non_food))
    get_correlation()
    get_use_tag(use_all)
    construct_train_test_set()

