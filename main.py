import streamlit as st
from streamlit_folium import folium_static
import folium
from folium.plugins import MarkerCluster, MiniMap, MeasureControl, Draw
import pandas as pd

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


st.title("RICE FIELD LOCATIONS")
st.write("The map I have created using Python programming incorporates various interactive features to enhance its functionality. The map includes location cluster, which groups nearby markers together as the map is zoomed out and separates them as the map is zoomed in. Additionally, the map features a mini map, allowing you to have a small map in the corner of the main map for reference. Furthermore, the measure control has been added to enable you to measure distances and areas on the map. The full screen plugin has also been integrated to enable full-screen mode for the map, and the draw plugin allows you to draw shapes and add markers on the map. These features collectively enhance the map's usability, allowing you to interact with it, measure distances, areas, and switch to full-screen mode, making it a comprehensive and user-friendly mapping solution.")
st.markdown('<hr>', unsafe_allow_html=True)

@st.cache_data
def load_data():
    # Read data from Excel to df
    df = pd.read_excel("rice_field.xlsx", sheet_name="data")
    return df

@st.cache_resource
def create_folium_map(df):
    # Create a Folium map
    mymap = folium.Map(location=[12.304411, 105.095148], zoom_start=9, control_scale=True, tiles="Esri.WorldImagery")

    # Create a MarkerCluster
    marker_cluster = MarkerCluster().add_to(mymap)

    # Iterate through the DataFrame and add markers with popups to the map
    for index, row in df.iterrows():
        popup_text = f"Plot Code: {row['Plot_Code']}<br>Village: {row['Village']}<br>Hectares: {row['Hectares']}"
        folium.Marker(location=[row['Latitude'], row['Longitude']], 
        popup=folium.Popup(popup_text, max_width=300), icon=folium.Icon(color="green")).add_to(marker_cluster)

    # Add measure control tools for easy calculation distand and area
    mymap.add_child(MeasureControl(primary_length_unit="kilometers"))

    # Add minimap to mymap for easy display location
    MiniMap(toggle_display=True).add_to(mymap)

    # Add option to make map can expand to full screen
    folium.plugins.Fullscreen(
        position="topright",
        title="Full Screen",
        title_cancel="Exit me",
        force_separate_button=True,
    ).add_to(mymap)

    # Add draw tool to play with.
    Draw(export=True).add_to(mymap)

    return mymap

# Load data
df = load_data()

# Create a Folium map and cache the results
mymap = create_folium_map(df)

# Display the map in the Streamlit app
folium_static(mymap, width=800, height=700)

st.header('Next Plan', divider='rainbow')
st.write("I will build dashboards, data visualizations, and more. With Python, I can create interactive and visually appealing data visualizations using libraries such as Matplotlib, Seaborn, Plotly, and more. These libraries offer a range of features for creating customized and appealing plots to present data most simply and effectively. I can create a variety of data visualizations, including line charts, bar graphs, histograms, scatter plots, heat maps, and more. As I have time now, I plan to create a dashboard, data visualizations, and more from now until April. I will prepare the data and plan first to ensure that the final product meets my requirements and is of high quality.")

st.write(":blue[Developing by Lay Chansetha]")
