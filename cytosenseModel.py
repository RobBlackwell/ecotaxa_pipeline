# Sebastien Galvagno  06/2023



from Template import Template


class cytosenseModel(Template):

    _mapping = {
        #'object_date':{ 'file' : "ROI" , 'header' :'Date', 'index' : 1 , 'fn' : "date" , 'type' : '[t]', 'comment': 'Date'},
        'img_file_name':{ 'file' : None , 'header' :None, 'index' : 1 , 'fn' : None , 'type' : '[t]', 'comment': 'image'},
    }
    
    def __init__(self, models = []): # Array<Template>
        for model in models:
            self.append(model.mapping)
        super().__init__()

    # def key(self,key):
    #     super().key(key)


# head -1 'ATSO_photos_flr16_2uls_10min 2022-06-15 16h31_Pulses.csv' | sed 's/;/\n/g' | sed 's/^/"object_date":{ "file" : "Pulses" , "header" :"/g' | sed 's/$/","index":1, "fn": None, "type":"[t]", "comment":""},/g' | awk '{gsub("index\":1","index\":" NR-1,$0);print}'
class pulse(Template):

    #'object_date':{ 'file' : "Pulses" , 'header' :'Date', 'index' : 1 , 'fn' : "date" , 'type' : '[t]', 'comment': 'Date'},
    _mapping = {            
            "object_id":{ "file" : "Pulses" , "header" :"Particle ID","index":0, "fn": "define_id", "type":"[t]", "comment":""},
            "object_fws":{ "file" : "Pulses" , "header" :"FWS","index":1, "fn": None, "type":"[t]", "comment":""},
            "object_sws":{ "file" : "Pulses" , "header" :"SWS","index":2, "fn": None, "type":"[t]", "comment":""},
            "object_fl_yellow":{ "file" : "Pulses" , "header" :"FL Yellow","index":3, "fn": None, "type":"[t]", "comment":""},
            "object_fl_orange":{ "file" : "Pulses" , "header" :"FL Orange","index":4, "fn": None, "type":"[t]", "comment":""},
            "object_fl_red":{ "file" : "Pulses" , "header" :"FL Red","index":5, "fn": None, "type":"[t]", "comment":""},
            'object_curvature':{ 'file' : "Pulses" , 'header' :'Curvature','index':6, 'fn': None, 'type':'[t]', 'comment':''}
   }


