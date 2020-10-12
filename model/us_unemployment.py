import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
baseurl = os.path.dirname(os.path.abspath(__file__))
from util.file_helper import FileReader
import folium
print(f'baseurl #### {baseurl}')
class UsUnemploy:
    def __init__(self):
        print(f'baseurl #### {baseurl}')
        self.reader = FileReader()
    def show_map(self):
        reader = self.reader
        reader.context = os.path.join(baseurl,'data')
        reader.fname='usa-map.json'
        usa_map =reader.json_load()
        reader.fname ='us_unemployment.csv'
        reader.new_file()
        us_unemploy = reader.csv_to_dframe()
        print(f'{us_unemploy.head()}')
        map = folium.Map(location =[37,-102],zoom_start=5)
        map.choropleth( geo_data= usa_map,
                       name= 'choropleth',
                       data = us_unemploy,
                       columns = ['State','Unemployment'],
                       key_on = 'feature.id',
                       fill_color ='YlGn',
                       fill_opacity =0.7,
                       line_opacity =0.2,
                       legend_name ='Unemployment Rate (%)')
        folium.LayerControl().add_to(map)
        reader = self.reader
        reader.context = os.path.join(baseurl , 'saved_data')
        reader.fname ='usa.html'
        
        map.save(reader.new_file())
    def get_unemploy(self):
        pass
    def set_unemploy(self):
        pass
if __name__ == '__main__':
    us = UsUnemploy()
    us.show_map()
    