# apps/new_app.py

import streamlit as st
import ee
import geemap.foliumap as geemap
import matplotlib

def app():
    st.title("Open Natural Ecosystems & Their LandCover Types", anchor = "onelandcovers")

    m = geemap.Map(location=(21, 79), zoom=5.2)

    oneLabelsCollapsedForViz = ee.Image("projects/ee-open-natural-ecosystems/assets/publish/onesWith7Classes/labelAndUncert")
    top1NonONEsCollapsed = oneLabelsCollapsedForViz.select("top1NonONECollapsed")
    oneProb = oneLabelsCollapsedForViz.select("oneProb")

    indiaStates = ee.FeatureCollection("users/mdm/india_soiStates")
    oneStates = indiaStates.filter(
        ee.Filter.inList(
            'state',
            ['KARNATAKA', 'KERALA', 'TAMIL NADU', 'ANDHRA PRADESH', 'TELANGANA',
             'MAHARASHTRA', 'MADHYA PRADESH', 'CHHATTISGARH', 'ODISHA', 'JHARKHAND',
             'BIHAR', 'UTTAR PRADESH', 'DELHI', 'PUNJAB', 'HARYANA', 'RAJASTHAN',
             'GUJARAT', 'GOA'])
        ).map(lambda f: f.simplify(1000)) \
        .geometry(1000)

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
    m.addLayer(top1NonONEsCollapsed.updateMask(oneProb).clip(oneStates), vis_params, "ONE LandCover Types", True, 1)
    m.add_legend(legend_title = "Landcover types", legend_dict = legendDict)

    m.to_streamlit(height = 768)
