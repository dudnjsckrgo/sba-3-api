import pip
from subprocess import call
call("conda activate C:/Users/dudnj/anaconda3/envs/tensecpu")
with open('/Users/dudnj/requirements.txt', encoding='utf-8-sig',mode='r') as file:
    for library_name in file.readlines():
        call("conda install -y " + library_name, shell=True)