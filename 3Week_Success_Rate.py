import streamlit as st, csv, datetime, Home
Home.add_logo()

def main():
    st.write("Week Success Rate")
    with st.form(key = "tab1"):
        week = st.date_input("Enter week:")
        
        
        product = st.text_input("Enter Product ID:")
        submitted = st.form_submit_button("Enter")
        if submitted:
            week = str(week.isocalendar().week)
            week_prob = calc_prob_week(week, product)
            st.write(str(round(week_prob*100, 2)) + "%")


def open_week(fn, product):
    lst = []
    with open(fn) as fp:
        filereader = csv.reader(fp)
        for i in filereader:
            if product in i:
                lst.append(i[-1])
    return lst

def calc_prob_week(week, product):
    ls_p = []
    ls_o = []
    
    plan = (open_week("Combined_Planning.csv", product))
    for k in plan:
        if k == week:
            ls_p.append(k)

    order = (open_week("Combined_Orders.csv", product))
    for m in order:
        if m == week:
            ls_o.append(m)

    return len(ls_o) / len(ls_p)

main()