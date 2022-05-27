# apps/new_app.py

import streamlit as st
import ee
import geemap.foliumap as geemap
import matplotlib

def app():
    st.title("Open Natural Ecosystems & Their LandCover Types", anchor = "onelandcovers")

    with st.expander("See a brief description of the landcover types"):
        col11, col12 = st.columns([1, 4])
        col11.markdown("**_Others_**")
        col12.markdown("Forests, tree plantations, agricultural areas, built-up areas, open water and wetlands")
        col51, col52 = st.columns([1, 4])
        col51.markdown("**_Dune_**")
        col52.markdown("Areas where the soil substrate is predominantly sandy, with the vegetation being mostly short-statured, sparsely distributed and occurring in clumps.")
        col61, col62 = st.columns([1, 4])
        col61.markdown("**_Ravine_**")
        col62.markdown("Areas with deep gullies following substrate erosion patterns. Tree cover is sparse, if at all, and ground vegetation is shrub- and grass-dominated.")
        col81, col82 = st.columns([1, 4])
        col81.markdown("**_Saline_**")
        col82.markdown("Salt marshes of The Rann of Kutchch.")
        col71, col72 = st.columns([1, 4])
        col71.markdown("**_Bare or sparsely vegetated_**")
        col72.markdown("Areas with no trees and little or no ground vegetation. Ground vegetation, if it occurs, is sparsely distributed.")
        # col2.markdown(<div style="text-align: right"> Forest, agriculture, built </div>)
        col21, col22 = st.columns([1, 4])
        col21.markdown("**_Open Savanna_**")
        col22.markdown("Areas with grasses and shrubs in the understorey and trees above. Tree cover is very sparse.")
        col31, col32 = st.columns([1, 4])
        col31.markdown("**_Shrub Savanna_**")
        col32.markdown("Areas with grasses and shrubs in the understorey and trees above. Tree cover is sparse. Understorey can include short-statured woody vegetation.")
        col41, col42 = st.columns([1, 4])
        col41.markdown("**_Woodland Savanna_**")
        col42.markdown("Areas with grasses and shrubs in the understorey and trees above. Tree cover is moderate. Large openings in the tree canopy cover remain, and the understorey is predominantly grasses.")

    m = geemap.Map(location=(21, 79), zoom=5.2)

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
    m.add_legend(legend_title = "Landcover types", legend_dict = legendDict)

    m.to_streamlit(height = 768)
