# import streamlit as st
# import pyperclip
# from gpt_utility import call_open_ai_chatcompletion_api, payload_for_api

# st.markdown(
#     """
#     <div style="text-align:center; font-size:42px; font-family: 'Times New Roman', Times, serif;">
#         <strong>Email Generator</strong>
#     </div>
#     """,
#     unsafe_allow_html=True
# )

# st.sidebar.title("Choose Email Tone")
# tone_options = ["Professional", "Friendly", "Neutral", "Strict to the Point"]
# selected_tone = st.sidebar.selectbox("", tone_options, index=0)

# # Input for Subject with a placeholder
# subject = st.text_input("Enter Email Subject:", placeholder="e.g., Board Meeting Agenda")

# # Input for Details with a placeholder
# email_content = st.text_area("Add Email Details:", placeholder="e.g., Discuss about revenue, upcoming financial year goals, promotions, rewards, Bonus")

# generated_email = False
# # Generate Email
# if st.button("Generate Email"):
#     with st.spinner("Generating email..."):
#         if selected_tone and subject and email_content:
#             # Call the API - 3.5-turbo
            
#             payload = payload_for_api(selected_tone, subject, email_content)
#             generated_email = call_open_ai_chatcompletion_api(payload)
#             email = f"Subject: {selected_tone}\n\n{subject}\n\n{email_content}"
#             st.text("Generated Email:")
#             st.text_area(
#                 label="Email Content",  # Provide a descriptive label
#                 value=generated_email,
#                 height=400,
#                 key="email_content",  # Assign a key to the element
#                 help="This is the generated email content.",  # Optional help text
#             )
#         else:
#             st.warning("Please select tone, and enter subject and email_content to generate the email.")
#     if generated_email:
#         if st.button("Copy to Clipboard"):
#             pyperclip.copy(generated_email)
#             st.success("Text copied to clipboard")

# -----------------------------------------------------------------------------------------------------------------------------
# import streamlit as st
# import pyperclip
# from gpt_utility import call_open_ai_chatcompletion_api, payload_for_api

# st.markdown(
#     """
#     <div style="text-align:center; font-size:42px; font-family: 'Times New Roman', Times, serif;">
#         <strong>Email Generator</strong>
#     </div>
#     """,
#     unsafe_allow_html=True
# )

# st.sidebar.title("Choose Email Tone")
# tone_options = ["Professional", "Friendly", "Neutral", "Strict to the Point"]
# selected_tone = st.sidebar.selectbox("", tone_options, index=0)

# # Input for Subject with a placeholder
# subject = st.text_input("Enter Email Subject:", placeholder="e.g., Board Meeting Agenda")

# # Input for Details with a placeholder
# email_content = st.text_area("Add Email Details:", placeholder="e.g., Discuss about revenue, upcoming financial year goals, promotions, rewards, Bonus")

# generated_email = None  # Initialize as None

# # Generate Email
# if st.button("Generate Email"):
#     with st.spinner("Generating email..."):
#         if selected_tone and subject and email_content:
#             # Call the API - 3.5-turbo
#             payload = payload_for_api(selected_tone, subject, email_content)
#             generated_email = call_open_ai_chatcompletion_api(payload)
#             email = f"Subject: {selected_tone}\n\n{subject}\n\n{email_content}"
#         else:
#             st.warning("Please select tone, and enter subject and email_content to generate the email.")

# # Display Generated Email if available
# if generated_email is not None:
#     st.text("Generated Email:")
#     st.text_area(
#         label=" ",  # Provide a non-empty label with a space
#         value=generated_email,
#         height=400,
#         key="email_content",
#         help="This is the generated email content.",
#     )

#     # Copy to Clipboard using JavaScript
#     copy_button_id = "copy-button"
#     copy_button_code = f"""
#     <button id="{copy_button_id}" onclick="copyToClipboard()">Copy to Clipboard</button>
#     <script>
#         function copyToClipboard() {{
#             const emailTextArea = document.querySelector('textarea');
#             emailTextArea.select();
#             document.execCommand('copy');
#             alert('Text copied to clipboard');
#         }}
#     </script>
#     """
#     st.markdown(copy_button_code, unsafe_allow_html=True)

#-------------------------------------------------------------------------------------------------

import streamlit as st
from gpt_utility import call_open_ai_chatcompletion_api, payload_for_api

# Initialize session state to store email history
if "email_history" not in st.session_state:
    st.session_state.email_history = {}

st.markdown(
    """
    <div style="text-align:center; font-size:42px; font-family: 'Times New Roman', Times, serif;">
        <strong>Email Generator</strong>
    </div>
    """,
    unsafe_allow_html=True
)

st.sidebar.title("Choose Email Tone")
tone_options = ["Professional", "Friendly", "Neutral", "Strict to the Point"]
selected_tone = st.sidebar.selectbox("", tone_options, index=0)

# Input for Subject with a placeholder
subject = st.text_input("Enter Email Subject:", placeholder="e.g., Board Meeting Agenda")

# Input for Details with a placeholder
email_content = st.text_area("Add Email Details:", placeholder="e.g., Discuss about revenue, upcoming financial year goals, promotions, rewards, Bonus")

generated_email = None  # Initialize as None

# Generate Email
if st.button("Generate Email"):
    with st.spinner("Generating email..."):
        if selected_tone and subject and email_content:
            # Call the API - 3.5-turbo
            payload = payload_for_api(selected_tone, subject, email_content)
            generated_email = call_open_ai_chatcompletion_api(payload)
            email = f"Subject: {selected_tone}\n\n{subject}\n\n{email_content}"

            # Add the generated email to the session state history
            # st.session_state.email_history.append(generated_email)
            st.session_state.email_history[subject] = generated_email
        else:
            st.warning("Please select tone, and enter subject and email_content to generate the email.")

# Display Generated Email if available
if generated_email is not None:
    st.text("Generated Email:")
    st.text_area(
        label=" ",  # Provide a non-empty label with a space
        value=generated_email,
        height=400,
        key="email_content",
        help="This is the generated email content.",
    )

# Sidebar dropdown to select and display email history
st.sidebar.markdown("## Email History")
selected_email_index = st.sidebar.selectbox("Select Email from History:", options=st.session_state.email_history.keys(), index=len(st.session_state.email_history.keys()) - 1)
print("selected_email_index", selected_email_index)

# Display the selected email from history
if selected_email_index:
    st.text("Selected Email from History:")
    st.text_area(
        label=" ",
        value=st.session_state.email_history[selected_email_index],
        height=200,
        key="selected_email_content",
        help="This is the selected email content from history.",
    )
