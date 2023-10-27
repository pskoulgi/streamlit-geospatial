# apps/new_app.py

import streamlit as st
import ee
import geemap.foliumap as geemap
import matplotlib

st.set_page_config(layout="wide")

st.sidebar.warning("⚠ ️️︎This is a **PRE-RELEASE ALPHA VERSION** of the map. Its final version will be made public shortly. ⚠")
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
st.sidebar.header("Funding and support")
st.sidebar.markdown(
    """
    Financial support for various aspects of this mapping work came from
    [Azim Premji University](https://azimpremjiuniversity.edu.in/)
    as part of the Research Funding Programme 2020,
    and from the [National Centre for Biological Sciences](https://www.ncbs.res.in/),
    its [Archives](https://archives.ncbs.res.in/),
    the Nadathur Foundation, [TNQ Technologies](https://www.tnq.co.in/csr-activities/)
    and [ATREE](https://www.atree.org/).

    This work would not have been possible without the generosity of efforts behind
    many free, public and open source scientific computation resources and software tools,
    chief among them being [{geemap}](https://geemap.org/),
    [Spatial Thoughts](https://spatialthoughts.com/) and [QGIS](https://qgis.org/).
    These analyses were carried out on the [Google Earth Engine](https://earthengine.google.com/)
    cloud computing platform.
"""
)

def app():
    st.title("Open Natural Ecosystems & Their LandCover Types", anchor = "onelandcovers")

    with st.expander("See a brief description of the landcover types"):
        col11, col12 = st.columns([1, 4])
        col11.markdown("**_Others_**")
        col12.markdown("""
            Forests, tree plantations, agricultural areas, built-up areas,
            open water and wetlands.""")
        col21, col22 = st.columns([1, 4])
        col21.markdown("**_Dune_**")
        col22.markdown("""
            Areas where the soil substrate is predominantly sandy,
            with the vegetation being mostly short-statured, sparsely distributed
            and occurring in clumps.""")
        col31, col32 = st.columns([1, 4])
        col31.markdown("**_Ravine_**")
        col32.markdown("""
            Areas with deep gullies following substrate erosion patterns.
            Tree cover is sparse, if at all, and ground vegetation is
            shrub- and grass-dominated.""")
        col41, col42 = st.columns([1, 4])
        col41.markdown("**_Saline_**")
        col42.markdown("""
            Salt marshes of The Rann of Kutchch.""")
        col51, col52 = st.columns([1, 4])
        col51.markdown("**_Bare or sparsely vegetated_**")
        col52.markdown("""
            Areas with no trees and little or no ground vegetation.
            Ground vegetation, if it occurs, is sparsely distributed.""")
        # col2.markdown(<div style="text-align: right"> Forest, agriculture, built </div>)
        col61, col62 = st.columns([1, 4])
        col61.markdown("**_Open Savanna_**")
        col62.markdown("""
            Areas with grasses and shrubs in the understorey and trees above.
            Tree cover is very sparse.""")
        col71, col72 = st.columns([1, 4])
        col71.markdown("**_Shrub Savanna_**")
        col72.markdown("""
            Areas with grasses and shrubs in the understorey and trees above.
            Tree cover is sparse. Understorey can include short-statured
            woody vegetation.""")
        col81, col82 = st.columns([1, 4])
        col81.markdown("**_Woodland Savanna_**")
        col82.markdown("""
            Areas with grasses and shrubs in the understorey and trees above.
            Tree cover is moderate. Large openings in the tree canopy cover remain,
            and the understorey is predominantly grasses.""")

    m = geemap.Map(center=[21, 79], zoom=5.2)

    oneLabelsCollapsedForViz = ee.Image("projects/ee-open-natural-ecosystems/assets/publish/onesWith7Classes/labelWithUncertAppliedONEStates")
    top1NonONEsCollapsed = oneLabelsCollapsedForViz

    legendDict = {          "Others": matplotlib.colors.cnames["black"],
                              "Dune": matplotlib.colors.cnames["khaki"],
                            "Ravine": matplotlib.colors.cnames["fuchsia"],
                            "Saline": matplotlib.colors.cnames["lightsteelblue"],
        "Bare or sparsely vegetated": matplotlib.colors.cnames["beige"],
                      "Open Savanna": matplotlib.colors.cnames["yellow"],
                     "Shrub Savanna": matplotlib.colors.cnames["goldenrod"],
                  "Woodland Savanna": matplotlib.colors.cnames["greenyellow"]
    }

    vis_params = {
        "min": 1,
        "max": 8,
        "palette": list(legendDict.values()),
    }

    m.add_basemap("SATELLITE")
    m.addLayer(top1NonONEsCollapsed, vis_params, "ONE LandCover Types", True, 1)
    m.add_legend(title = "Landcover types", legend_dict = legendDict)

    m.to_streamlit(height = 768)

app()