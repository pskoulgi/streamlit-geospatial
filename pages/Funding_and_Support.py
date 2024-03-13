# apps/new_app.py

import streamlit as st
import ee
import geemap.foliumap as geemap
import matplotlib

st.set_page_config(layout="wide")

def app():
    st.title("Funding and support")

    """
    Financial support for various aspects of this mapping work came from
    [Azim Premji University](https://azimpremjiuniversity.edu.in/)
    as part of the Research Funding Programme 2020,
    and from the [National Centre for Biological Sciences](https://www.ncbs.res.in/),
    its [Archives](https://archives.ncbs.res.in/),
    the Nadathur Foundation, [TNQ Technologies](https://www.tnq.co.in/csr-activities/),
    [ATREE](https://www.atree.org/) and [The Habitats Trust](https://www.thehabitatstrust.org/).

    This work would not have been possible without the generosity of efforts behind
    many free, public and open source scientific computation resources and software tools,
    chief among them being [{geemap}](https://geemap.org/),
    [Spatial Thoughts](https://spatialthoughts.com/), [QGIS](https://qgis.org/)
    and [awesome-gee-community-catalog](https://gee-community-catalog.org/).
    These analyses were carried out on the [Google Earth Engine](https://earthengine.google.com/)
    cloud computing platform.
    """
    
app()