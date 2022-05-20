import streamlit as st
import streamlit_authenticator as stauth
from datetime import datetime
from PIL import Image
Icon = Image.open('ICHOS.png')
favIcon = Image.open('ICHOremovebgpng.png')
import pandas as pd
import numpy as np





#setting page to auto into wide mode
st.set_page_config(page_title="ichos",page_icon=favIcon)

names = ['ICHOS', 'aadil']
usernames = ['DPR', 'aadil']
passwords = ['LEEzkH', 'aadil']

hashed_passwords = stauth.hasher(passwords).generate()

authenticator = stauth.authenticate(names,usernames,hashed_passwords,
    'biscuit','biscuit_monster420',cookie_expiry_days=30)

name, authentication_status = authenticator.login('Login','main')



if st.session_state['authentication_status']:
    
    st.title('Hal')
    q1 = "Hi, how are you feeling today"
    q2 = "Understood! How would you describe an ideal emotional state for you?"
    @st.cache(allow_output_mutation=True)
    def get_data():
        return []
    
    st.write(q2)
    with st.form(key='f1'):
        answer = st.text_input(label = "Type your reply")
        submit = st.form_submit_button(label = 'enter')
        
        
    if st.button("Send"):
        #df = []
        get_data().append({"answer": answer})
        df = pd.DataFrame(get_data())
        st.dataframe(df)
        np.savetxt(r'.\\input.txt', df.values, fmt='"%s"')
        q1 = q2

    #  st.image(Icon, caption='Welcome to Ichos', width = 300)
    # Declare a form and call methods directly on the returned object
    
    
    

        
elif st.session_state['authentication_status'] == False:
    st.error('Username/password is incorrect')
elif st.session_state['authentication_status'] == None:
    st.warning('Please enter your username and password')





