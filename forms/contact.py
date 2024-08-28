import streamlit as st
import re
import requests

WEBHOOK_URL = "https://connect.pabbly.com/workflow/sendwebhookdata/IjU3NjUwNTY0MDYzZjA0MzQ1MjY0NTUzNTUxMzEi_pc"

def is_valid_email(email):
    # Basic regex pattern for email validation
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, email) is not None

 
def is_valid_number(number):
    # Regular expression to match the standard international mobile number format
    number_pattern = r"^\+?\d{10,15}$"
    return re.match(number_pattern, number) is not None


def contact_form():
    with st.form("contact_form"):
        first_name = st.text_input("First Name", key="key1")
        last_name = st.text_input("Last Name")
        email = st.text_input("Email Address")
        number = st.text_input("Whatsapp Number")
        message = st.text_area("Your Message")
        submit_button = st.form_submit_button("Submit")

    if submit_button:
        if not WEBHOOK_URL:
            st.error("Email service is not set up. Please try again later.", icon="📧")
            st.stop()

        if not first_name:
            st.error("Please provide your first name.", icon="🧑")
            st.stop()

        if not last_name:
            st.error("Please provide your last name.", icon="🧑")
            st.stop()

        if not email:
            st.error("Please provide your email address.", icon="📨")
            st.stop()

        if not is_valid_email(email):
            st.error("Please provide a valid email address.", icon="📧")
            st.stop()

        if not is_valid_number(number):
            st.error("Please provide a valid whatsapp number.", icon="📞")
            st.stop()

        if not message:
            st.error("Please provide a message.", icon="💬")
            st.stop()

        # Prepare the data payload and send it to the specified webhook URL
        data = {"first_name": first_name, "last_name": last_name, "email": email, "number": number, "message": message}
        response = requests.post(WEBHOOK_URL, json=data)

        if response.status_code == 200:
            st.success("Your message has been sent successfully! 🎉", icon="🚀")
        else:
            st.error("There was an error sending your message.", icon="😨")