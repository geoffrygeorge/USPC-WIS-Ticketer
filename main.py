import streamlit as st

def main():
    st.set_page_config(
        page_title="USPC Ticketer",
        page_icon="🎟️",
        initial_sidebar_state="auto",
        layout="centered",
        menu_items={
            "Report a bug": "mailto:jeffrygeorge58@gmail.com",
            "About": "USPC Manchester's Official Ticket Booking Application v1.0 ® 2026. All Rights Reserved."
        }
    )
    
    nav_pages = [
        st.Page("home.py"),
        st.Page("pages/single_main.py"),
        st.Page("pages/multiple_main.py")
    ]

    ticketer_pages = st.navigation(pages=nav_pages, position="hidden")
    
    ticketer_pages.run()

if __name__ == '__main__':
    main()
