import streamlit as st, csv, Home
Home.add_logo()


def main():
    st.write("Product Success Rate")
    with st.form(key = "tab1"):
        
        product = st.text_input("Enter product code: ")
        prob_delivery = calculate_delivery(product)

        submitted = st.form_submit_button("Enter")

        if submitted:
            if prob_delivery > 1:
                prob_delivery = 1
            # prob_delivery = round(prob_delivery, 2)
            st.write(str(round(prob_delivery*100, 2)) + "%")


def counts(fname, product):
    count = 0

    with open(fname) as fp:
        filereader = csv.reader(fp)
        for i in filereader:
            if product in i:
                count += 1
    return count


def calculate_delivery(product):
    count_plan = counts("Combined_Planning.csv", product)
    count_order = counts("Combined_Orders.csv", product)
    
    return count_order / count_plan


main()