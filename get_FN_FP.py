import shutil
import os

FP, FN = [], []
with open('FP.txt') as f:
    for row in f:
        FP.append(row.strip())
with open('FN.txt') as f:
    for row in f:
        FN.append(row.strip())
FP = list(set(FP))
FN = list(set(FN))


for root, dirs, files in os.walk('.'):
    for f in files:
        if f in FP:
            src = os.path.join(root, f)
            dst = './FP/' + f
            if not os.path.isfile(dst):
                shutil.copyfile(src, dst)

        if f in FN:
            src = os.path.join(root, f)
            dst = os.path.join('./FN/', f)
            if not os.path.isfile(dst):
                shutil.copyfile(src, dst)


# print(os.path.join(root, name))
# shutil.copyfile(src, dst, *, follow_symlinks=True)
