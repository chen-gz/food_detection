import csv
import os
import numpy as np
import matplotlib.pyplot as plt

folder_list = [
    'PHASE3_HH01_T2_EButtom-402/eButton_Data/Camera/ID0402_Nov.27/7',
    'PHASE3_HH01_T2_EButtom-402/eButton_Data/Camera/ID0402_Nov.27/8',
    'PHASE3_HH01_T2_EButtom-402/eButton_Data/Camera/ID0402_Nov.27/9',
    'PHASE3_HH01_T2_EButtom-402/eButton_Data/Camera/ID0402_Nov.27/10',
    'PHASE3_HH01_T2_EButtom-402/eButton_Data/Camera/ID0402_Nov.27/11',
    'PHASE3_HH01_T2_EButtom-402/eButton_Data/Camera/ID0402_Nov.27/12',
    'PHASE3_HH01_T2_EButtom-402/eButton_Data/Camera/ID0402_Nov.27/13',
    'PHASE3_HH01_T2_EButtom-402/eButton_Data/Camera/ID0402_Nov.27/14',
    'PHASE3_HH01_T2_EButtom-402/eButton_Data/Camera/ID0402_Nov.27/15',
    'PHASE3_HH01_T2_EButtom-402/eButton_Data/Camera/ID0402_Nov.27/18',
    'PHASE3_HH01_T2_EButtom_411-Mother/eButton_Data/Camera/ID0411_Nov.27/8',
    'PHASE3_HH01_T2_EButtom_411-Mother/eButton_Data/Camera/ID0411_Nov.27/9',
    'PHASE3_HH01_T2_EButtom_411-Mother/eButton_Data/Camera/ID0411_Nov.27/10',
    'PHASE3_HH01_T2_EButtom_411-Mother/eButton_Data/Camera/ID0411_Nov.27/11',
    'PHASE3_HH01_T2_EButtom_411-Mother/eButton_Data/Camera/ID0411_Nov.27/12',
    'PHASE3_HH01_T2_EButtom_411-Mother/eButton_Data/Camera/ID0411_Nov.27/13',
    'PHASE3_HH01_T2_EButtom_411-Mother/eButton_Data/Camera/ID0411_Nov.27/14',
    'PHASE3_HH01_T2_EButtom_411-Mother/eButton_Data/Camera/ID0411_Nov.27/15',
    'PHASE3_HH01_T2_EButtom_411-Mother/eButton_Data/Camera/ID0411_Nov.27/16',
    'PHASE3_HH01_T2_EButtom_411-Mother/eButton_Data/Camera/ID0411_Nov.27/17',
    'PHASE3_HH02_T2_eButton-402_Mother/eButton_Data/Camera/ID0402_Nov.28/8',
    'PHASE3_HH02_T2_eButton-402_Mother/eButton_Data/Camera/ID0402_Nov.28/9',
    'PHASE3_HH02_T2_eButton-402_Mother/eButton_Data/Camera/ID0402_Nov.28/10',
    'PHASE3_HH02_T2_eButton-402_Mother/eButton_Data/Camera/ID0402_Nov.28/12',
    'PHASE3_HH02_T2_eButton-402_Mother/eButton_Data/Camera/ID0402_Nov.28/13',
    'PHASE3_HH02_T2_eButton-402_Mother/eButton_Data/Camera/ID0402_Nov.28/14',
    'PHASE3_HH02_T2_eButton-402_Mother/eButton_Data/Camera/ID0402_Nov.28/15',
    'PHASE3_HH02_T2_eButton-402_Mother/eButton_Data/Camera/ID0402_Nov.28/16',
    'PHASE3_HH02_T2_eButton-402_Mother/eButton_Data/Camera/ID0402_Nov.28/17',
    'PHASE3_HH02_T2_eButton-402_Mother/eButton_Data/Camera/ID0402_Nov.28/18',
    'PHASE3_HH02_T2_eButton-411_Adolescent_child/eButton_Data/Camera/ID0411_Nov.28/10',
    'PHASE3_HH02_T2_eButton-411_Adolescent_child/eButton_Data/Camera/ID0411_Nov.28/13',
    'PHASE3_HH02_T2_eButton-411_Adolescent_child/eButton_Data/Camera/ID0411_Nov.28/15',
    'PHASE3_HH02_T2_eButton-411_Adolescent_child/eButton_Data/Camera/ID0411_Nov.28/16',
    'PHASE3_HH02_T2_eButton-411_Adolescent_child/eButton_Data/Camera/ID0411_Nov.28/17',
    'PHASE3_HH02_T2_eButton-411_Adolescent_child/eButton_Data/Camera/ID0411_Nov.28/18',
    'PHASE3_HH02_T4-eButton-411_Mother/eButton_Data/Camera/ID0411_Dec.02/7',
    'PHASE3_HH02_T4-eButton-411_Mother/eButton_Data/Camera/ID0411_Dec.02/8',
    'PHASE3_HH02_T4-eButton-411_Mother/eButton_Data/Camera/ID0411_Dec.02/9',
    'PHASE3_HH02_T4-eButton-411_Mother/eButton_Data/Camera/ID0411_Dec.02/10',
    'PHASE3_HH02_T4-eButton-411_Mother/eButton_Data/Camera/ID0411_Dec.02/11',
    'PHASE3_HH02_T4-eButton-411_Mother/eButton_Data/Camera/ID0411_Dec.02/12',
    'PHASE3_HH02_T4-eButton-411_Mother/eButton_Data/Camera/ID0411_Dec.02/13',
    'PHASE3_HH02_T4-eButton-411_Mother/eButton_Data/Camera/ID0411_Dec.02/14',
    'PHASE3_HH02_T4-eButton-411_Mother/eButton_Data/Camera/ID0411_Dec.02/15',
    'PHASE3_HH02_T4-eButton-411_Mother/eButton_Data/Camera/ID0411_Dec.02/16',

    # new data
    'PHASE3_HH03_eButton-402_Father/eButton_Data/Camera/ID0402_Nov.30/9',
    'PHASE3_HH03_eButton-402_Father/eButton_Data/Camera/ID0402_Nov.30/10',
    'PHASE3_HH03_eButton-402_Father/eButton_Data/Camera/ID0402_Nov.30/11',
    'PHASE3_HH03_eButton-402_Father/eButton_Data/Camera/ID0402_Nov.30/12',
    'PHASE3_HH03_eButton-402_Father/eButton_Data/Camera/ID0402_Nov.30/13',
    'PHASE3_HH03_eButton-402_Father/eButton_Data/Camera/ID0402_Nov.30/14',
    'PHASE3_HH03_eButton-402_Father/eButton_Data/Camera/ID0402_Nov.30/15',
    'PHASE3_HH03_eButton-402_Father/eButton_Data/Camera/ID0402_Nov.30/16',
    'PHASE3_HH03_eButton-402_Father/eButton_Data/Camera/ID0402_Nov.30/17',

    'PHASE3_HH03_eButton-411_Mother/eButton_Data/Camera/ID0411_Nov.30/8',
    'PHASE3_HH03_eButton-411_Mother/eButton_Data/Camera/ID0411_Nov.30/9',
    'PHASE3_HH03_eButton-411_Mother/eButton_Data/Camera/ID0411_Nov.30/10',
    'PHASE3_HH03_eButton-411_Mother/eButton_Data/Camera/ID0411_Nov.30/13',
    'PHASE3_HH03_eButton-411_Mother/eButton_Data/Camera/ID0411_Nov.30/14',
    'PHASE3_HH03_eButton-411_Mother/eButton_Data/Camera/ID0411_Nov.30/15',
    'PHASE3_HH03_eButton-411_Mother/eButton_Data/Camera/ID0411_Nov.30/16',
    'PHASE3_HH03_eButton-411_Mother/eButton_Data/Camera/ID0411_Nov.30/17',

    'PHASE3_HH03_T4_eBUTTON_402-ADOLESCENT_BOY/eButton_Data/Camera/ID0402_Dec.03/8',
    'PHASE3_HH03_T4_eBUTTON_402-ADOLESCENT_BOY/eButton_Data/Camera/ID0402_Dec.03/9',
    'PHASE3_HH03_T4_eBUTTON_402-ADOLESCENT_BOY/eButton_Data/Camera/ID0402_Dec.03/10',
    'PHASE3_HH03_T4_eBUTTON_402-ADOLESCENT_BOY/eButton_Data/Camera/ID0402_Dec.03/11',
    'PHASE3_HH03_T4_eBUTTON_402-ADOLESCENT_BOY/eButton_Data/Camera/ID0402_Dec.03/12',
    'PHASE3_HH03_T4_eBUTTON_402-ADOLESCENT_BOY/eButton_Data/Camera/ID0402_Dec.03/13',
    'PHASE3_HH03_T4_eBUTTON_402-ADOLESCENT_BOY/eButton_Data/Camera/ID0402_Dec.03/14',
    'PHASE3_HH03_T4_eBUTTON_402-ADOLESCENT_BOY/eButton_Data/Camera/ID0402_Dec.03/15',
    'PHASE3_HH03_T4_eBUTTON_402-ADOLESCENT_BOY/eButton_Data/Camera/ID0402_Dec.03/16',

    'PHASE3_HH05_eButton-402_Father/eButton_Data/Camera/ID0402_Dec.05/7',
    'PHASE3_HH05_eButton-402_Father/eButton_Data/Camera/ID0402_Dec.05/8',
    'PHASE3_HH05_eButton-402_Father/eButton_Data/Camera/ID0402_Dec.05/9',
    'PHASE3_HH05_eButton-402_Father/eButton_Data/Camera/ID0402_Dec.05/10',
    'PHASE3_HH05_eButton-402_Father/eButton_Data/Camera/ID0402_Dec.05/11',
    'PHASE3_HH05_eButton-402_Father/eButton_Data/Camera/ID0402_Dec.05/12',
    'PHASE3_HH05_eButton-402_Father/eButton_Data/Camera/ID0402_Dec.05/13',
    'PHASE3_HH05_eButton-402_Father/eButton_Data/Camera/ID0402_Dec.05/14',

]