# head -1 'ATSO_photos_flr16_2uls_10min 2022-06-15 16h31_Listmode.csv' | sed 's/;/\n/g' | sed 's/^/"object_date":{ "file" : "ListMode" , "header" :"/g' | sed 's/$/","index":1, "fn": None, "type":"[t]", "comment":""},/g' | awk '{gsub("index\":1","index\":" NR-1,$0);print}' > listnode.txt
class Listnode(Template):
    _mapping = {
        "object_id":{ "file" : "ListMode" , "header" :"Particle ID","index":0, "fn": "extract_name", "type":"[t]", "comment":"ID"},
        "object_sample_len":{ "file" : "ListMode" , "header" :"Sample Length","index":1, "fn": None, "type":"[t]", "comment":""},
        "object_arrival_time":{ "file" : "ListMode" , "header" :"Arrival Time","index":2, "fn": None, "type":"[t]", "comment":""},
        "object_fws_len":{ "file" : "ListMode" , "header" :"FWS Length","index":3, "fn": None, "type":"[t]", "comment":""},
        "object_fws_total":{ "file" : "ListMode" , "header" :"FWS Total","index":4, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"FWS Maximum","index":5, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"FWS Average","index":6, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"FWS Inertia","index":7, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"FWS Center of gravity","index":8, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"FWS Fill factor","index":9, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"FWS Asymmetry","index":10, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"FWS Number of cells","index":11, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"FWS First","index":12, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"FWS Last","index":13, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"FWS Minimum","index":14, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"FWS SWS covariance","index":15, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"SWS Length","index":16, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"SWS Total","index":17, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"SWS Maximum","index":18, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"SWS Average","index":19, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"SWS Inertia","index":20, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"SWS Center of gravity","index":21, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"SWS Fill factor","index":22, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"SWS Asymmetry","index":23, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"SWS Number of cells","index":24, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"SWS First","index":25, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"SWS Last","index":26, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"SWS Minimum","index":27, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"SWS SWS covariance","index":28, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"FL Yellow Length","index":29, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"FL Yellow Total","index":30, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"FL Yellow Maximum","index":31, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"FL Yellow Average","index":32, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"FL Yellow Inertia","index":33, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"FL Yellow Center of gravity","index":34, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"FL Yellow Fill factor","index":35, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"FL Yellow Asymmetry","index":36, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"FL Yellow Number of cells","index":37, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"FL Yellow First","index":38, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"FL Yellow Last","index":39, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"FL Yellow Minimum","index":40, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"FL Yellow SWS covariance","index":41, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"FL Orange Length","index":42, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"FL Orange Total","index":43, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"FL Orange Maximum","index":44, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"FL Orange Average","index":45, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"FL Orange Inertia","index":46, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"FL Orange Center of gravity","index":47, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"FL Orange Fill factor","index":48, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"FL Orange Asymmetry","index":49, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"FL Orange Number of cells","index":50, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"FL Orange First","index":51, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"FL Orange Last","index":52, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"FL Orange Minimum","index":53, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"FL Orange SWS covariance","index":54, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"FL Red Length","index":55, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"FL Red Total","index":56, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"FL Red Maximum","index":57, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"FL Red Average","index":58, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"FL Red Inertia","index":59, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"FL Red Center of gravity","index":60, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"FL Red Fill factor","index":61, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"FL Red Asymmetry","index":62, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"FL Red Number of cells","index":63, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"FL Red First","index":64, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"FL Red Last","index":65, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"FL Red Minimum","index":66, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"FL Red SWS covariance","index":67, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Curvature Length","index":68, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Curvature Total","index":69, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Curvature Maximum","index":70, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Curvature Average","index":71, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Curvature Inertia","index":72, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Curvature Center of gravity","index":73, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Curvature Fill factor","index":74, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Curvature Asymmetry","index":75, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Curvature Number of cells","index":76, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Curvature First","index":77, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Curvature Last","index":78, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Curvature Minimum","index":79, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Curvature SWS covariance","index":80, "fn": None, "type":"[t]", "comment":""},
    }


class CefasListNode(Template):

    _mapping = {
        "object_id":{ "file" : "ListMode" , "header" :"﻿Particle ID","index":0, "fn": "extract_name", "type":"[t]", "comment":"ID"},
        "object_sample_len":{ "file" : "ListMode" , "header" :"Sample Length","index":1, "fn": None, "type":"[t]", "comment":""},
        "object_time":{ "file" : "ListMode" , "header" :"Arrival Time","index":2, "fn": None, "type":"[t]", "comment":""},
        "object_fws_length":{ "file" : "ListMode" , "header" :"FWS Length","index":3, "fn": None, "type":"[t]", "comment":""},
        "object_fws_total":{ "file" : "ListMode" , "header" :"FWS Total","index":4, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"FWS Maximum","index":5, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"FWS Average","index":6, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"FWS Inertia","index":7, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"FWS Center of gravity","index":8, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"FWS Fill factor","index":9, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"FWS Asymmetry","index":10, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"FWS Number of cells","index":11, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"FWS First","index":12, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"FWS Last","index":13, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"FWS Minimum","index":14, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"FWS SWS covariance","index":15, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"FWS Length(50%)","index":16, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Sidewards Scatter Length","index":17, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Sidewards Scatter Total","index":18, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Sidewards Scatter Maximum","index":19, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Sidewards Scatter Average","index":20, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Sidewards Scatter Inertia","index":21, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Sidewards Scatter Center of gravity","index":22, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Sidewards Scatter Fill factor","index":23, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Sidewards Scatter Asymmetry","index":24, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Sidewards Scatter Number of cells","index":25, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Sidewards Scatter First","index":26, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Sidewards Scatter Last","index":27, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Sidewards Scatter Minimum","index":28, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Sidewards Scatter SWS covariance","index":29, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Sidewards Scatter Length(50%)","index":30, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Fl Yellow Length","index":31, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Fl Yellow Total","index":32, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Fl Yellow Maximum","index":33, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Fl Yellow Average","index":34, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Fl Yellow Inertia","index":35, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Fl Yellow Center of gravity","index":36, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Fl Yellow Fill factor","index":37, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Fl Yellow Asymmetry","index":38, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Fl Yellow Number of cells","index":39, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Fl Yellow First","index":40, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Fl Yellow Last","index":41, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Fl Yellow Minimum","index":42, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Fl Yellow SWS covariance","index":43, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Fl Yellow Length(50%)","index":44, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Fl Orange Length","index":45, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Fl Orange Total","index":46, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Fl Orange Maximum","index":47, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Fl Orange Average","index":48, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Fl Orange Inertia","index":49, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Fl Orange Center of gravity","index":50, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Fl Orange Fill factor","index":51, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Fl Orange Asymmetry","index":52, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Fl Orange Number of cells","index":53, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Fl Orange First","index":54, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Fl Orange Last","index":55, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Fl Orange Minimum","index":56, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Fl Orange SWS covariance","index":57, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Fl Orange Length(50%)","index":58, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Fl Red Length","index":59, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Fl Red Total","index":60, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Fl Red Maximum","index":61, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Fl Red Average","index":62, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Fl Red Inertia","index":63, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Fl Red Center of gravity","index":64, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Fl Red Fill factor","index":65, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Fl Red Asymmetry","index":66, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Fl Red Number of cells","index":67, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Fl Red First","index":68, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Fl Red Last","index":69, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Fl Red Minimum","index":70, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Fl Red SWS covariance","index":71, "fn": None, "type":"[t]", "comment":""},
        # "object_date":{ "file" : "ListMode" , "header" :"Fl Red Length(50%)","index":72, "fn": None, "type":"[t]", "comment":""},
    }


# # sed 's/:.*//g' 'ATSO_photos_flr16_2uls_10min 2022-06-15 16h31_Info.txt' | sed 's/^/"object_date":{ "file" : "Info" , "header" :"/g' | sed 's/$/","index":1, "fn": None, "type":"[t]", "comment":""},/g' | awk '{gsub("index\":1","index\":" NR-1,$0);print}' > info.txt
class Info(Template):
   
    # Question : is channel order can change?
   _mapping = {
#         "sample_":{ "file" : "Info" , "header" :"﻿Trigger level (mV)","index":0, "fn": None, "type":"[t]", "comment":""},
#         "sample_":{ "file" : "Info" , "header" :"CytoUSB Block size","index":1, "fn": None, "type":"[t]", "comment":""},
# -        "sample_":{ "file" : "Info" , "header" :"Instrument","index":3, "fn": None, "type":"[t]", "comment":""},
#         "sample_":{ "file" : "Info" , "header" :"Beam width","index":4, "fn": None, "type":"[t]", "comment":""},
#         "sample_":{ "file" : "Info" , "header" :"Core speed","index":5, "fn": None, "type":"[t]", "comment":""},
#         "sample_":{ "file" : "Info" , "header" :"User Comments","index":6, "fn": None, "type":"[t]", "comment":""},
# -        "sample_":{ "file" : "Info" , "header" :"Measurement date","index":8, "fn": None, "type":"[t]", "comment":""},
#         "sample_":{ "file" : "Info" , "header" :"Measurement duration","index":9, "fn": None, "type":"[t]", "comment":""},
#         "sample_":{ "file" : "Info" , "header" :"Flow rate (μL/sec)","index":10, "fn": None, "type":"[t]", "comment":""},
# -        "sample_":{ "file" : "Info" , "header" :"Channel 1","index":12, "fn": None, "type":"[t]", "comment":""},
#         "sample_":{ "file" : "Info" , "header" :"Channel 2","index":13, "fn": None, "type":"[t]", "comment":""},
#         "sample_":{ "file" : "Info" , "header" :"Channel 3","index":14, "fn": None, "type":"[t]", "comment":""},
#         "sample_":{ "file" : "Info" , "header" :"Channel 4","index":15, "fn": None, "type":"[t]", "comment":""},
#         "sample_":{ "file" : "Info" , "header" :"  - sensitivity level","index":16, "fn": None, "type":"[t]", "comment":""},
#         "sample_":{ "file" : "Info" , "header" :"Channel 5","index":17, "fn": None, "type":"[t]", "comment":""},
#         "sample_":{ "file" : "Info" , "header" :"  - sensitivity level","index":18, "fn": None, "type":"[t]", "comment":""},
#         "sample_":{ "file" : "Info" , "header" :"Channel 6","index":19, "fn": None, "type":"[t]", "comment":""},
#         "sample_":{ "file" : "Info" , "header" :"  - sensitivity level","index":20, "fn": None, "type":"[t]", "comment":""},
#         "sample_":{ "file" : "Info" , "header" :"Channel 7","index":21, "fn": None, "type":"[t]", "comment":""},
#         "sample_":{ "file" : "Info" , "header" :"  - sensitivity level","index":22, "fn": None, "type":"[t]", "comment":""},
#         "sample_":{ "file" : "Info" , "header" :"Total number of particles","index":24, "fn": None, "type":"[t]", "comment":""},
#         "sample_":{ "file" : "Info" , "header" :"Smart triggered number of particles","index":25, "fn": None, "type":"[t]", "comment":""},
#         "sample_":{ "file" : "Info" , "header" :"Concentration (part/μL)","index":26, "fn": None, "type":"[t]", "comment":""},
#         "sample_":{ "file" : "Info" , "header" :"Volume (μL)","index":27, "fn": None, "type":"[t]", "comment":""},
    }