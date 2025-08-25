# import streamlit as st
# st.title("Hello,Edukron")
# st.write("This is a sample streamlin app")




# import streamlit as st
# name = st.text_input("Enter the name: ")
# age = st.number_input(" Enter the age: ")
# if st.button("Submit"):
#     st.write(f"Hello {name}, you are {age} yr old")




# import streamlit as st
# number = st.slider("Pick number: ",1,100)
# st.write(f"you selected {number}")





# import streamlit as st
# import pandas as pd
# import numpy as np

# df = pd.DataFrame(np.random.randn(10,2), columns=['x','y'])
# st.write("Random DataFrame:")
# st.dataframe(df)





# import streamlit as st
# # if st.checkbox("show box: "):
# #     st.write("your checkbox is clicked")



# # gender = st.radio("select gender",('Male','Female','other')) 
# # st.write(f"you selected {gender}")


# option = st.selectbox("Choose an option", ["Option 1", "Option 2", "Option 3"])
# st.write(f"You chose: {option}")   




# import streamlit as st
# import time

# progress = st.progress(0)
# for i in range(100):
#     time.sleep(0.05)
#     progress.progress(i + 1)




# import streamlit as st

# hobbies = st.multiselect("Choose your hobbies", ["Reading", "Sports", "Coding", "Traveling"])
# st.write("You selected:", hobbies)




# import streamlit as st
# from datetime import time

# t = st.time_input("Pick a time")
# st.write("Selected time:", t)



# import streamlit as st

# st.metric(label="Revenue", value="$12,000", delta="+5%")
# st.metric(label="Users", value="1,200", delta="-2%")





# import streamlit as st

# tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])

# with tab1:
#     st.write("Content for Tab 1")

# with tab2:
#     st.write("Content for Tab 2")