from shutil import copyfile
import time

def construct_vector(folder_path):
    label_file_name = "label.csv"
    clarify_result_name = "clarify_result.csv"
    label_filepath = os.path.join(folder_path, label_file_name)
    clarify_result_filepath = os.path.join(folder_path, clarify_result_name)
    if not os.path.exists(label_filepath) and not os.path.exists(
            clarify_result_filepath):
        print('no label file and clarify result file')
    vector_x, vector_y, vector_time = [], [], []
    label_list = []
    clarify_list = []
    with open(label_filepath) as f:
        label_reader = csv.reader(f, delimiter=',')
        for row in label_reader:
            label_list.append(row)
    with open(clarify_result_filepath) as f:
        clarify_reader = csv.reader(f, delimiter=',')
        for row in clarify_reader:
            clarify_list.append(row)
    for i in range(len(label_list)):
        for j in range(len(label_list[i])):
            label_list[i][j] = label_list[i][j].strip()
    for i in range(len(clarify_list)):
        for j in range(len(clarify_list[i])):
            clarify_list[i][j] = clarify_list[i][j].strip()
    food_name_list = []
    no_food_name_list = []
    
    food_rectify = []
    with open("./food_rectify.csv") as f:
        for line in f:
            food_rectify.append(line.strip()+'.jpg') 

    for i in clarify_list:
        for j in label_list:
            if os.path.basename(i[0]) in j:
                vector_time.append(j[0])
                print(j[1])
                tmp_with_name = [j[1]]
                tmp_with_name += i[1:]
                if tmp_with_name[0] in food_rectify:
                    vector_y.append(1)
                    # vector_x.append(i[1:])
                    vector_x.append(tmp_with_name)
                    food_name_list.append(j[1])
                else:
                    if int(j[2]) >= 3:  # 3 and 4 recognized as food
                        vector_y.append(1)
                        # vector_x.append(i[1:])
                        vector_x.append(tmp_with_name)
                        food_name_list.append(j[1])
                    else:
                        vector_y.append(0)
                        # vector_x.append(i[1:])
                        vector_x.append(tmp_with_name)
                        no_food_name_list.append(j[1])

    t = time.time()
    for root, dirs, files in os.walk('./', topdown=False):
        for name in files:
            if name in food_name_list:
                src = os.path.join(root,name)
                dst = os.path.join('../food_detection_data/food', name)
                # if os.path.isfile(dst):
                #     dst = os.path.join('./food/' , str(int(t)) + name)
                copyfile(src,dst)

                print(src)
                print(dst)
            if name in no_food_name_list:
                src = os.path.join(root,name)
                dst = os.path.join('../food_detection_data/no_food', name)
                # if os.path.isfile(dst):
                #     dst = os.path.join('./no_food/' ,str(int(t)) + name)
                print(src)
                print(dst)
                copyfile(src,dst)

    return vector_x, vector_y, vector_time


