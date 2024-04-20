# apps/new_app.py

import pandas as pd
import streamlit as st

st.set_page_config(layout="wide", page_title="India's ONE | Code, Data & License")

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
    st.page_link("pages/03_Data_License.py", label="**Code, Data & License**", use_container_width=True)
with col5:
    st.page_link("pages/99_Funding_and_Support.py", label="**Funding and Support**", use_container_width=True)

st.divider()

st.sidebar.title("Project Repository")
st.sidebar.info(
    """
    [https://github.com/openlandcover/one7types](https://github.com/openlandcover/one7types)
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

st.sidebar.title("[Contact Us](https://forms.gle/r4NiLoEjVRaHoTE48)")

# Function to style header
def style_header(s):
    return ['background-color: grey; color: white; font-weight: bold' for _ in s]

# Function to color cells based on another column's values
def colour_cells(val):
    color = 'black'  # Default text color for better readability
    return f'background-color: {val}; color: {color}'

def app():
    
    st.write("# Source Code")
    st.write("The source code used to produce the maps will be available on our [openlandcover GitHub repository](https://github.com/openlandcover/one7types) when it is ready. The repository contains the code used to train the models, the code used to produce the maps, and the code used to produce the data visualisations. The code is available under the MIT License, which is a permissive open source license. While not required, we would appreciate if you attribute the source if and when you use these data or code.")
    st.write("**Suggested citation:** Koulgi, PS & Madhusudan, MD (2024) Open Land Cover Mapping of India's Semi-arid Open Natural Ecosystems. https://one-india.streamlit.app/")
    
    st.write("## A word on known issues and limitations")
    st.write("""
             Our maps are a work in progress, and as we made them, we have seen many of their limitations. As we endeavour to improve them, we welcome your feedback and suggestions, you can [contact us here](https://forms.gle/r4NiLoEjVRaHoTE48). 
             
             Specifically, as you access and use these maps, here are a few points about the map to be mindful of:
             * These maps largely pertain to the Semi-Arid Lowland regions of India, i.e., areas <= 1,000 m ASL elevation, receiving <= 1200 mm annual rainfall, and may not be directly applicable to other regions. While we have not masked results from areas of higher rainfall, or greater elevations, our labels may not work best in such areas.
             * Much of the imagery used in our input composites come from the period 2019-2021, and are often aggregated over that period. This means that while our maps, on average, capture the pulse of that period, they do not represent a precise slice of time, but more a smear of time extending over those 3 years.
             * Categorising and distinguishing particular land cover types pose both conceptual and practical challenges. Drawing lines at where 'Bare and Sparsely Vegetated Areas' end and where 'Open Savannas' begin, or for that matter, where 'Woodland Savannas' end and 'Forests' begin, are difficult, and to some extent, based on arbitrary thresholds. In nature, these ecosystems/ecotypes seamlessly intergrade, whereas we are constrained to assign them a single label in our map. As a result, our assignments may not always be accurate. To acknowledge this uncertainty, we have made available the entire vector of label probabilities. So, if you find that an area you know to be 'Open Savanna' is labelled 'Agriculture-Low Biomass', please also look at the probability values for both these categories; you may find them to be close to each other. Feel free to use these probability values creatively to incorporate the uncertainty in our maps into your downstream analyses. There are particular pairs of labels where such errors of ommision and commission are more common. They are:
                 * Agriculture-Low Biomass and Open Savannas (especially so in rainfed areas)
                 * Agriculture-High Biomass and Forests/Woodland Savannas (especially crops such as coffee, areca nut, and rubber)
                 * Open Savannas and Shrub Savannas
                 * Woodland Savannas and Forests
             * While we have made every effort to ensure that our labels are as accurate as possible, we are aware that there are many areas where our labels may not be accurate. We are working to improve these labels, and welcome your feedback on how we can do so. You can [contact us here](https://forms.gle/r4NiLoEjVRaHoTE48).
             """)
    
    "&nbsp;"
    
    st.write("# Data Access")
    st.write("The data are publicly available for use on the Google Earth Engine platform as an image raster at `projects/ee-open-natural-ecosystems/assets/publish/onesWith7Classes/landcover_hier`, from where they may be used directly in further analyses, or select bands can be downloaded for specific areas of interest, as required. Metadata pertaining to this dataset are presented below.")
    st.write("To help you get started, here is a Google Earth Engine [starter script](https://code.earthengine.google.co.in/02585ca79a284e0be81441c24f8653a7) to load and visualise the data. (Note: Google Earth Engine account needed to run this script)")
    
    band_names = pd.read_excel("./band_data.xlsx", sheet_name="bandData")
    band_names_styled = band_names.style.apply(style_header, axis=1)
    st.write("## Summary of Bands in the Dataset")
    st.dataframe(band_names_styled, height = 670, use_container_width=True, hide_index=True)
    "&nbsp;"
   
    # l1_label_num = pd.read_excel("./band_data.xlsx", sheet_name="l1LabelNum")
    l1_label_num = pd.read_excel("./band_data.xlsx", sheet_name="l1LabelNum", usecols=["Value", "Label"])
    l1_label_num_styled = l1_label_num.style.apply(style_header, axis=1)
    # l1_label_num_styled = l1_label_num.style.applymap(colour_cells, subset=['CSS_Colour'])
    st.write("## Band Values")
    st.write("Band: `l1LabelNum` | Level 1 Labels Numeric")
    st.dataframe(l1_label_num_styled, use_container_width=False, hide_index=True)
    "&nbsp;"
    
    # l2_label_num = pd.read_excel("./band_data.xlsx", sheet_name="l2LabelNum")
    l2_label_num = pd.read_excel("./band_data.xlsx", sheet_name="l2LabelNum", usecols=["Value", "Label"])
    l2_label_num_styled = l2_label_num.style.apply(style_header, axis=1)
    st.write("Band: `l2LabelNum` | Level 2 Labels Numeric")
    st.dataframe(l2_label_num_styled, height = 460, width = 550,
            column_config={"Label": st.column_config.Column(label="Label", width="large")}, 
            hide_index=True)

app()