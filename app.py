<<<<<<< HEAD
import streamlit as st
import psycopg2
import pandas as pd

st.title("📦 Dynamic Inventory Dashboard")

conn = psycopg2.connect(
    host='localhost',
    port=5432,
    database='retail',
    user='postgres',
    password='password'
)

query = """
SELECT 
    store_id,
    product_id,
    event,
    COUNT(*) as count
FROM 
    customer_events
GROUP BY 
    store_id, product_id, event
ORDER BY 
    store_id, product_id;
"""

df = pd.read_sql_query(query, conn)
st.dataframe(df)
=======
import streamlit as st
import psycopg2
import pandas as pd

st.title("📦 Dynamic Inventory Dashboard")

conn = psycopg2.connect(
    host='localhost',
    port=5432,
    database='retail',
    user='postgres',
    password='password'
)

query = """
SELECT 
    store_id,
    product_id,
    event,
    COUNT(*) as count
FROM 
    customer_events
GROUP BY 
    store_id, product_id, event
ORDER BY 
    store_id, product_id;
"""

df = pd.read_sql_query(query, conn)
st.dataframe(df)
>>>>>>> 4aff65779de5bd6fbcb8133cc71e606221b3fe13