def construct_food_no_food(folder_name):
    vector_x, vector_y, _ = construct_vector(folder_name)
    # print(_)
    food_csv = 'food.csv'
    no_food_csv = 'no_food.csv'
    food_file = open(food_csv, 'a')
    no_food_file = open(no_food_csv, 'a')
    for i in range(len(vector_y)):
        if vector_y[i] == 1:
            food_file.write(','.join(vector_x[i]))
            food_file.write('\n')
        else:
            no_food_file.write(','.join(vector_x[i]))
            no_food_file.write('\n')
    food_file.close()
    no_food_file.close()


if __name__ == '__main__':
    section = [10, 10, 10, 6, 10, 9, 8, 9, 8]
    # for i in range(10):
    #     vector_x, vector_y, _ = construct_vector(folder_list[i])
    #     tmp_vector_y = [str(i) for i in vector_y]
    #     print(' '.join((tmp_vector_y)))
    #     plt.scatter(range(len(vector_y)), vector_y, s=0.5)
    #     plt.show()
    # for i in range(0, 5):
    #     vector_x, vector_y, vector_time = construct_vector(folder_list[i])
    #     vector_y = list(map(str, vector_y))
    #     print(' '.join(vector_y))

    # second = [i for i in range(40)] + [i for i in range(36,46)]
    # print(second)
    # for i in second:
    for i in range(0, sum(section)):
       construct_food_no_food(folder_list[i])
