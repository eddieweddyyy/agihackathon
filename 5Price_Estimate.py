import streamlit as st, csv, Home
Home.add_logo()


def main():
    st.write("Price Estimator")

    with st.form(key = "calc"):
        
        contract_price = st.number_input("Price per contract:")
        sales_price = st.number_input("Sales price:")
        order_quantity = st.number_input("Order Quantity:")
        producer = st.text_input("Producer ID:")

        submitted = st.form_submit_button("Enter")

        prob_delivery = calculate_delivery(producer)

        if submitted:
            estimated_price = calculate_price(contract_price, order_quantity, sales_price, prob_delivery)
            estimated_price = round(estimated_price, 2)
            st.write(estimated_price)
    

def calculate_price(price_per_contract, seller_price, order_qnt = 1, farmer_prob = 1):
    
    total_value = price_per_contract / farmer_prob
    item_spread = total_value / order_qnt
    offer_price = seller_price - item_spread
    return offer_price

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



