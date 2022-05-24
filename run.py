import os

import argparse
parser = argparse.ArgumentParser()

parser.add_argument('-method', default=None, type=str)
parser.add_argument('-gpu', default=1, type=int)
# parser.add_argument('-method', default=None, type=str)

opt = parser.parse_args()

gpu = str(opt.gpu)

if opt.method == 'ewc':
    os.system("python main.py -method=ewc -gpu="+ gpu + " -comment=fg -distill_frac=1 -data_name=bank")
    os.system("python main.py -method=ewc -gpu="+ gpu + " -comment=fg -distill_frac=2 -data_name=blast_char")
    os.system("python main.py -method=ewc -gpu="+ gpu + " -comment=fg -distill_frac=1 -data_name=income")
    os.system("python main.py -method=ewc -gpu="+ gpu + " -comment=fg -distill_frac=1 -data_name=shoppers")
    os.system("python main.py -method=ewc -gpu="+ gpu + " -comment=fg -distill_frac=1 -data_name=shrutime")
    os.system("python main.py -method=ewc -gpu="+ gpu + " -comment=fg -distill_frac=1 -data_name=volkert -class_inc")

if opt.method == 'ours_ewc':
    os.system("python main.py -method=ours_ewc -gpu="+ gpu + " -comment=fg -distill_frac=0.5 -alpha=0.2 -beta=0.1 -gamma=15 -data_name=bank")
    os.system("python main.py -method=ours_ewc -gpu="+ gpu + " -comment=fg -distill_frac=0.5 -alpha=0.3 -beta=0.5 -gamma=10 -data_name=blast_char")
    os.system("python main.py -method=ours_ewc -gpu="+ gpu + " -comment=fg -distill_frac=1 -alpha=0.1 -beta=0.5 -gamma=25 -data_name=income")
    os.system("python main.py -method=ours_ewc -gpu="+ gpu + " -comment=fg -distill_frac=0.5 -alpha=0.4 -beta=2 -gamma=25 -data_name=shoppers")
    os.system("python main.py -method=ours_ewc -gpu="+ gpu + " -comment=fg -distill_frac=1 -alpha=0.2 -beta=1 -gamma=15 -data_name=shrutime")
    os.system("python main.py -method=ours_ewc -gpu="+ gpu + " -comment=fg -distill_frac=1 -alpha=0.2 -beta=1 -gamma=10 -data_name=volkert -class_inc")

if opt.method == 'pnn':
    os.system("python main.py -method=pnn -gpu="+ gpu + " -comment=fg -data_name=bank")
    os.system("python main.py -method=pnn -gpu="+ gpu + " -comment=fg -data_name=blast_char")
    os.system("python main.py -method=pnn -gpu="+ gpu + " -comment=fg -data_name=income")
    os.system("python main.py -method=pnn -gpu="+ gpu + " -comment=fg -data_name=shoppers")
    os.system("python main.py -method=pnn -gpu="+ gpu + " -comment=fg -data_name=shrutime")
    os.system("python main.py -method=pnn -gpu="+ gpu + " -comment=fg -data_name=volkert -class_inc")

if opt.method == 'joint':
    os.system("python main.py -method=joint -gpu="+ gpu + " -comment=fg -data_name=bank")
    os.system("python main.py -method=joint -gpu="+ gpu + " -comment=fg -data_name=blast_char")
    os.system("python main.py -method=joint -gpu="+ gpu + " -comment=fg -data_name=income")
    os.system("python main.py -method=joint -gpu="+ gpu + " -comment=fg -data_name=shoppers")
    os.system("python main.py -method=joint -gpu="+ gpu + " -comment=fg -data_name=shrutime")
    os.system("python main.py -method=joint -gpu="+ gpu + " -comment=fg -data_name=volkert -class_inc -lr=0.0005")