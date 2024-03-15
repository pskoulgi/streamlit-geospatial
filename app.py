import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide", page_title="India's ONE")

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

st.title("Open Land Cover Mapping of India's Semi-arid Open Natural Ecosystems (ONE)")

st.info("Explore the map from pages on the left sidebar.")

st.markdown(
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
    in this [publication](https://doi.org/10.1111/jbi.14471).
    """
)


