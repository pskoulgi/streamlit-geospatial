# apps/new_app.py

import streamlit as st
import ee
import geemap.foliumap as geemap
import matplotlib

def app():
    st.title("Open Natural Ecosystems & Their LandCover Types", anchor = "onelandcovers")
    st.warning("⚠ ️️︎This is a **PRE-RELEASE ALPHA VERSION** of the map. Its final version will be made public shortly. ⚠")

    m = geemap.Map(location=(21, 79), zoom=5.2)
    one = ee.Image(
        "projects/ee-open-natural-ecosystems/assets/finalSprint/globalModelGbtBiomeZonesOhe/prediction"
    )

    india = ee.FeatureCollection("users/mdm/india_soiBoundary")
    top1 = one.select("top1LabelNum").clipToCollection(india)

    legendDict = {
        "Agriculture (high biomass)": matplotlib.colors.cnames["black"],
         "Agriculture (low biomass)": matplotlib.colors.cnames["black"],
                              "Bare": matplotlib.colors.cnames["beige"],
                             "Built": matplotlib.colors.cnames["black"],
                              "Dune": matplotlib.colors.cnames["khaki"],
                            "Forest": matplotlib.colors.cnames["black"],
                            "Ravine": matplotlib.colors.cnames["fuchsia"],
                            "Saline": matplotlib.colors.cnames["lightsteelblue"],
                    "Savanna (open)": matplotlib.colors.cnames["yellow"],
                   "Savanna (shrub)": matplotlib.colors.cnames["goldenrod"],
                "Savanna (woodland)": matplotlib.colors.cnames["greenyellow"],
                  "Water or wetland": matplotlib.colors.cnames["black"]
    }

    vis_params = {
        "min": 1,
        "max": 12,
        "palette": list(legendDict.values()),
    }

    m.add_basemap("SATELLITE")
    m.addLayer(top1, vis_params, "ONE LandCover Types", True, 1)
    m.add_legend(legend_title = "Landcover types", legend_dict = legendDict)

    m.to_streamlit(height = 768)
