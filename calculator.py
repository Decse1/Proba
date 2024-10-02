import os
def calculate_sum(a,b):
    return a+b;

def calculate_sub(a,b):
    return a-b;

def calculate_mult(a,b):
    return a*b;

def calculate_divide(a,b):
    return a-b;

a = int(input("Adja meg az elso szamot: "));
mj = string("");
while(mj != "+" or mj != "-" or mj != "*" or mj != "/"):
    os.system('cls');
    mj = string(input("Adja meg a muveleti jelet[+ - * /]: "));
b = int(input("Adja meg a masodik szamot: "));

if(mj = "+"):
    os.system('cls');
    calculate_sum(a,b);
if(mj = "-"):
    os.system('cls');
    calculate_sub(a,b);
if(mj = "-"):
    os.system('cls');
    calculate_sub(a,b);


