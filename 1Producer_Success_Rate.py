import streamlit as st, csv, Home
Home.add_logo()

delivery_success = 1
# About.img_background('background.jpg')
    
def main():
    st.write("Producer Success Rate")
    with st.form(key = "tab1"):
        
        producer = st.text_input("Enter producer code: ")
        prob_delivery = calculate_delivery(producer)

        submitted = st.form_submit_button("Enter")

        if submitted:
            if prob_delivery > 1:
                prob_delivery = 1
            # prob_delivery = round(prob_delivery, 2)
            st.write(str(round(prob_delivery*100, 2)) + "%")


def counts(fname, producer):
    count = 0

    with open(fname) as fp:
        filereader = csv.reader(fp)
        for i in filereader:

            if producer in i:
                count += 1
    return count


def calculate_delivery(producer):
    count_plan = counts("Combined_Planning.csv", producer)
    count_order = counts("Combined_Orders.csv", producer)
    
    return count_order / count_plan


main()
