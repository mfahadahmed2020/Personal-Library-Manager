import streamlit as st
import pandas as pd

novels = {
    "Colonel Faridi Series": {
        "Read": [
            {"Title": "Tarantula", "Year": 1981,"First Author": "Ibne Safi"},
            {"Title": "Dog Race", "Year": 1982,"First Author": "Ibne Safi"},
            {"Title": "Pressure Lock", "Year": 1984,"First Author": "Ibne Safi"},
            {"Title": "Black Collar", "Year": 1986,"First Author": "Ibne Safi"},
            {"Title": "Diamond of Death", "Year": 1987,"First Author": "Ibne Safi"},
            {"Title": "Shalmaq", "Year": 1990,"First Author": "Ibne Safi"},
            {"Title": "Dark Club", "Year": 1992,"First Author": "Ibne Safi"},
            {"Title": "Halka-e-Maut", "Year": 1993,"First Author": "Ibne Safi"},
            {"Title": "Way to Action", "Year": 1994,"First Author": "Ibne Safi"},
            {"Title": "Top Target", "Year": 1997,"First Author": "Ibne Safi"},
        ],
        "Unread": []
    },
"Imran Series": {
        "Read": [],
        "Unread": [
            {"Title": "Big Target", "Year": 2019,"Second Author": "Mazhar Kaleem M.A"},
            {"Title": "Master Mission", "Year": 2018,"Second Author": "Mazhar Kaleem M.A"},
            {"Title": "Special Force", "Year": 2017,"Second Author": "Mazhar Kaleem M.A"},
            {"Title": "Final Game", "Year": 2017,"Second Author": "Mazhar Kaleem M.A"},
            {"Title": "Scarm", "Year": 2017,"Second Author": "Mazhar Kaleem M.A"},
            {"Title": "Cyril", "Year": 2017,"Second Author": "Mazhar Kaleem M.A"},
            {"Title": "Dark Heart", "Year": 2017,"Second Author": "Mazhar Kaleem M.A"},
            {"Title": "Double Dodge", "Year": 2016,"Second Author": "Mazhar Kaleem M.A"},
            {"Title": "Spargon", "Year": 2016,"Second Author": "Mazhar Kaleem M.A"},
            {"Title": "Last of Black Thunder Headquarters", "Year": 2028,"Second Author": "Mazhar Kaleem M.A"},
        ]
    }
}


st.title("📚 Personal Library Manager")


st.header("📖 Imran Series (Unread Books)")
unread_imran = pd.DataFrame(novels["Imran Series"]["Unread"])
st.write(unread_imran)


with st.form(key="add_book_form"):
    book_title = st.text_input("Book Title")
    series_choice = st.selectbox("Series", ["Colonel Faridi Series", "Imran Series"])
    book_status = st.radio("Status", ["Read", "Unread"])
    year_read = st.number_input("Year of Book Read", min_value=1900, max_value=2028)
    author_name = st.text_input("Author Name")  

    submit_button = st.form_submit_button(label="Add Book")

    if submit_button:
        
        if "Read" not in novels[series_choice]:
            novels[series_choice]["Read"] = []
        if "Unread" not in novels[series_choice]:
            novels[series_choice]["Unread"] = []


        new_book = {"Title": book_title, "Year": year_read, "Author": author_name}

        if book_status == "Read":
            novels[series_choice]["Read"].append(new_book)
        else:
            novels[series_choice]["Unread"].append(new_book)

        st.success(f"Book '{book_title}' by {author_name} added successfully!")
        # st.experimental_rerun()


st.subheader("📚 Books in Library")
read_f_faridi_updated = pd.DataFrame(novels["Colonel Faridi Series"]["Read"])
unread_imran_updated = pd.DataFrame(novels["Imran Series"]["Unread"])

st.write("### Colonel Faridi Series (Read)")
st.write(read_f_faridi_updated)

st.write("### Imran Series (Unread)")
st.write(unread_imran_updated)