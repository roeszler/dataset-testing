import streamlit as st
from app_pages.multi_page import MultiPage

# load pages scripts
from app_pages.page_summary import page_summary_body
from app_pages.page_inspect_data import inspect_data_body
from app_pages.page_1 import page1_body
from app_pages.page_2 import page2_body
from app_pages.page_3 import page3_body
from app_pages.page_4 import page4_body
from app_pages.page_5 import page5_body
from app_pages.page_6 import page6_body
from app_pages.page_calculator import page_calculator_body
from app_pages.page_commands_and_widgets import page_commands_and_widgets_body

app = MultiPage(app_name= "DataTester") # Create an instance of the app 

# Add your app pages here using .add_page()
app.add_page("Import and Inspect Data", inspect_data_body)
app.add_page("Commands & Widgets", page_commands_and_widgets_body)
app.add_page("Calculator", page_calculator_body)
app.add_page("Quick Project Summary", page_summary_body)
app.add_page("Page 1", page1_body)
app.add_page("Page 2", page2_body)
app.add_page("Page 3", page3_body)
app.add_page("Page 4", page4_body)
app.add_page("ML Model 1: Page 5", page5_body)
app.add_page("ML Model 2: Page 6", page6_body)

app.run() # Run the  app