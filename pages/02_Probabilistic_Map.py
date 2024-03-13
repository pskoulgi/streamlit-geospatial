# apps/new_app.py

import streamlit as st
import ee
import geemap.foliumap as geemap
import matplotlib

st.set_page_config(layout="wide")

st.sidebar.markdown(
    """
    India is endowed with a diversity of terrestrial biomes. Barring
    forests—areas of closed tree canopies—they comprise diverse
    naturally open and often treeless habitats that support their own
    rich and unique complement of plant and animal life. Further,
    for centuries, such diversity has thrived alongside unique pastoral
    and agro-pastoral communities that have shared space with nature
    in this biome, while deriving identity, sustenance and livelihood from it.

    Together, these Open Natural Ecosystems stretch across a vast
    area comprising some 15% of the land area in India's semi-arid zone.
    The threats they face are vast too. Not only are they
    disregarded for their unique ecological, cultural and livelihood values,
    but they are also targets of huge government schemes and programmes for
    well-intentioned developmental purposes that lead to serious
    unintended negative consequences.

    A previous effort to map the extent of these ONEs can be seen
    [here](https://mdm.users.earthengine.app/view/open-natural-ecosystems),
    with its methods and data freely and publicly accessible
    in this [preprint](https://www.essoar.org/doi/10.1002/essoar.10507612.1).
"""
)

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