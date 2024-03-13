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
    st.title("Thematic Map of Open Natural Ecosystems", anchor = "onelandcovers")

    with st.expander("See a brief description of the types of ONE"):
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

    m = geemap.Map(center=(21, 79), zoom=5.2)

    mapRaster = ee.Image("projects/ee-open-natural-ecosystems/assets/homeStretch2023/globalModelGbt_readjLabels2024R2_CpyHtPlsScnsIncl_BiomeZonesOhe_hier/prediction_expHierMult")
    l2Labels = mapRaster.select("l2LabelNum") \
        .remap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
               [1, 1, 5, 1, 2, 1, 3, 4, 6,  7,  8,  1])
    l1Labels = mapRaster.select("l1LabelNum") \
        .remap([200, 100], [1, 0])

    oneTypeslegendDict = {  "Others": matplotlib.colors.cnames["black"],
                              "Dune": matplotlib.colors.cnames["khaki"],
                            "Ravine": matplotlib.colors.cnames["fuchsia"],
                            "Saline": matplotlib.colors.cnames["lightsteelblue"],
        "Bare or sparsely vegetated": matplotlib.colors.cnames["beige"],
                      "Open Savanna": matplotlib.colors.cnames["yellow"],
                     "Shrub Savanna": matplotlib.colors.cnames["goldenrod"],
                  "Woodland Savanna": matplotlib.colors.cnames["greenyellow"]
    }
    oneTypes_vis_params = {
        "min": 1,
        "max": 8,
        "palette": list(oneTypeslegendDict.values()),
    }
    onelegendDict = {"Non-ONE": matplotlib.colors.cnames["black"],
                         "ONE": matplotlib.colors.cnames["white"]}
    one_vis_params = {
        "min": 0,
        "max": 1,
        "palette": list(onelegendDict.values()),
    }
    
    m.add_basemap("SATELLITE")
    left_layer = geemap.ee_tile_layer(l1Labels, one_vis_params, name = "ONE")
    right_layer = geemap.ee_tile_layer(l2Labels, oneTypes_vis_params, name = "Types of ONE")
    m.split_map(left_layer, right_layer)
    m.add_legend(title = "ONE types", legend_dict = oneTypeslegendDict)
    m.add_legend(title = "ONE", legend_dict = onelegendDict, position = "bottomleft")

    m.to_streamlit(height = 768)

app()