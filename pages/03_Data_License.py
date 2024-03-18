# apps/new_app.py

import pandas as pd
import streamlit as st

st.set_page_config(layout="wide", page_title="India's ONE | Data and License")

# I think the sectionb below may be better done with st_tabs
# https://docs.streamlit.io/library/api-reference/layout/st.tabs

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.page_link("app.py", label="Home", icon="🏠", use_container_width=True)
with col2:
    st.page_link("pages/01_Thematic_Map.py", label="**Thematic Map**", use_container_width=True)
with col3:
    st.page_link("pages/02_Probabilistic_Map.py", label="**Probabilistic Map**", use_container_width=True)
with col4:
    st.page_link("pages/03_Data_License.py", label="**Data and License**", use_container_width=True)
with col5:
    st.page_link("pages/99_Funding_and_Support.py", label="**Funding and Support**", use_container_width=True)

st.divider()

st.sidebar.title("Project Repository")
st.sidebar.info(
    """
    [https://github.com/openlandcover/](https://github.com/openlandcover/)
    """
)

# st.sidebar.title("Contact")
# st.sidebar.info(
#     """
#     """
# )

st.sidebar.title("Terms of Use")
st.sidebar.markdown(
    """
    This map data and analysis code are available for free and open public use, under [MIT License](https://mit-license.org/).
    """
)


# Function to style header
def style_header(s):
    return ['background-color: grey; color: white; font-weight: bold' for _ in s]

# Function to color cells based on another column's values
def colour_cells(val):
    color = 'black'  # Default text color for better readability
    return f'background-color: {val}; color: {color}'


def app():
    
    st.write("# Data Access")
    st.write("The data are publicly available for use on the Google Earth Engine platform at `projects/ee-open-natural-ecosystems/assets/publish/onesWith7Classes/landcover_hier`, from where they may be used directly in further analyses, or select bands can be downloaded for specific areas of interest, as required. Metadata pertaining to this dataset are presented below.")
    st.write("To help you get started, here is a Google Earth Engine [starter script](https://code.earthengine.google.co.in/02585ca79a284e0be81441c24f8653a7) to load and visualise the data. (Note: Google Earth Engine account needed to run this script)")
    
    band_names = pd.read_excel("./band_data.xlsx", sheet_name="bandData")
    band_names_styled = band_names.style.apply(style_header, axis=1)
    st.write("## Summary of Bands in the Dataset")
    st.dataframe(band_names_styled, height = 670, use_container_width=True, hide_index=True)

   
    l1_label_num = pd.read_excel("./band_data.xlsx", sheet_name="l1LabelNum")
    l1_label_num_styled = l1_label_num.style.applymap(colour_cells, subset=['CSS_Colour'])
    st.write("## Band Values")
    st.write("BAND: l1LabelNum | Level 1 Labels Numeric")
    st.dataframe(l1_label_num_styled, width=800, use_container_width=True, hide_index=True)


    l2_label_num = pd.read_excel("./band_data.xlsx", sheet_name="l2LabelNum")
    l2_label_num_styled = l2_label_num.style.applymap(colour_cells, subset=['CSS_Colour'])
    st.write("BAND: l2LabelNum | Level 2 Labels Numeric")
    st.dataframe(l2_label_num_styled, height = 460, width=800, use_container_width=True, hide_index=True)

    st.write("## Data & Code License")
    st.write("All map data and analysis code are available freely for open public use, under [MIT License](https://mit-license.org/). While not required, we would appreciate if you attribute the source. Suggested citation:???")   
    
app()