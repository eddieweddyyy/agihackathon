import streamlit as st, csv, Home

Home.add_logo()
delivery_success = 1
    
def main():
    st.write("Overall Success Rate")
    with st.form(key = "tab1"):
        
        producer = st.text_input("Enter producer code:")
        product = st.text_input("Enter product code:")
        week = st.date_input("Enter week:")
        goal_percentage = st.number_input("Enter goal percentage (%):")
        goal_percentage = goal_percentage*0.01
        week = str(week.isocalendar().week)
        # prob_delivery = calculate_delivery(producer)

        submitted = st.form_submit_button("Enter")
       

        if submitted:
            week_prob = calc_prob_week(week, product, producer)
            if week_prob > 1:
                week_prob = 1
            # round(week_prob, 2)
            st.write("Overall Success Rate: " + str(round(week_prob*100, 2)) + "%")
            if goal_percentage > week_prob:
                st.write("You will fall short of your goal by", round((goal_percentage - week_prob)*100, 2), "%")
            elif goal_percentage == week_prob:
                st.write("You have met the goal percentage exactly!")
            else:
                st.write("You have exceeded your goal percentage by", round((week_prob - goal_percentage)*100, 2), "%")

        st.write()


# def counts(fname, producer):
#     count = 0

#     with open(fname) as fp:
#         filereader = csv.reader(fp)
#         for i in filereader:

#             if producer in i:
#                 count += 1
#     return count


# def calculate_delivery(producer):
#     count_plan = counts("Combined_Planning.csv", producer)
#     count_order = counts("Combined_Orders.csv", producer)
    
#     return count_order / count_plan


def open_week(fn, product, producer):
    lst = []
    with open(fn) as fp:
        filereader = csv.reader(fp)
        for i in filereader:
            if product in i and producer in i:
                lst.append(i[-1])
    return lst

def calc_prob_week(week, product, producer):
    ls_p = []
    ls_o = []
    
    plan = (open_week("Combined_Planning.csv", product, producer))
    for k in plan:
        if k == week:
            ls_p.append(k)

    order = (open_week("Combined_Orders.csv", product, producer))
    for m in order:
        if m == week:
            ls_o.append(m)
    return len(ls_o) / len(ls_p)

main()
