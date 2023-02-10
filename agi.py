import csv
import datetime
list_of_plan = ["Combined_Planning.csv"]
list_of_order = ["Combined_Orders.csv"]
list_of_water = []

filename = input("Type your file name: ")

for i in filename:
    if "plan" in filename: #change to streamlit style
        list_of_plan.append(filename)
    elif "order" in filename:
        list_of_order.append(filename)
    elif "water" in filename:
        list_of_water.append(filename)

def counts(fname, producer):
    count = 0
    #change to streamlit style

    with open(fname) as fp:
        filereader = csv.reader(fp)
        for i in filereader:
            # print(i)
            if producer in i:
                count += 1
    return count

def calc_prob_deliv():
    
    count_plan = 0
    count_order = 0

    # type_of_input = input()
   
    prod = input("Type product ID or producer code: ")

    for i in list_of_plan:
        count_plan += counts(i, prod)
    for j in list_of_order:
        count_order += counts(j, prod)
    
    return count_order / count_plan

# print(calc_prob_deliv())

# Given a specific product, what is the probability that it will be delivered in the week specified?

def open_week(fn, product):
    lst = []
    with open(fn) as fp:
        filereader = csv.reader(fp)
        for i in filereader:
            if product in i:
                lst.append(i[-1])
    # print(lst)
    return lst

def calc_prob_week():
    product = input("Type product ID: ")
    week = input("Type week: ")

    ls_p = []
    ls_o = []
    
    for i in list_of_plan:
        plan = (open_week(i, product))
    for k in plan:
        if k == week:
            ls_p.append(k)
    for j in list_of_order:
        order = (open_week(j, product))
    for m in order:
        if m == week:
            ls_o.append(m)

    return len(ls_o) / len(ls_p)

print(calc_prob_week())

# dic {producer code: product ID}

def open_week_and_prod(fn, product, producer):
    lst = []
    with open(fn) as fp:
        filereader = csv.reader(fp)
        for i in filereader:
            if product in i and producer in i:
                lst.append(i[-1])
    # print(lst)
    return lst

def calc_prob_week_prod():
    product = input("Type product ID: ")
    week = input("Type week: ")
    producer = input("Type producer code: ")

    ls_p = []
    ls_o = []
    
    for i in list_of_plan:
        plan = (open_week(i, product, producer))
    for k in plan:
        if k == week:
            ls_p.append(k)
    for j in list_of_order:
        order = (open_week(j, product, producer))
    for m in order:
        if m == week:
            ls_o.append(m)

    return len(ls_o) / len(ls_p)


input4 = int(input("What is the percentage you consider as succsessful? "))

def calc_plan_fact():
   
    cal3 = calc_prob_week_prod()
  
    print("Success rate of combined data is %b", cal3)

    if input4 > int(cal3):
        print("%d is %b percent smaller than %s", cal3, input4 - cal3, input4)
        print("You might want to re-cosider choosing this product and producer in the given week")
    else:
        print("%d is %b percent greater than %s", cal3, cal3 - input4, input4)
        print("Choosing this product and producer in the given week looks good!")
