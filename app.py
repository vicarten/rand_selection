import time

import streamlit as st

from rand_selection.selector import random_selection

st.set_page_config(page_title="Random Picker")

st.session_state.setdefault("names", [])
st.session_state.setdefault("questions", [])
st.session_state.setdefault("used_names", set())
st.session_state.setdefault("result", None)

st.title("Random Name & Question Picker")

add_name_col, add_question_col = st.columns(2)

with add_name_col:
    with st.form("add_name_form", clear_on_submit=True):
        new_name = st.text_input("Add a name")
        if st.form_submit_button("Add name") and new_name.strip():
            st.session_state.names.append(new_name.strip())

with add_question_col:
    with st.form("add_question_form", clear_on_submit=True):
        new_question = st.text_input("Add a question")
        if st.form_submit_button("Add question") and new_question.strip():
            st.session_state.questions.append(new_question.strip())

names_col, questions_col = st.columns(2)

with names_col:
    st.subheader("Names")
    if st.session_state.names:
        for i, name in enumerate(st.session_state.names, start=1):
            used_tag = " (used)" if name in st.session_state.used_names else ""
            st.write(f"{i}. {name}{used_tag}")
    else:
        st.write("No names added yet.")

with questions_col:
    st.subheader("Questions")
    if st.session_state.questions:
        for i, question in enumerate(st.session_state.questions, start=1):
            st.write(f"{i}. {question}")
    else:
        st.write("No questions added yet.")

no_repeats = st.checkbox("No repeats (names)")

eligible_names = (
    [n for n in st.session_state.names if n not in st.session_state.used_names]
    if no_repeats
    else st.session_state.names
)

draw_disabled = not eligible_names or not st.session_state.questions

draw_clicked = st.button("Draw", disabled=draw_disabled)

result_placeholder = st.empty()

if draw_clicked:
    for _ in range(18):
        flash_name, flash_question = random_selection(
            st.session_state.names, st.session_state.questions
        )
        result_placeholder.markdown(f"### {flash_name} — {flash_question}")
        time.sleep(0.15)

    chosen_name, chosen_question = random_selection(eligible_names, st.session_state.questions)
    st.session_state.used_names.add(chosen_name)
    st.session_state.result = (chosen_name, chosen_question)

if st.session_state.result:
    chosen_name, chosen_question = st.session_state.result
    result_placeholder.markdown(f"## 🎉 {chosen_name} — {chosen_question}")

if draw_disabled and st.session_state.names and st.session_state.questions:
    st.info("All names have been used. Uncheck \"No repeats\" or add a new name to draw again.")
