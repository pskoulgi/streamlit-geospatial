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
    top1 = one.select("top1LabelNum")
    top1OrigLabels = [i for i in range(1, 13)]
    top1RemappedLabels = [8, 8, 1, 8, 2, 8, 3, 4, 5, 6, 7,  8]
    # top1RemappedLabels = [1, 1, 3, 1, 5, 1, 7, 8, 9, 10, 11,  1]
    top1NonONEsCollapsed = top1.remap(** {"from": top1OrigLabels, "to": top1RemappedLabels})
    probsArrayIm = one.select(ee.List.sequence(0, 11)).toArray()
    oneArrayMask = ee.Image(ee.Array([0,0,1,0,1,0,1,1,1,1,1,0]))
    oneProb = probsArrayIm.arrayMask(oneArrayMask) \
        .arrayReduce(ee.Reducer.sum(), [0]) \
        .select(0) \
        .arrayProject([0]) \
        .arrayFlatten([['oneProb']])
    # top1Prob = probsArrayIm.arrayReduce(ee.Reducer.max(), [0]).select(0).arrayProject([0]).arrayFlatten([['top1Prob']])

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

    legendDict = {            "Bare": matplotlib.colors.cnames["beige"],
                              "Dune": matplotlib.colors.cnames["khaki"],
                            "Ravine": matplotlib.colors.cnames["fuchsia"],
                            "Saline": matplotlib.colors.cnames["lightsteelblue"],
                    "Savanna (open)": matplotlib.colors.cnames["yellow"],
                   "Savanna (shrub)": matplotlib.colors.cnames["goldenrod"],
                "Savanna (woodland)": matplotlib.colors.cnames["greenyellow"],
                            "Others": matplotlib.colors.cnames["black"]
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
