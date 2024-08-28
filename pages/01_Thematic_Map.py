# apps/new_app.py

import streamlit as st
import ee
import geemap.foliumap as geemap
import matplotlib

st.set_page_config(layout="wide", page_title="India's ONE | Thematic Map")

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

def app():
    st.title("Thematic Map of Open Natural Ecosystems", anchor = "landcovers-thematic")

    with st.expander("**See a brief description of the types of ONE**"):
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

    m = geemap.Map(center=(21, 79), zoom=5.2, control_scale=True)

    mapRaster = ee.Image("projects/ee-open-natural-ecosystems/assets/publish/onesWith7Classes/landcover_hier")
    l2Labels = mapRaster.select("l2LabelNum") \
        .remap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
               [1, 1, 6, 1, 3, 2, 4, 5, 7,  8,  9,  1])
    l1Labels = mapRaster.select("l1LabelNum") \
        .remap([200, 100], [1, 0])

    oneTypeslegendDict = {  "Others": matplotlib.colors.cnames["black"],
                            "Forest": matplotlib.colors.cnames["darkgreen"],
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
        "max": 9,
        "palette": list(oneTypeslegendDict.values()),
    }
    onelegendDict = {"Non-ONE": "#1a2b2b",
                         "ONE": matplotlib.colors.cnames["navajowhite"]}
    one_vis_params = {
        "min": 0,
        "max": 1,
        "palette": list(onelegendDict.values()),
    }
    
    m.add_basemap("SATELLITE")
    # left_layer = geemap.ee_tile_layer(l1Labels, one_vis_params, name = "ONE")
    # right_layer = geemap.ee_tile_layer(l2Labels, oneTypes_vis_params, name = "Types of ONE")
    # m.split_map(left_layer, right_layer)
    # m.add_legend(title = "ONE types", legend_dict = oneTypeslegendDict, draggable = False)
    # m.add_legend(title = "ONE", legend_dict = onelegendDict, position = "bottomleft", draggable = False)
    m.addLayer(l2Labels, oneTypes_vis_params, "ONE")
    m.add_legend(title = "ONE types", legend_dict = oneTypeslegendDict, draggable = False)

    m.to_streamlit(height = 768)

app()