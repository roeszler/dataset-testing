import streamlit as st
from app_page.multi_page import MultiPage

from app_page.page1 import page1_body
from app_page.page2 import page2_body
from app_page.page3 import page3_body
from app_page.page4 import page4_body
from app_page.page5 import page5_body
from app_page.page6 import page6_body

# define the app_name argument, give it a string to be used everywhere app_name is used.
app = MultiPage(app_name= "This is my first multi page Streamlit App")

# add each page
app.app_page("Page 1", page1_body)
app.app_page("Page 2", page2_body)
app.app_page("Page 3", page3_body)
app.app_page("Page 4", page4_body)
app.app_page("Page 5", page5_body)
app.app_page("Page 6", page6_body)

app.run()