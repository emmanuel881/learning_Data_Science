import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup

#select topic
tag = st.selectbox('Choose a topic',["love", "life", "humor", "books"])

#generate CSV file button
genarate = st.button("generate CSV")

#url to the topic
url = f"https://quotes.toscrape.com/tag/{tag}/"

#using request to access the site
res = requests.get(url)
#get content of response
content = BeautifulSoup(res.content, 'html.parser')

#get page source code
#st.code(content)
#select the page content we want to extract
quotes = content.find_all('div', class_='quote')

qoute_file = []

#will loop through the content in qoutes
for qoute in quotes:
    #capture the specifics into variables 
    text = qoute.find('span', class_='text').text 
    author = qoute.find('small', class_='author').text 
    link = qoute.find('a')
    st.markdown(f"<a href=https://quotes.toscrape.com{link['href']}>{author}</a>", unsafe_allow_html=True)
    st.code(f"https://quotes.toscrape.com{link['href']}")
    st.success(text)
    qoute_file.append([text, author, link])
if genarate:
    try:
        df = pd.DataFrame(quote_file)
        df.to_csv("quote.csv", index=False, header=['qoute', 'Author', 'Link'])
    except:
        st.write("loading.....")