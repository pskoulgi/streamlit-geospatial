# apps/new_app.py

import streamlit as st
import ee
import geemap.foliumap as geemap
import matplotlib

def app():
    st.title("Open Natural Ecosystem LandCover Types")

    m = geemap.Map(location=(21, 79), zoom=4.2)
    one = ee.Image(
        "projects/ee-open-natural-ecosystems/assets/finalSprint/globalModelGbtBiomeZonesOhe/prediction"
    )

    india = ee.FeatureCollection("users/mdm/india_soiBoundary")
    top1 = one.select("top1LabelNum").clipToCollection(india)

    legendDict = {
          "agri_hiBioMass": matplotlib.colors.cnames["darkviolet"],
          "agri_loBiomass": matplotlib.colors.cnames["violet"],
                    "bare": matplotlib.colors.cnames["beige"],
                   "built": matplotlib.colors.cnames["red"],
                    "dune": matplotlib.colors.cnames["khaki"],
                  "forest": matplotlib.colors.cnames["darkgreen"],
                  "ravine": matplotlib.colors.cnames["fuchsia"],
                  "saline": matplotlib.colors.cnames["lightsteelblue"],
            "savanna_open": matplotlib.colors.cnames["yellow"],
           "savanna_shrub": matplotlib.colors.cnames["orange"],
        "savanna_woodland": matplotlib.colors.cnames["lightgreen"],
           "water_wetland": matplotlib.colors.cnames["blue"]
    }

    vis_params = {
        "min": 1,
        "max": 12,
        "palette": list(legendDict.values()),
    }

    m.addLayer(top1, vis_params, "ONE LandCover Types", True, 1)
    m.add_legend(legend_title = "Legend", legend_dict = legendDict)

    m.to_streamlit()
