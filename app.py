from PIL import Image
import requests 
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="vend here ",page_icon = ": tada :", layout ="wide")

def load_lottieurl(url):
    r= requests.get(url)
    if r.status_code !=200 :
        return None
    return r.json()

# Use local CSS 
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

local_css=("style/style.css")
#animation through lottiefiles
lottie_coding=load_lottieurl("https://assets7.lottiefiles.com/private_files/lf30_d16uoqsh.json")
img_contact_form =Image.open("images/yt_contact_form.png")
img_lottie_animation =Image.open("images/yt_lottie_animation.png")

#header section---
st.subheader(" vending machine at adt")
st.title("A new way to catch up with snacks ")
st.write("this page contains all your queries related to vending machine! ")
st.write("if you are new NO WORRIES ")
st.write("[learn the use >](https://www.youtube.com/watch?v=Fy042phZLRg)")

with st.container():
    st.write("---")
    left_column,right_column=st.columns((1,2))
    with left_column:
        st.write("$$$$$")
        st.write(''' we are introducing a new way for mitians to get their snacks and foods from the vending machine....
            We have seen our fellows running from tuck shop to their destinations (classes)
            between the breaks for 15 min which take them to travel from SOE building to get the lift on time.
            and many more problems faced by them.
                
            thus, what if we get our snacks in our places 
            like in IT building and many more parts of MIT
            -adt university from without going through a
            lengthy process of getting out of the building 
            ,taking tokens and then getting desired food.  
                ''')
    with right_column:
        st_lottie(lottie_coding,height =500,key = "vending machine ")

        #--contact about item --
with st.container():
    st.write("---")
    st.header("the items available ")
    st.write("##")
    image_column,text_column=st.columns((1,2))
    with image_column:
        st.image(img_lottie_animation) 
        
    with text_column:
        st.subheader("Queriies and comments ")
        st.write(
            """
                here all your quieries and commments will be answerd ,
                In this section right now i'm not adding but i will soon !
            """
        )
        st.markdown("[watch video to paste quiries.....](https://www.quackit.com/html/codes/add_comments_to_website.cfm)")
#---contact

with st.container():
    image_column,text_column= st.columns((1,2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("all sort of Healthy liquids ")
        st.write("here you can have multiple snacks item like Heathy juices")
        st.markdown("adding no links here --->")
        #documentation : https://formsubmit.co/ change email address!!!
    contact_form ="""
        <form action="https://formsubmit.co/charliee.rodriguez666@gmail.com" method="POST">
        <input type ="hidden" name "_captcha " vaue="false" >
     <input type="text" name="name" placeholder= "Your name" required>
     <input type="email" name="email" placeholder = "Your email" required>
     <textarea name ="message" placeholder= "Your comment here" required></textarea>
     <button type="submit">Send</button>
     </form>"""
    left_column,right_column=st.columns(2)
    with left_column:
        st.markdown(contact_form,unsafe_allow_html=True)
    with right_column:
        st.empty()