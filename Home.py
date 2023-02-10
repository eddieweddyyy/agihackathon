import streamlit as st, base64

st.title("Probability Calculator")

st.write("The Probability Calculator Tool will help The Good Acre accurately plan and forecast production for farmers. This tool will provide insights into the reliability of forecasts that will aid in contract decision making.")
# which producsts are being forecasted more accurately, which ones are able to meet quotas
# better info that allows for higher contract quotas, not leave any money on the table, inc the volume that 
# we contract for; how we envision you using it, at conference every year looks at everyone and be armed with app
# refresh every year with new data
# build off of it in the future - what do you do once you get the information back?
# take pricing out of app -> add, test with you more, not central, uuseful to incorporate reliability in procong to help farmers improve reliability
# poor producing performers - readjust expectations, find a potential process problem so TGA can provide support and more service to get yields mroe reliabel
# top pro - double down, contract more aggressively
def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(https://thegoodacre.org/wp-content/uploads/2022/02/tga_logo_2022_rev-400px.png);
                background-repeat: no-repeat;
                background-size: 230px;
                padding-top: 10px;
                background-position: 20px 20px;
                width: 300px;
                height: auto;
                margin-left: auto;
                margin-right: auto;

            }
                [data-testid="stSidebarNav"]::before {
                content: "";
                margin-left: 20px;
                margin-top: 10px;
                font-size: 25px;
                position: relative;
                top: 100px;
            }

        </style>
        """,
        unsafe_allow_html=True,
    )
add_logo()

# def img_background(img):
#     with open(img, "rb") as image_file:
#         encoded_string = base64.b64encode(image_file.read())
#     st.markdown(
#         f"""
#         <style>
#         ."css-bdg44w e1fqkh3o11" {{
#             background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
#             background-size: cover;

#             filter: blur(5px);
#         }}

#         </style>
#         """,
#         unsafe_allow_html=True
#     )
# img_background('background2.jpg')