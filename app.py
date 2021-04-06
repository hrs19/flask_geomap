from flask import Flask, render_template

import folium

app = Flask(__name__)


@app.route('/')
def index():
    start_coords = (19.076090, 72.877426)
    folium_map = folium.Map(location=start_coords, zoom_start=12)
    folium_map.save('templates/map.html')    
    start_coords = (19.218330, 72.978088)
    folium_map = folium.Map(location=start_coords, zoom_start=12)
    folium_map.save('templates/map2.html')        
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)