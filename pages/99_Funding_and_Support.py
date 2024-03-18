# apps/new_app.py

import streamlit as st
import ee
import geemap.foliumap as geemap
import matplotlib

st.set_page_config(layout="wide", page_title="India's ONE | Support")

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

def app():
    st.title("Funding and support")

    """
    Financial support for various aspects of this mapping work came from:
    * [Azim Premji University](https://azimpremjiuniversity.edu.in/) as part of the Research Funding Programme 2020
    * [National Centre for Biological Sciences (NCBS)](https://www.ncbs.res.in/)
    * [Archives at NCBS](https://archives.ncbs.res.in/)
    * Nadathur Foundation
    * [TNQ Technologies](https://www.tnq.co.in/csr-activities/)
    * [ATREE](https://www.atree.org/)
    * [The Habitats Trust](https://www.thehabitatstrust.org/)
    * [Nature Conservation Foundation](https://www.ncf-india.org/) provided technical and logistical support

    This work would not have been possible without the generosity of efforts behind
    many free, public and open source scientific computation resources and software tools,
    chief among them being:
    * [{geemap}](https://geemap.org/)
    * [Spatial Thoughts](https://spatialthoughts.com/)
    * [QGIS](https://qgis.org/)
    * [awesome-gee-community-catalog](https://gee-community-catalog.org/)
    
    These analyses were carried out on the [Google Earth Engine](https://earthengine.google.com/)
    cloud computing platform.
    """
    
app()