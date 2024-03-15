# apps/new_app.py

import streamlit as st
import ee
import geemap.foliumap as geemap
import matplotlib

st.set_page_config(layout="wide", page_title="India's ONE | Probabilistic Map")

st.sidebar.title("GitHub")
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

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.page_link("app.py", label="Home", icon="🏠", use_container_width=True)
with col2:
    st.page_link("pages/01_Thematic_Map.py", label="**Thematic Map**", use_container_width=True)
with col3:
    st.page_link("pages/02_Probabilistic_Map.py", label="**Probabilistic Map**", use_container_width=True)
with col4:
    st.page_link("pages/99_Funding_and_Support.py", label="**Funding and Support**", use_container_width=True)

st.divider()

def app():
    st.title("Probabilistic Map of Open Natural Ecosystems", anchor = "onelandcovers")

    m = geemap.Map(center=(21, 79), zoom=5.2)

    mapRaster = ee.Image("projects/ee-open-natural-ecosystems/assets/homeStretch2023/globalModelGbt_readjLabels2024R2_CpyHtPlsScnsIncl_BiomeZonesOhe_hier/prediction_expHierMult")
    l2OneProbs = mapRaster.select(["prob_one_.*"]).divide(1e4)
    l2NononeProbs = mapRaster.select(["prob_nonone_.*"]).divide(1e4)
    l1Probs = mapRaster.select(["prob_one", "prob_nonone"]).divide(1e4)

    oneProb = l2OneProbs.reduce(ee.Reducer.sum()).rename("one")
    agrProb = l2NononeProbs.select(["prob_nonone_agri_.*"]).reduce(ee.Reducer.sum()).rename("agr")
    othProb = l2NononeProbs.select("prob_nonone_forest").rename("oth")
    oneAgrOthRgb = ee.Image.cat([agrProb, oneProb, othProb])

    m.add_basemap("SATELLITE")
    left_layer = geemap.ee_tile_layer(l1Probs, {"bands": ["prob_one"], "min": 0, "max": 1}, name = "ONE")
    right_layer = geemap.ee_tile_layer(oneAgrOthRgb, {"min": 0, "max": 1}, name = "ONE-Agri-For probabilities")
    m.split_map(left_layer, right_layer)

    m.to_streamlit(height = 768)

app()