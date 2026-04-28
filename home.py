import streamlit as st
from datetime import datetime

@st.dialog(" ", width="small", dismissible=True)
def select_booking():
    st.subheader("Welcome to :primary[USPC Manchester's Official Ticket Booker]", width="stretch")

    st.divider()

    st.warning("Please choose **Single** or **Multiple** option to proceed with the respective ticket creation process.")

    options = ["Single", "Multiple"]
    booking_option = st.pills(
        "Select", options, label_visibility="collapsed", selection_mode="single", default=None, width="stretch"
    )
    if booking_option == "Single":
        st.switch_page("pages/single_main.py")
    elif booking_option == "Multiple":
        st.switch_page("pages/multiple_main.py")

    todays_date = datetime.now().strftime("%d/%m/%Y")
    st.text(f"Date: {todays_date}")

EMPTY_COL_1, BOOKING_BUTTON_COLUMN, EMPTY_COL_2 = st.columns([2, 2, 2], gap="small", vertical_alignment="center")
with BOOKING_BUTTON_COLUMN:
    if st.button("BOOK NOW!", icon=":material/event_available:", type="primary", key="booking_primary", width="stretch", help="Start Booking!"):
        select_booking()
        