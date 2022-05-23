"""Frameworks for running multiple Streamlit applications as a single app.
"""
import streamlit as st

# app_state = st.experimental_get_query_params()
# app_state = {k: v[0] if isinstance(v, list) else v for k, v in app_state.items()} # fetch the first item in each query string as we don't have multiple values for each query string key in this example


class MultiApp:
    """Framework for combining multiple streamlit applications.
    Usage:
        def foo():
            st.title("Hello Foo")
        def bar():
            st.title("Hello Bar")
        app = MultiApp()
        app.add_app("Foo", foo)
        app.add_app("Bar", bar)
        app.run()
    It is also possible keep each application in a separate file.
        import foo
        import bar
        app = MultiApp()
        app.add_app("Foo", foo.app)
        app.add_app("Bar", bar.app)
        app.run()
    """

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        """Adds a new application.
        Parameters
        ----------
        func:
            the python function to render this app.
        title:
            title of the app. Appears in the dropdown in the sidebar.
        """
        self.apps.append({"title": title, "function": func})

    def run(self):
        app_state = st.experimental_get_query_params()
        app_state = {
            k: v[0] if isinstance(v, list) else v for k, v in app_state.items()
        }  # fetch the first item in each query string as we don't have multiple values for each query string key in this example

        # st.write('before', app_state)

        titles = [a["title"] for a in self.apps]
        functions = [a["function"] for a in self.apps]
        default_radio = titles.index(app_state["page"]) if "page" in app_state else 0

        st.sidebar.title("Navigation")

        title = st.sidebar.radio("Go To", titles, index=default_radio, key="radio")

        app_state["page"] = st.session_state.radio
        # st.write('after', app_state)

        st.experimental_set_query_params(**app_state)
        # st.experimental_set_query_params(**st.session_state.to_dict())
        functions[titles.index(title)]()

        st.sidebar.title("India's Open Natural Ecosystems")
        st.sidebar.info(
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
        st.sidebar.title("Funding and support")
        st.sidebar.info(
            """
            Financial support for various aspects of this mapping work came from
            [Azim Premji University](https://azimpremjiuniversity.edu.in/)
            as part of the Research Funding Programme 2020,
            and from the [National Centre for Biological Sciences](https://www.ncbs.res.in/),
            its [Archives](https://archives.ncbs.res.in/),
            the Nadathur Foundation, [TNQ Technologies](http://www.tnq.co.in/)
            and [ATREE](https://www.atree.org/).

            This work would not have been possible without the generosity of efforts behind
            many free and open source scientific computation resources and software tools,
            chief among them being [{geemap}](https://geemap.org/) and
            [Spatial Thoughts](https://spatialthoughts.com/). These analyses
            were carried out on the [Google Earth Engine](https://earthengine.google.com/)
            cloud computing platform.
        """
        )
