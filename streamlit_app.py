import streamlit as st

# Alphabet list
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Caesar cipher function
def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    return output_text

# Streamlit app
st.title("Caesar Cipher App")
st.write("Encrypt or decrypt a message using the Caesar cipher.")

# User input
st.subheader("Enter your inputs:")
direction = st.radio("Choose an action:", ["encode", "decode"])
text = st.text_area("Enter your message:", placeholder="Type your message here...")
shift = st.number_input("Enter the shift number:", min_value=0, step=1, value=0)

# Button to execute the Caesar cipher
if st.button("Submit"):
    if not text.strip():
        st.warning("Please enter a message to process.")
    else:
        result = caesar(text.lower(), shift, direction)
        st.success(f"The {direction}d result is: {result}")
