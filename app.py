if amount is not None:
    st.write(f"The exercise input was {amount}.")

# NEW MARKOV TEXT DEMO FOR ASSIGNMENT
user_text = st.text_area("Enter corpus text:", "")
seed = st.text_input("Optional seed word:", "")
count = st.number_input("Number of terms to generate:", value=15, step=1)

if st.button("Generate Text"):
    if len(user_text.strip()) == 0:
        st.write("Please enter a corpus.")
    else:
        mt = MarkovText(user_text)
        try:
            generated = mt.generate(seed_term=seed if seed != "" else None,
                                    term_count=count)
            st.write("### Generated Text:")
            st.write(generated)
        except Exception as e:
            st.write(f"Error: {e}")

