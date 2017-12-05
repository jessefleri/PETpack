<!DOCTYPE html>
<head>    
    <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
    <script>L_PREFER_CANVAS = false; L_NO_TOUCH = false; L_DISABLE_3D = false;</script>
    <script src="https://cdn.jsdelivr.net/npm/leaflet@1.2.0/dist/leaflet.js"></script>
    <script src="https://code.jquery.com/jquery-2.1.0.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/leaflet@1.2.0/dist/leaflet.css" />
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css" />
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css" />
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css" />
    <link rel="stylesheet" href="https://rawgit.com/python-visualization/folium/master/folium/templates/leaflet.awesome.rotate.css" />
    <style>html, body {width: 100%;height: 100%;margin: 0;padding: 0;}</style>
    <style>#map {position:absolute;top:0;bottom:0;right:0;left:0;}</style>
    
            <style> #map_a11e733e71494a52a5a1a1025d8522bf {
                position : relative;
                width : 100.0%;
                height: 100.0%;
                left: 0.0%;
                top: 0.0%;
                }
            </style>
        
    
            <style> #vega_7aef3140c26d40029baae1a5edac6edc {
                position : relative;
                width : 525.0px;
                height: 250.0px;
                left: 0.0%;
                top: 0.0%;
            </style>
            
    <script src="https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.5/d3.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/vega/1.4.3/vega.min.js"></script>
    
            <style> #vega_4d0148364e334127b51d1befac4ac22d {
                position : relative;
                width : 525.0px;
                height: 250.0px;
                left: 0.0%;
                top: 0.0%;
            </style>
            
    
            <style> #vega_cfcbd4a4d59c45fcb7040f8bd48ede6c {
                position : relative;
                width : 525.0px;
                height: 250.0px;
                left: 0.0%;
                top: 0.0%;
            </style>
            
    
            <style> #vega_3cab17cdbb7c40c6bc1cec9940e39b85 {
                position : relative;
                width : 525.0px;
                height: 250.0px;
                left: 0.0%;
                top: 0.0%;
            </style>
            
    
            <style> #vega_edeb116b7e664574a2746ab62913a815 {
                position : relative;
                width : 525.0px;
                height: 250.0px;
                left: 0.0%;
                top: 0.0%;
            </style>
            
    
            <style> #vega_76cdf42684dd4adfb8788665db3192ab {
                position : relative;
                width : 525.0px;
                height: 250.0px;
                left: 0.0%;
                top: 0.0%;
            </style>
            
    
            <style> #vega_6b92085a0efd4ed9bc92cd1bc9252ea5 {
                position : relative;
                width : 525.0px;
                height: 250.0px;
                left: 0.0%;
                top: 0.0%;
            </style>
            
    
            <style> #vega_c917469539ba495497ae1eb78a06ba81 {
                position : relative;
                width : 525.0px;
                height: 250.0px;
                left: 0.0%;
                top: 0.0%;
            </style>
            
    
            <style> #vega_5e21ccecff5e4da69dc8ae014cbc1ab3 {
                position : relative;
                width : 525.0px;
                height: 250.0px;
                left: 0.0%;
                top: 0.0%;
            </style>
            
    
            <style> #vega_7df0c0ddd4884579acacf9c93aaf2c6e {
                position : relative;
                width : 525.0px;
                height: 250.0px;
                left: 0.0%;
                top: 0.0%;
            </style>
            
    
            <style> #vega_8d90d7f8dc8b4be29c563c96d798915b {
                position : relative;
                width : 525.0px;
                height: 250.0px;
                left: 0.0%;
                top: 0.0%;
            </style>
            
    
            <style> #vega_6b8867458c994b1c939dac8afaec2ec2 {
                position : relative;
                width : 525.0px;
                height: 250.0px;
                left: 0.0%;
                top: 0.0%;
            </style>
            
</head>
<body>    
    
            <div class="folium-map" id="map_a11e733e71494a52a5a1a1025d8522bf" ></div>
        
</body>
<script>    
    

            
                var bounds = null;
            

            var map_a11e733e71494a52a5a1a1025d8522bf = L.map(
                                  'map_a11e733e71494a52a5a1a1025d8522bf',
                                  {center: [39.737,-110.8338],
                                  zoom: 7,
                                  maxBounds: bounds,
                                  layers: [],
                                  worldCopyJump: false,
                                  crs: L.CRS.EPSG3857
                                 });
            
        
    
            var tile_layer_06e43775d3a042ac82ff9945b4d4df37 = L.tileLayer(
                'https://stamen-tiles-{s}.a.ssl.fastly.net/terrain/{z}/{x}/{y}.jpg',
                {
  "attribution": null, 
  "detectRetina": false, 
  "maxZoom": 18, 
  "minZoom": 1, 
  "noWrap": false, 
  "subdomains": "abc"
}
                ).addTo(map_a11e733e71494a52a5a1a1025d8522bf);
        
    
            var circle_marker_17c0c30867c747599827e06f39c0141c = L.circleMarker(
                [38.574,-109.546],
                {
  "bubblingMouseEvents": true, 
  "color": "crimson", 
  "dashArray": null, 
  "dashOffset": null, 
  "fill": true, 
  "fillColor": "crimson", 
  "fillOpacity": 0.2, 
  "fillRule": "evenodd", 
  "lineCap": "round", 
  "lineJoin": "round", 
  "opacity": 1.0, 
  "radius": 10, 
  "stroke": true, 
  "weight": 3
}
                ).addTo(map_a11e733e71494a52a5a1a1025d8522bf);
            
    function vega_parse(spec, div) {
            vg.parse.spec(spec, function(chart) { chart({el:div}).update(); });}
    
            var popup_c1e375c7bbc14ee08037133a0c181222 = L.popup({maxWidth: '650'});

            
                var vega_7aef3140c26d40029baae1a5edac6edc = $('             <div id="vega_7aef3140c26d40029baae1a5edac6edc"></div>             ')[0];
                popup_c1e375c7bbc14ee08037133a0c181222.setContent(vega_7aef3140c26d40029baae1a5edac6edc);
            

            circle_marker_17c0c30867c747599827e06f39c0141c.bindPopup(popup_c1e375c7bbc14ee08037133a0c181222);

            
                
            vega_parse({"legends": [{"title": "Models", "offset": 0, "properties": {}, "fill": "color"}], "scales": [{"range": "width", "domain": {"field": "data.idx", "data": "table"}, "type": "linear", "name": "x"}, {"range": "height", "domain": {"field": "data.val", "data": "table"}, "name": "y", "nice": true}, {"range": "category20", "domain": {"field": "data.col", "data": "table"}, "type": "ordinal", "name": "color"}], "axes": [{"scale": "x", "type": "x", "title": "Month"}, {"scale": "y", "type": "y", "title": "Potential ET (mm)"}], "height": 200, "padding": "auto", "width": 400, "marks": [{"type": "group", "from": {"data": "table", "transform": [{"keys": ["data.col"], "type": "facet"}]}, "marks": [{"type": "line", "properties": {"enter": {"y": {"field": "data.val", "scale": "y"}, "x": {"field": "data.idx", "scale": "x"}, "stroke": {"field": "data.col", "scale": "color"}, "strokeWidth": {"value": 2}}}}]}], "data": [{"values": [{"val": 0.0, "col": "thornthwait", "idx": 1}, {"val": 16.97212487939074, "col": "blaney-criddle", "idx": 1}, {"val": 0.0, "col": "hargreaves", "idx": 1}, {"val": 4.179029818980236, "col": "thornthwait", "idx": 2}, {"val": 18.6406069727356, "col": "blaney-criddle", "idx": 2}, {"val": 13.177545136905428, "col": "hargreaves", "idx": 2}, {"val": 30.87514305547569, "col": "thornthwait", "idx": 3}, {"val": 33.58000974474676, "col": "blaney-criddle", "idx": 3}, {"val": 33.57419700341127, "col": "hargreaves", "idx": 3}, {"val": 50.99174642106648, "col": "thornthwait", "idx": 4}, {"val": 38.99334801459835, "col": "blaney-criddle", "idx": 4}, {"val": 41.30997647009155, "col": "hargreaves", "idx": 4}, {"val": 89.73658736389082, "col": "thornthwait", "idx": 5}, {"val": 51.70405025147265, "col": "blaney-criddle", "idx": 5}, {"val": 55.91885695621447, "col": "hargreaves", "idx": 5}, {"val": 168.53141369928122, "col": "thornthwait", "idx": 6}, {"val": 62.44960630100534, "col": "blaney-criddle", "idx": 6}, {"val": 81.47038186048853, "col": "hargreaves", "idx": 6}, {"val": 182.08568833617497, "col": "thornthwait", "idx": 7}, {"val": 66.96580875398278, "col": "blaney-criddle", "idx": 7}, {"val": 88.026166710172, "col": "hargreaves", "idx": 7}, {"val": 142.0603430859813, "col": "thornthwait", "idx": 8}, {"val": 58.376449720946425, "col": "blaney-criddle", "idx": 8}, {"val": 78.0103269217977, "col": "hargreaves", "idx": 8}, {"val": 93.32751040432699, "col": "thornthwait", "idx": 9}, {"val": 44.542247389225835, "col": "blaney-criddle", "idx": 9}, {"val": 62.685662240402415, "col": "hargreaves", "idx": 9}, {"val": 58.76917362259921, "col": "thornthwait", "idx": 10}, {"val": 37.52816076376793, "col": "blaney-criddle", "idx": 10}, {"val": 51.01062462533866, "col": "hargreaves", "idx": 10}, {"val": 19.939211476354924, "col": "thornthwait", "idx": 11}, {"val": 24.749684531638536, "col": "blaney-criddle", "idx": 11}, {"val": 29.01628365070629, "col": "hargreaves", "idx": 11}, {"val": 1.6791965952342105, "col": "thornthwait", "idx": 12}, {"val": 18.267885687777497, "col": "blaney-criddle", "idx": 12}, {"val": 10.251908879275572, "col": "hargreaves", "idx": 12}], "name": "table"}]},vega_7aef3140c26d40029baae1a5edac6edc);
            
            
        
    
            var circle_marker_b03784ee673c48db9bfb01c94e9a1499 = L.circleMarker(
                [37.268,-109.927],
                {
  "bubblingMouseEvents": true, 
  "color": "crimson", 
  "dashArray": null, 
  "dashOffset": null, 
  "fill": true, 
  "fillColor": "crimson", 
  "fillOpacity": 0.2, 
  "fillRule": "evenodd", 
  "lineCap": "round", 
  "lineJoin": "round", 
  "opacity": 1.0, 
  "radius": 10, 
  "stroke": true, 
  "weight": 3
}
                ).addTo(map_a11e733e71494a52a5a1a1025d8522bf);
            
    
            var popup_9769cb181ac04b829e346caa9011ed34 = L.popup({maxWidth: '650'});

            
                var vega_4d0148364e334127b51d1befac4ac22d = $('             <div id="vega_4d0148364e334127b51d1befac4ac22d"></div>             ')[0];
                popup_9769cb181ac04b829e346caa9011ed34.setContent(vega_4d0148364e334127b51d1befac4ac22d);
            

            circle_marker_b03784ee673c48db9bfb01c94e9a1499.bindPopup(popup_9769cb181ac04b829e346caa9011ed34);

            
                
            vega_parse({"legends": [{"title": "Models", "offset": 0, "properties": {}, "fill": "color"}], "scales": [{"range": "width", "domain": {"field": "data.idx", "data": "table"}, "type": "linear", "name": "x"}, {"range": "height", "domain": {"field": "data.val", "data": "table"}, "name": "y", "nice": true}, {"range": "category20", "domain": {"field": "data.col", "data": "table"}, "type": "ordinal", "name": "color"}], "axes": [{"scale": "x", "type": "x", "title": "Month"}, {"scale": "y", "type": "y", "title": "Potential ET (mm)"}], "height": 200, "padding": "auto", "width": 400, "marks": [{"type": "group", "from": {"data": "table", "transform": [{"keys": ["data.col"], "type": "facet"}]}, "marks": [{"type": "line", "properties": {"enter": {"y": {"field": "data.val", "scale": "y"}, "x": {"field": "data.idx", "scale": "x"}, "stroke": {"field": "data.col", "scale": "color"}, "strokeWidth": {"value": 2}}}}]}], "data": [{"values": [{"val": 0.0, "col": "thornthwait", "idx": 1}, {"val": 16.97212487939074, "col": "blaney-criddle", "idx": 1}, {"val": 0.0, "col": "hargreaves", "idx": 1}, {"val": 9.334233692411992, "col": "thornthwait", "idx": 2}, {"val": 20.577392830683078, "col": "blaney-criddle", "idx": 2}, {"val": 18.55351402921091, "col": "hargreaves", "idx": 2}, {"val": 29.85431939815501, "col": "thornthwait", "idx": 3}, {"val": 33.22244482616844, "col": "blaney-criddle", "idx": 3}, {"val": 32.740300907083856, "col": "hargreaves", "idx": 3}, {"val": 46.75139593109441, "col": "thornthwait", "idx": 4}, {"val": 37.999060870101935, "col": "blaney-criddle", "idx": 4}, {"val": 39.06765472862496, "col": "hargreaves", "idx": 4}, {"val": 82.40453874907044, "col": "thornthwait", "idx": 5}, {"val": 50.25874986768088, "col": "blaney-criddle", "idx": 5}, {"val": 52.83820208078631, "col": "hargreaves", "idx": 5}, {"val": 170.5511797158427, "col": "thornthwait", "idx": 6}, {"val": 62.7310762098674, "col": "blaney-criddle", "idx": 6}, {"val": 82.14247294089171, "col": "hargreaves", "idx": 6}, {"val": 184.0821158019762, "col": "thornthwait", "idx": 7}, {"val": 67.26033281963757, "col": "blaney-criddle", "idx": 7}, {"val": 88.72970610453059, "col": "hargreaves", "idx": 7}, {"val": 135.88725102608, "col": "thornthwait", "idx": 8}, {"val": 57.416624516180036, "col": "blaney-criddle", "idx": 8}, {"val": 75.64522565370162, "col": "hargreaves", "idx": 8}, {"val": 92.924826617205, "col": "thornthwait", "idx": 9}, {"val": 44.426774926426894, "col": "blaney-criddle", "idx": 9}, {"val": 62.37392624352104, "col": "hargreaves", "idx": 9}, {"val": 58.58125994050121, "col": "thornthwait", "idx": 10}, {"val": 37.418345535069875, "col": "blaney-criddle", "idx": 10}, {"val": 50.707544380348196, "col": "hargreaves", "idx": 10}, {"val": 19.877387833554213, "col": "thornthwait", "idx": 11}, {"val": 24.657588957422764, "col": "blaney-criddle", "idx": 11}, {"val": 28.751273529356375, "col": "hargreaves", "idx": 11}, {"val": 2.0233566884715324, "col": "thornthwait", "idx": 12}, {"val": 18.453592371012363, "col": "blaney-criddle", "idx": 12}, {"val": 10.860901760826627, "col": "hargreaves", "idx": 12}], "name": "table"}]},vega_4d0148364e334127b51d1befac4ac22d);
            
            
        
    
            var circle_marker_27911b1d612042a1b4bdd4bd49d72d1f = L.circleMarker(
                [41.746,-111.803],
                {
  "bubblingMouseEvents": true, 
  "color": "crimson", 
  "dashArray": null, 
  "dashOffset": null, 
  "fill": true, 
  "fillColor": "crimson", 
  "fillOpacity": 0.2, 
  "fillRule": "evenodd", 
  "lineCap": "round", 
  "lineJoin": "round", 
  "opacity": 1.0, 
  "radius": 10, 
  "stroke": true, 
  "weight": 3
}
                ).addTo(map_a11e733e71494a52a5a1a1025d8522bf);
            
    
            var popup_5a103bce738444618c5a0d5cd7f52311 = L.popup({maxWidth: '650'});

            
                var vega_cfcbd4a4d59c45fcb7040f8bd48ede6c = $('             <div id="vega_cfcbd4a4d59c45fcb7040f8bd48ede6c"></div>             ')[0];
                popup_5a103bce738444618c5a0d5cd7f52311.setContent(vega_cfcbd4a4d59c45fcb7040f8bd48ede6c);
            

            circle_marker_27911b1d612042a1b4bdd4bd49d72d1f.bindPopup(popup_5a103bce738444618c5a0d5cd7f52311);

            
                
            vega_parse({"legends": [{"title": "Models", "offset": 0, "properties": {}, "fill": "color"}], "scales": [{"range": "width", "domain": {"field": "data.idx", "data": "table"}, "type": "linear", "name": "x"}, {"range": "height", "domain": {"field": "data.val", "data": "table"}, "name": "y", "nice": true}, {"range": "category20", "domain": {"field": "data.col", "data": "table"}, "type": "ordinal", "name": "color"}], "axes": [{"scale": "x", "type": "x", "title": "Month"}, {"scale": "y", "type": "y", "title": "Potential ET (mm)"}], "height": 200, "padding": "auto", "width": 400, "marks": [{"type": "group", "from": {"data": "table", "transform": [{"keys": ["data.col"], "type": "facet"}]}, "marks": [{"type": "line", "properties": {"enter": {"y": {"field": "data.val", "scale": "y"}, "x": {"field": "data.idx", "scale": "x"}, "stroke": {"field": "data.col", "scale": "color"}, "strokeWidth": {"value": 2}}}}]}], "data": [{"values": [{"val": 0.0, "col": "thornthwait", "idx": 1}, {"val": 12.362721222109712, "col": "blaney-criddle", "idx": 1}, {"val": 0.0, "col": "hargreaves", "idx": 1}, {"val": 0.0, "col": "thornthwait", "idx": 2}, {"val": 14.326856652761673, "col": "blaney-criddle", "idx": 2}, {"val": 0.0, "col": "hargreaves", "idx": 2}, {"val": 18.14878540209551, "col": "thornthwait", "idx": 3}, {"val": 27.382217822722513, "col": "blaney-criddle", "idx": 3}, {"val": 19.470381631550335, "col": "hargreaves", "idx": 3}, {"val": 45.05658982236383, "col": "thornthwait", "idx": 4}, {"val": 34.76762765048861, "col": "blaney-criddle", "idx": 4}, {"val": 31.952808934243656, "col": "hargreaves", "idx": 4}, {"val": 67.9298486167391, "col": "thornthwait", "idx": 5}, {"val": 44.333018294134604, "col": "blaney-criddle", "idx": 5}, {"val": 40.65808710988987, "col": "hargreaves", "idx": 5}, {"val": 125.59334310856413, "col": "thornthwait", "idx": 6}, {"val": 54.56844885286749, "col": "blaney-criddle", "idx": 6}, {"val": 63.31038276554996, "col": "hargreaves", "idx": 6}, {"val": 147.16642341388135, "col": "thornthwait", "idx": 7}, {"val": 60.92806540806008, "col": "blaney-criddle", "idx": 7}, {"val": 73.968501242202, "col": "hargreaves", "idx": 7}, {"val": 128.37059013306967, "col": "thornthwait", "idx": 8}, {"val": 55.08562044746169, "col": "blaney-criddle", "idx": 8}, {"val": 69.98756027831153, "col": "hargreaves", "idx": 8}, {"val": 76.23990651738465, "col": "thornthwait", "idx": 9}, {"val": 39.57693148887143, "col": "blaney-criddle", "idx": 9}, {"val": 49.65884301229918, "col": "hargreaves", "idx": 9}, {"val": 44.246577466130354, "col": "thornthwait", "idx": 10}, {"val": 32.0373993288655, "col": "blaney-criddle", "idx": 10}, {"val": 36.378190249409826, "col": "hargreaves", "idx": 10}, {"val": 16.58061633431798, "col": "thornthwait", "idx": 11}, {"val": 21.71053058251806, "col": "blaney-criddle", "idx": 11}, {"val": 20.396632081229782, "col": "hargreaves", "idx": 11}, {"val": 0.0, "col": "thornthwait", "idx": 12}, {"val": 12.418125165879244, "col": "blaney-criddle", "idx": 12}, {"val": 0.0, "col": "hargreaves", "idx": 12}], "name": "table"}]},vega_cfcbd4a4d59c45fcb7040f8bd48ede6c);
            
            
        
    
            var circle_marker_0df667756ad5414496eaa42909853933 = L.circleMarker(
                [41.616,-112.544],
                {
  "bubblingMouseEvents": true, 
  "color": "crimson", 
  "dashArray": null, 
  "dashOffset": null, 
  "fill": true, 
  "fillColor": "crimson", 
  "fillOpacity": 0.2, 
  "fillRule": "evenodd", 
  "lineCap": "round", 
  "lineJoin": "round", 
  "opacity": 1.0, 
  "radius": 10, 
  "stroke": true, 
  "weight": 3
}
                ).addTo(map_a11e733e71494a52a5a1a1025d8522bf);
            
    
            var popup_d24e514e94d8415fa5fd415e03646cf2 = L.popup({maxWidth: '650'});

            
                var vega_3cab17cdbb7c40c6bc1cec9940e39b85 = $('             <div id="vega_3cab17cdbb7c40c6bc1cec9940e39b85"></div>             ')[0];
                popup_d24e514e94d8415fa5fd415e03646cf2.setContent(vega_3cab17cdbb7c40c6bc1cec9940e39b85);
            

            circle_marker_0df667756ad5414496eaa42909853933.bindPopup(popup_d24e514e94d8415fa5fd415e03646cf2);

            
                
            vega_parse({"legends": [{"title": "Models", "offset": 0, "properties": {}, "fill": "color"}], "scales": [{"range": "width", "domain": {"field": "data.idx", "data": "table"}, "type": "linear", "name": "x"}, {"range": "height", "domain": {"field": "data.val", "data": "table"}, "name": "y", "nice": true}, {"range": "category20", "domain": {"field": "data.col", "data": "table"}, "type": "ordinal", "name": "color"}], "axes": [{"scale": "x", "type": "x", "title": "Month"}, {"scale": "y", "type": "y", "title": "Potential ET (mm)"}], "height": 200, "padding": "auto", "width": 400, "marks": [{"type": "group", "from": {"data": "table", "transform": [{"keys": ["data.col"], "type": "facet"}]}, "marks": [{"type": "line", "properties": {"enter": {"y": {"field": "data.val", "scale": "y"}, "x": {"field": "data.idx", "scale": "x"}, "stroke": {"field": "data.col", "scale": "color"}, "strokeWidth": {"value": 2}}}}]}], "data": [{"values": [{"val": 0.0, "col": "thornthwait", "idx": 1}, {"val": 12.07463349352965, "col": "blaney-criddle", "idx": 1}, {"val": 0.0, "col": "hargreaves", "idx": 1}, {"val": 0.0, "col": "thornthwait", "idx": 2}, {"val": 14.502928094393262, "col": "blaney-criddle", "idx": 2}, {"val": 0.0, "col": "hargreaves", "idx": 2}, {"val": 17.75887062487531, "col": "thornthwait", "idx": 3}, {"val": 26.786276291758643, "col": "blaney-criddle", "idx": 3}, {"val": 18.128155055590042, "col": "hargreaves", "idx": 3}, {"val": 41.668957864802586, "col": "thornthwait", "idx": 4}, {"val": 33.40048282680604, "col": "blaney-criddle", "idx": 4}, {"val": 29.01628365070629, "col": "hargreaves", "idx": 4}, {"val": 63.79540393642754, "col": "thornthwait", "idx": 5}, {"val": 42.74318787196365, "col": "blaney-criddle", "idx": 5}, {"val": 37.51064045731992, "col": "hargreaves", "idx": 5}, {"val": 123.74878473463545, "col": "thornthwait", "idx": 6}, {"val": 53.86477408071233, "col": "blaney-criddle", "idx": 6}, {"val": 61.75170380170054, "col": "hargreaves", "idx": 6}, {"val": 146.69319911907877, "col": "thornthwait", "idx": 7}, {"val": 60.6335413424053, "col": "blaney-criddle", "idx": 7}, {"val": 73.30076921707935, "col": "hargreaves", "idx": 7}, {"val": 124.17001025236613, "col": "thornthwait", "idx": 8}, {"val": 53.98867735630012, "col": "blaney-criddle", "idx": 8}, {"val": 67.36766766382777, "col": "hargreaves", "idx": 8}, {"val": 70.58250428052348, "col": "thornthwait", "idx": 9}, {"val": 37.960317009686264, "col": "blaney-criddle", "idx": 9}, {"val": 45.58477799803905, "col": "hargreaves", "idx": 9}, {"val": 40.3102329609361, "col": "thornthwait", "idx": 10}, {"val": 30.609801355790864, "col": "blaney-criddle", "idx": 10}, {"val": 32.740300907083856, "col": "hargreaves", "idx": 10}, {"val": 12.431324018055939, "col": "thornthwait", "idx": 11}, {"val": 20.237001395065707, "col": "blaney-criddle", "idx": 11}, {"val": 16.23718024525587, "col": "hargreaves", "idx": 11}, {"val": 0.0, "col": "thornthwait", "idx": 12}, {"val": 11.489591749704918, "col": "blaney-criddle", "idx": 12}, {"val": 0.0, "col": "hargreaves", "idx": 12}], "name": "table"}]},vega_3cab17cdbb7c40c6bc1cec9940e39b85);
            
            
        
    
            var circle_marker_112e072bafcc4100a2a425da35c0adbe = L.circleMarker(
                [40.246,-111.651],
                {
  "bubblingMouseEvents": true, 
  "color": "crimson", 
  "dashArray": null, 
  "dashOffset": null, 
  "fill": true, 
  "fillColor": "crimson", 
  "fillOpacity": 0.2, 
  "fillRule": "evenodd", 
  "lineCap": "round", 
  "lineJoin": "round", 
  "opacity": 1.0, 
  "radius": 10, 
  "stroke": true, 
  "weight": 3
}
                ).addTo(map_a11e733e71494a52a5a1a1025d8522bf);
            
    
            var popup_5149f3d483d140d9a87147c2f64a8277 = L.popup({maxWidth: '650'});

            
                var vega_edeb116b7e664574a2746ab62913a815 = $('             <div id="vega_edeb116b7e664574a2746ab62913a815"></div>             ')[0];
                popup_5149f3d483d140d9a87147c2f64a8277.setContent(vega_edeb116b7e664574a2746ab62913a815);
            

            circle_marker_112e072bafcc4100a2a425da35c0adbe.bindPopup(popup_5149f3d483d140d9a87147c2f64a8277);

            
                
            vega_parse({"legends": [{"title": "Models", "offset": 0, "properties": {}, "fill": "color"}], "scales": [{"range": "width", "domain": {"field": "data.idx", "data": "table"}, "type": "linear", "name": "x"}, {"range": "height", "domain": {"field": "data.val", "data": "table"}, "name": "y", "nice": true}, {"range": "category20", "domain": {"field": "data.col", "data": "table"}, "type": "ordinal", "name": "color"}], "axes": [{"scale": "x", "type": "x", "title": "Month"}, {"scale": "y", "type": "y", "title": "Potential ET (mm)"}], "height": 200, "padding": "auto", "width": 400, "marks": [{"type": "group", "from": {"data": "table", "transform": [{"keys": ["data.col"], "type": "facet"}]}, "marks": [{"type": "line", "properties": {"enter": {"y": {"field": "data.val", "scale": "y"}, "x": {"field": "data.idx", "scale": "x"}, "stroke": {"field": "data.col", "scale": "color"}, "strokeWidth": {"value": 2}}}}]}], "data": [{"values": [{"val": 0.0, "col": "thornthwait", "idx": 1}, {"val": 16.684037150810678, "col": "blaney-criddle", "idx": 1}, {"val": 0.0, "col": "hargreaves", "idx": 1}, {"val": 1.769758443591955, "col": "thornthwait", "idx": 2}, {"val": 17.0559639980513, "col": "blaney-criddle", "idx": 2}, {"val": 8.407753275951427, "col": "hargreaves", "idx": 2}, {"val": 29.433939288570546, "col": "thornthwait", "idx": 3}, {"val": 32.38812668281901, "col": "blaney-criddle", "idx": 3}, {"val": 30.806970948989452, "col": "hargreaves", "idx": 3}, {"val": 49.55163706894898, "col": "thornthwait", "idx": 4}, {"val": 37.874774977039884, "col": "blaney-criddle", "idx": 4}, {"val": 38.78917310436984, "col": "hargreaves", "idx": 4}, {"val": 77.87232820842765, "col": "thornthwait", "idx": 5}, {"val": 48.66891944550993, "col": "blaney-criddle", "idx": 5}, {"val": 49.499548880022395, "col": "hargreaves", "idx": 5}, {"val": 152.80095849582932, "col": "thornthwait", "idx": 6}, {"val": 60.05711207567778, "col": "blaney-criddle", "idx": 6}, {"val": 75.82246225657182, "col": "hargreaves", "idx": 6}, {"val": 170.73885250762123, "col": "thornthwait", "idx": 7}, {"val": 65.34592639288155, "col": "blaney-criddle", "idx": 7}, {"val": 84.18606125583815, "col": "hargreaves", "idx": 7}, {"val": 144.07139878861298, "col": "thornthwait", "idx": 8}, {"val": 58.51356760734162, "col": "blaney-criddle", "idx": 8}, {"val": 78.34987766512421, "col": "hargreaves", "idx": 8}, {"val": 86.44069152916217, "col": "thornthwait", "idx": 9}, {"val": 42.925632910040676, "col": "blaney-criddle", "idx": 9}, {"val": 58.359323339938506, "col": "hargreaves", "idx": 9}, {"val": 54.25754726182929, "col": "thornthwait", "idx": 10}, {"val": 35.99074756199525, "col": "blaney-criddle", "idx": 10}, {"val": 46.806796749600885, "col": "hargreaves", "idx": 10}, {"val": 20.249110364264727, "col": "thornthwait", "idx": 11}, {"val": 24.197111086343902, "col": "blaney-criddle", "idx": 11}, {"val": 27.430723514162267, "col": "hargreaves", "idx": 11}, {"val": 0.0, "col": "thornthwait", "idx": 12}, {"val": 16.317965513811412, "col": "blaney-criddle", "idx": 12}, {"val": 0.0, "col": "hargreaves", "idx": 12}], "name": "table"}]},vega_edeb116b7e664574a2746ab62913a815);
            
            
        
    
            var circle_marker_05eaf11aa8934e6c8c4815ac4d93b74d = L.circleMarker(
                [40.44,-109.536],
                {
  "bubblingMouseEvents": true, 
  "color": "crimson", 
  "dashArray": null, 
  "dashOffset": null, 
  "fill": true, 
  "fillColor": "crimson", 
  "fillOpacity": 0.2, 
  "fillRule": "evenodd", 
  "lineCap": "round", 
  "lineJoin": "round", 
  "opacity": 1.0, 
  "radius": 10, 
  "stroke": true, 
  "weight": 3
}
                ).addTo(map_a11e733e71494a52a5a1a1025d8522bf);
            
    
            var popup_740406c0c00d46d48723636783f8baec = L.popup({maxWidth: '650'});

            
                var vega_76cdf42684dd4adfb8788665db3192ab = $('             <div id="vega_76cdf42684dd4adfb8788665db3192ab"></div>             ')[0];
                popup_740406c0c00d46d48723636783f8baec.setContent(vega_76cdf42684dd4adfb8788665db3192ab);
            

            circle_marker_05eaf11aa8934e6c8c4815ac4d93b74d.bindPopup(popup_740406c0c00d46d48723636783f8baec);

            
                
            vega_parse({"legends": [{"title": "Models", "offset": 0, "properties": {}, "fill": "color"}], "scales": [{"range": "width", "domain": {"field": "data.idx", "data": "table"}, "type": "linear", "name": "x"}, {"range": "height", "domain": {"field": "data.val", "data": "table"}, "name": "y", "nice": true}, {"range": "category20", "domain": {"field": "data.col", "data": "table"}, "type": "ordinal", "name": "color"}], "axes": [{"scale": "x", "type": "x", "title": "Month"}, {"scale": "y", "type": "y", "title": "Potential ET (mm)"}], "height": 200, "padding": "auto", "width": 400, "marks": [{"type": "group", "from": {"data": "table", "transform": [{"keys": ["data.col"], "type": "facet"}]}, "marks": [{"type": "line", "properties": {"enter": {"y": {"field": "data.val", "scale": "y"}, "x": {"field": "data.idx", "scale": "x"}, "stroke": {"field": "data.col", "scale": "color"}, "strokeWidth": {"value": 2}}}}]}], "data": [{"values": [{"val": 0.0, "col": "thornthwait", "idx": 1}, {"val": 8.233463779128794, "col": "blaney-criddle", "idx": 1}, {"val": 0.0, "col": "hargreaves", "idx": 1}, {"val": 0.0, "col": "thornthwait", "idx": 2}, {"val": 12.83024939889317, "col": "blaney-criddle", "idx": 2}, {"val": 0.0, "col": "hargreaves", "idx": 2}, {"val": 15.729786678069212, "col": "thornthwait", "idx": 3}, {"val": 26.071146454602, "col": "blaney-criddle", "idx": 3}, {"val": 16.507141548576335, "col": "hargreaves", "idx": 3}, {"val": 38.278191821158984, "col": "thornthwait", "idx": 4}, {"val": 32.40619568230963, "col": "blaney-criddle", "idx": 4}, {"val": 26.904507382479665, "col": "hargreaves", "idx": 4}, {"val": 63.58876161650062, "col": "thornthwait", "idx": 5}, {"val": 42.454127795205295, "col": "blaney-criddle", "idx": 5}, {"val": 36.94362406068651, "col": "hargreaves", "idx": 5}, {"val": 128.6671981823952, "col": "thornthwait", "idx": 6}, {"val": 54.70918380729852, "col": "blaney-criddle", "idx": 6}, {"val": 63.623366873101226, "col": "hargreaves", "idx": 6}, {"val": 140.4614912934035, "col": "thornthwait", "idx": 7}, {"val": 59.30818304695885, "col": "blaney-criddle", "idx": 7}, {"val": 70.31696766436578, "col": "hargreaves", "idx": 7}, {"val": 117.96059883197333, "col": "thornthwait", "idx": 8}, {"val": 52.617498492348155, "col": "blaney-criddle", "idx": 8}, {"val": 64.13136025392215, "col": "hargreaves", "idx": 8}, {"val": 72.50953810386342, "col": "thornthwait", "idx": 9}, {"val": 38.191261935284146, "col": "blaney-criddle", "idx": 9}, {"val": 46.161780794771886, "col": "hargreaves", "idx": 9}, {"val": 42.06930738990715, "col": "thornthwait", "idx": 10}, {"val": 30.829431813186964, "col": "blaney-criddle", "idx": 10}, {"val": 33.29586694131913, "col": "hargreaves", "idx": 10}, {"val": 11.165630220893949, "col": "thornthwait", "idx": 11}, {"val": 19.77652352398685, "col": "blaney-criddle", "idx": 11}, {"val": 14.918654617540055, "col": "hargreaves", "idx": 11}, {"val": 0.0, "col": "thornthwait", "idx": 12}, {"val": 11.861005116174647, "col": "blaney-criddle", "idx": 12}, {"val": 0.0, "col": "hargreaves", "idx": 12}], "name": "table"}]},vega_76cdf42684dd4adfb8788665db3192ab);
            
            
        
    
            var circle_marker_8bc4e919bf7f46efb8a545eff9a8d2f9 = L.circleMarker(
                [36.0719,-115.163],
                {
  "bubblingMouseEvents": true, 
  "color": "crimson", 
  "dashArray": null, 
  "dashOffset": null, 
  "fill": true, 
  "fillColor": "crimson", 
  "fillOpacity": 0.2, 
  "fillRule": "evenodd", 
  "lineCap": "round", 
  "lineJoin": "round", 
  "opacity": 1.0, 
  "radius": 10, 
  "stroke": true, 
  "weight": 3
}
                ).addTo(map_a11e733e71494a52a5a1a1025d8522bf);
            
    
            var popup_57114d3ad5914d6eab16ab9b771ea454 = L.popup({maxWidth: '650'});

            
                var vega_6b92085a0efd4ed9bc92cd1bc9252ea5 = $('             <div id="vega_6b92085a0efd4ed9bc92cd1bc9252ea5"></div>             ')[0];
                popup_57114d3ad5914d6eab16ab9b771ea454.setContent(vega_6b92085a0efd4ed9bc92cd1bc9252ea5);
            

            circle_marker_8bc4e919bf7f46efb8a545eff9a8d2f9.bindPopup(popup_57114d3ad5914d6eab16ab9b771ea454);

            
                
            vega_parse({"legends": [{"title": "Models", "offset": 0, "properties": {}, "fill": "color"}], "scales": [{"range": "width", "domain": {"field": "data.idx", "data": "table"}, "type": "linear", "name": "x"}, {"range": "height", "domain": {"field": "data.val", "data": "table"}, "name": "y", "nice": true}, {"range": "category20", "domain": {"field": "data.col", "data": "table"}, "type": "ordinal", "name": "color"}], "axes": [{"scale": "x", "type": "x", "title": "Month"}, {"scale": "y", "type": "y", "title": "Potential ET (mm)"}], "height": 200, "padding": "auto", "width": 400, "marks": [{"type": "group", "from": {"data": "table", "transform": [{"keys": ["data.col"], "type": "facet"}]}, "marks": [{"type": "line", "properties": {"enter": {"y": {"field": "data.val", "scale": "y"}, "x": {"field": "data.idx", "scale": "x"}, "stroke": {"field": "data.col", "scale": "color"}, "strokeWidth": {"value": 2}}}}]}], "data": [{"values": [{"val": 6.357363971868442, "col": "thornthwait", "idx": 1}, {"val": 25.80681522251271, "col": "blaney-criddle", "idx": 1}, {"val": 29.98349310572983, "col": "hargreaves", "idx": 1}, {"val": 20.50983189386953, "col": "thornthwait", "idx": 2}, {"val": 28.1484648208414, "col": "blaney-criddle", "idx": 2}, {"val": 40.14153150990797, "col": "hargreaves", "idx": 2}, {"val": 46.929040468464734, "col": "thornthwait", "idx": 3}, {"val": 42.28075609681927, "col": "blaney-criddle", "idx": 3}, {"val": 54.990104941731154, "col": "hargreaves", "idx": 3}, {"val": 71.16507934478079, "col": "thornthwait", "idx": 4}, {"val": 47.07193106363168, "col": "blaney-criddle", "idx": 4}, {"val": 60.51226256336476, "col": "hargreaves", "idx": 4}, {"val": 129.02517674551424, "col": "thornthwait", "idx": 5}, {"val": 60.375852554223286, "col": "blaney-criddle", "idx": 5}, {"val": 75.3090369006452, "col": "hargreaves", "idx": 5}, {"val": 323.74790997418313, "col": "thornthwait", "idx": 6}, {"val": 72.44178806560869, "col": "blaney-criddle", "idx": 6}, {"val": 106.28994002618985, "col": "hargreaves", "idx": 6}, {"val": 365.8236198686501, "col": "thornthwait", "idx": 7}, {"val": 77.86319918320918, "col": "blaney-criddle", "idx": 7}, {"val": 115.12555866476224, "col": "hargreaves", "idx": 7}, {"val": 283.7886466414705, "col": "thornthwait", "idx": 8}, {"val": 69.34588063256217, "col": "blaney-criddle", "idx": 8}, {"val": 106.4707853837107, "col": "hargreaves", "idx": 8}, {"val": 159.73977038365203, "col": "thornthwait", "idx": 9}, {"val": 52.740792247950566, "col": "blaney-criddle", "idx": 9}, {"val": 85.86745752051347, "col": "hargreaves", "idx": 9}, {"val": 89.48948652090031, "col": "thornthwait", "idx": 10}, {"val": 44.99559631523523, "col": "blaney-criddle", "idx": 10}, {"val": 72.63473087711144, "col": "hargreaves", "idx": 10}, {"val": 28.093645940474552, "col": "thornthwait", "idx": 11}, {"val": 31.012183578311028, "col": "blaney-criddle", "idx": 11}, {"val": 47.90278923873135, "col": "hargreaves", "idx": 11}, {"val": 5.968272643722221, "col": "thornthwait", "idx": 12}, {"val": 24.860472942615207, "col": "blaney-criddle", "idx": 12}, {"val": 29.709649313668255, "col": "hargreaves", "idx": 12}], "name": "table"}]},vega_6b92085a0efd4ed9bc92cd1bc9252ea5);
            
            
        
    
            var circle_marker_a058629280cc4dc7b4db7d858d370577 = L.circleMarker(
                [32.1314,-110.955],
                {
  "bubblingMouseEvents": true, 
  "color": "crimson", 
  "dashArray": null, 
  "dashOffset": null, 
  "fill": true, 
  "fillColor": "crimson", 
  "fillOpacity": 0.2, 
  "fillRule": "evenodd", 
  "lineCap": "round", 
  "lineJoin": "round", 
  "opacity": 1.0, 
  "radius": 10, 
  "stroke": true, 
  "weight": 3
}
                ).addTo(map_a11e733e71494a52a5a1a1025d8522bf);
            
    
            var popup_ab324dd05d8a4298a83d63442e346c6b = L.popup({maxWidth: '650'});

            
                var vega_c917469539ba495497ae1eb78a06ba81 = $('             <div id="vega_c917469539ba495497ae1eb78a06ba81"></div>             ')[0];
                popup_ab324dd05d8a4298a83d63442e346c6b.setContent(vega_c917469539ba495497ae1eb78a06ba81);
            

            circle_marker_a058629280cc4dc7b4db7d858d370577.bindPopup(popup_ab324dd05d8a4298a83d63442e346c6b);

            
                
            vega_parse({"legends": [{"title": "Models", "offset": 0, "properties": {}, "fill": "color"}], "scales": [{"range": "width", "domain": {"field": "data.idx", "data": "table"}, "type": "linear", "name": "x"}, {"range": "height", "domain": {"field": "data.val", "data": "table"}, "name": "y", "nice": true}, {"range": "category20", "domain": {"field": "data.col", "data": "table"}, "type": "ordinal", "name": "color"}], "axes": [{"scale": "x", "type": "x", "title": "Month"}, {"scale": "y", "type": "y", "title": "Potential ET (mm)"}], "height": 200, "padding": "auto", "width": 400, "marks": [{"type": "group", "from": {"data": "table", "transform": [{"keys": ["data.col"], "type": "facet"}]}, "marks": [{"type": "line", "properties": {"enter": {"y": {"field": "data.val", "scale": "y"}, "x": {"field": "data.idx", "scale": "x"}, "stroke": {"field": "data.col", "scale": "color"}, "strokeWidth": {"value": 2}}}}]}], "data": [{"values": [{"val": 11.521751274607285, "col": "thornthwait", "idx": 1}, {"val": 27.91945856543318, "col": "blaney-criddle", "idx": 1}, {"val": 36.09606221108435, "col": "hargreaves", "idx": 1}, {"val": 28.987402722713007, "col": "thornthwait", "idx": 2}, {"val": 29.82114351634149, "col": "blaney-criddle", "idx": 2}, {"val": 45.254035288431474, "col": "hargreaves", "idx": 2}, {"val": 51.66596152439601, "col": "thornthwait", "idx": 3}, {"val": 42.995885933975906, "col": "blaney-criddle", "idx": 3}, {"val": 56.85151355657217, "col": "hargreaves", "idx": 3}, {"val": 72.46762090798204, "col": "thornthwait", "idx": 4}, {"val": 47.19621695669373, "col": "blaney-criddle", "idx": 4}, {"val": 60.82149694907022, "col": "hargreaves", "idx": 4}, {"val": 127.80375426441891, "col": "thornthwait", "idx": 5}, {"val": 60.231322515844106, "col": "blaney-criddle", "idx": 5}, {"val": 74.97326978132534, "col": "hargreaves", "idx": 5}, {"val": 264.4829244419153, "col": "thornthwait", "idx": 6}, {"val": 69.06414915926389, "col": "blaney-criddle", "idx": 6}, {"val": 97.68188619158988, "col": "hargreaves", "idx": 6}, {"val": 291.32495758619467, "col": "thornthwait", "idx": 7}, {"val": 73.73986226404243, "col": "blaney-criddle", "idx": 7}, {"val": 104.61664097184835, "col": "hargreaves", "idx": 7}, {"val": 214.77794867950007, "col": "thornthwait", "idx": 8}, {"val": 64.95810826791588, "col": "blaney-criddle", "idx": 8}, {"val": 94.77556532810456, "col": "hargreaves", "idx": 8}, {"val": 144.7280869996132, "col": "thornthwait", "idx": 9}, {"val": 51.58606761996116, "col": "blaney-criddle", "idx": 9}, {"val": 82.47911765683664, "col": "hargreaves", "idx": 9}, {"val": 111.8707260189373, "col": "thornthwait", "idx": 10}, {"val": 47.19190088919621, "col": "blaney-criddle", "idx": 10}, {"val": 79.37104167959048, "col": "hargreaves", "idx": 10}, {"val": 37.74148266363028, "col": "thornthwait", "idx": 11}, {"val": 32.66990391419492, "col": "blaney-criddle", "idx": 11}, {"val": 53.216230588772085, "col": "hargreaves", "idx": 11}, {"val": 17.536029805878563, "col": "thornthwait", "idx": 12}, {"val": 28.94601997378224, "col": "blaney-criddle", "idx": 12}, {"val": 42.10520354345964, "col": "hargreaves", "idx": 12}], "name": "table"}]},vega_c917469539ba495497ae1eb78a06ba81);
            
            
        
    
            var circle_marker_2d145217d8754f4ea8bce5c1bb530c30 = L.circleMarker(
                [38.9408,-77.4636],
                {
  "bubblingMouseEvents": true, 
  "color": "crimson", 
  "dashArray": null, 
  "dashOffset": null, 
  "fill": true, 
  "fillColor": "crimson", 
  "fillOpacity": 0.2, 
  "fillRule": "evenodd", 
  "lineCap": "round", 
  "lineJoin": "round", 
  "opacity": 1.0, 
  "radius": 10, 
  "stroke": true, 
  "weight": 3
}
                ).addTo(map_a11e733e71494a52a5a1a1025d8522bf);
            
    
            var popup_ae3e80d9eef94879853bde8d4165a015 = L.popup({maxWidth: '650'});

            
                var vega_5e21ccecff5e4da69dc8ae014cbc1ab3 = $('             <div id="vega_5e21ccecff5e4da69dc8ae014cbc1ab3"></div>             ')[0];
                popup_ae3e80d9eef94879853bde8d4165a015.setContent(vega_5e21ccecff5e4da69dc8ae014cbc1ab3);
            

            circle_marker_2d145217d8754f4ea8bce5c1bb530c30.bindPopup(popup_ae3e80d9eef94879853bde8d4165a015);

            
                
            vega_parse({"legends": [{"title": "Models", "offset": 0, "properties": {}, "fill": "color"}], "scales": [{"range": "width", "domain": {"field": "data.idx", "data": "table"}, "type": "linear", "name": "x"}, {"range": "height", "domain": {"field": "data.val", "data": "table"}, "name": "y", "nice": true}, {"range": "category20", "domain": {"field": "data.col", "data": "table"}, "type": "ordinal", "name": "color"}], "axes": [{"scale": "x", "type": "x", "title": "Month"}, {"scale": "y", "type": "y", "title": "Potential ET (mm)"}], "height": 200, "padding": "auto", "width": 400, "marks": [{"type": "group", "from": {"data": "table", "transform": [{"keys": ["data.col"], "type": "facet"}]}, "marks": [{"type": "line", "properties": {"enter": {"y": {"field": "data.val", "scale": "y"}, "x": {"field": "data.idx", "scale": "x"}, "stroke": {"field": "data.col", "scale": "color"}, "strokeWidth": {"value": 2}}}}]}], "data": [{"values": [{"val": 0.0, "col": "thornthwait", "idx": 1}, {"val": 16.780066393670698, "col": "blaney-criddle", "idx": 1}, {"val": 0.0, "col": "hargreaves", "idx": 1}, {"val": 3.376319111721432, "col": "thornthwait", "idx": 2}, {"val": 18.024356927025043, "col": "blaney-criddle", "idx": 2}, {"val": 11.399009691557966, "col": "hargreaves", "idx": 2}, {"val": 31.83044509888618, "col": "thornthwait", "idx": 3}, {"val": 33.34163313236122, "col": "blaney-criddle", "idx": 3}, {"val": 33.01790256538511, "col": "hargreaves", "idx": 3}, {"val": 45.08617412698612, "col": "thornthwait", "idx": 4}, {"val": 37.25334551172963, "col": "blaney-criddle", "idx": 4}, {"val": 37.40271788531247, "col": "hargreaves", "idx": 4}, {"val": 80.53777632067215, "col": "thornthwait", "idx": 5}, {"val": 49.53609967578499, "col": "blaney-criddle", "idx": 5}, {"val": 51.31413777937582, "col": "hargreaves", "idx": 5}, {"val": 132.15804988406455, "col": "thornthwait", "idx": 6}, {"val": 56.96094307819506, "col": "blaney-criddle", "idx": 6}, {"val": 68.68747746984464, "col": "hargreaves", "idx": 6}, {"val": 167.7508255219447, "col": "thornthwait", "idx": 7}, {"val": 64.90414029439941, "col": "blaney-criddle", "idx": 7}, {"val": 83.14742080268572, "col": "hargreaves", "idx": 7}, {"val": 156.19530842400084, "col": "thornthwait", "idx": 8}, {"val": 60.43321801687437, "col": "blaney-criddle", "idx": 8}, {"val": 83.14742080268572, "col": "hargreaves", "idx": 8}, {"val": 108.43514719221035, "col": "thornthwait", "idx": 9}, {"val": 46.73622418240569, "col": "blaney-criddle", "idx": 9}, {"val": 68.68747746984464, "col": "hargreaves", "idx": 9}, {"val": 53.4236200889516, "col": "thornthwait", "idx": 10}, {"val": 36.100562790693296, "col": "blaney-criddle", "idx": 10}, {"val": 47.10427059797369, "col": "hargreaves", "idx": 10}, {"val": 19.592747646259873, "col": "thornthwait", "idx": 11}, {"val": 24.289206660559675, "col": "blaney-criddle", "idx": 11}, {"val": 27.69425013766576, "col": "hargreaves", "idx": 11}, {"val": 4.698614888315586, "col": "thornthwait", "idx": 12}, {"val": 19.660685812038984, "col": "blaney-criddle", "idx": 12}, {"val": 14.589424973002437, "col": "hargreaves", "idx": 12}], "name": "table"}]},vega_5e21ccecff5e4da69dc8ae014cbc1ab3);
            
            
        
    
            var circle_marker_9720acd0b3b346cbbae92a89886afe8a = L.circleMarker(
                [47.6872,-122.255],
                {
  "bubblingMouseEvents": true, 
  "color": "crimson", 
  "dashArray": null, 
  "dashOffset": null, 
  "fill": true, 
  "fillColor": "crimson", 
  "fillOpacity": 0.2, 
  "fillRule": "evenodd", 
  "lineCap": "round", 
  "lineJoin": "round", 
  "opacity": 1.0, 
  "radius": 10, 
  "stroke": true, 
  "weight": 3
}
                ).addTo(map_a11e733e71494a52a5a1a1025d8522bf);
            
    
            var popup_9b29a518b29b49a3a5b5a39f4c6ba25e = L.popup({maxWidth: '650'});

            
                var vega_7df0c0ddd4884579acacf9c93aaf2c6e = $('             <div id="vega_7df0c0ddd4884579acacf9c93aaf2c6e"></div>             ')[0];
                popup_9b29a518b29b49a3a5b5a39f4c6ba25e.setContent(vega_7df0c0ddd4884579acacf9c93aaf2c6e);
            

            circle_marker_9720acd0b3b346cbbae92a89886afe8a.bindPopup(popup_9b29a518b29b49a3a5b5a39f4c6ba25e);

            
                
            vega_parse({"legends": [{"title": "Models", "offset": 0, "properties": {}, "fill": "color"}], "scales": [{"range": "width", "domain": {"field": "data.idx", "data": "table"}, "type": "linear", "name": "x"}, {"range": "height", "domain": {"field": "data.val", "data": "table"}, "name": "y", "nice": true}, {"range": "category20", "domain": {"field": "data.col", "data": "table"}, "type": "ordinal", "name": "color"}], "axes": [{"scale": "x", "type": "x", "title": "Month"}, {"scale": "y", "type": "y", "title": "Potential ET (mm)"}], "height": 200, "padding": "auto", "width": 400, "marks": [{"type": "group", "from": {"data": "table", "transform": [{"keys": ["data.col"], "type": "facet"}]}, "marks": [{"type": "line", "properties": {"enter": {"y": {"field": "data.val", "scale": "y"}, "x": {"field": "data.idx", "scale": "x"}, "stroke": {"field": "data.col", "scale": "color"}, "strokeWidth": {"value": 2}}}}]}], "data": [{"values": [{"val": 16.738437263120925, "col": "thornthwait", "idx": 1}, {"val": 23.117996422432114, "col": "blaney-criddle", "idx": 1}, {"val": 22.41454370534511, "col": "hargreaves", "idx": 1}, {"val": 24.655696718768002, "col": "thornthwait", "idx": 2}, {"val": 23.218464455156912, "col": "blaney-criddle", "idx": 2}, {"val": 25.84796679515471, "col": "hargreaves", "idx": 2}, {"val": 35.585548267069036, "col": "thornthwait", "idx": 3}, {"val": 32.50731498901179, "col": "blaney-criddle", "idx": 3}, {"val": 31.08212686227648, "col": "hargreaves", "idx": 3}, {"val": 60.28759336251627, "col": "thornthwait", "idx": 4}, {"val": 38.74477622847424, "col": "blaney-criddle", "idx": 4}, {"val": 40.74697117108997, "col": "hargreaves", "idx": 4}, {"val": 78.72064084302887, "col": "thornthwait", "idx": 5}, {"val": 47.36814910009733, "col": "blaney-criddle", "idx": 5}, {"val": 46.806796749600885, "col": "hargreaves", "idx": 5}, {"val": 96.33901332745603, "col": "thornthwait", "idx": 6}, {"val": 49.501990493350306, "col": "blaney-criddle", "idx": 6}, {"val": 52.32121733425746, "col": "hargreaves", "idx": 6}, {"val": 111.85775148140908, "col": "thornthwait", "idx": 7}, {"val": 54.59579799648258, "col": "blaney-criddle", "idx": 7}, {"val": 59.98854856179395, "col": "hargreaves", "idx": 7}, {"val": 110.61396469508094, "col": "thornthwait", "idx": 8}, {"val": 52.06902694676737, "col": "blaney-criddle", "idx": 8}, {"val": 62.8488801807059, "col": "hargreaves", "idx": 8}, {"val": 71.93336576135273, "col": "thornthwait", "idx": 9}, {"val": 39.2305141004746, "col": "blaney-criddle", "idx": 9}, {"val": 48.77893246013361, "col": "hargreaves", "idx": 9}, {"val": 49.03125307064739, "col": "thornthwait", "idx": 10}, {"val": 33.68462775933622, "col": "blaney-criddle", "idx": 10}, {"val": 40.65808710988987, "col": "hargreaves", "idx": 10}, {"val": 32.813488985735034, "col": "thornthwait", "idx": 11}, {"val": 26.13111814487511, "col": "blaney-criddle", "idx": 11}, {"val": 33.030934371543445, "col": "hargreaves", "idx": 11}, {"val": 7.541240083604993, "col": "thornthwait", "idx": 12}, {"val": 19.75353915365642, "col": "blaney-criddle", "idx": 12}, {"val": 14.865844069040865, "col": "hargreaves", "idx": 12}], "name": "table"}]},vega_7df0c0ddd4884579acacf9c93aaf2c6e);
            
            
        
    
            var circle_marker_a94b4532d9db4f1c8b6034b58b85e363 = L.circleMarker(
                [25.8064,-80.1336],
                {
  "bubblingMouseEvents": true, 
  "color": "crimson", 
  "dashArray": null, 
  "dashOffset": null, 
  "fill": true, 
  "fillColor": "crimson", 
  "fillOpacity": 0.2, 
  "fillRule": "evenodd", 
  "lineCap": "round", 
  "lineJoin": "round", 
  "opacity": 1.0, 
  "radius": 10, 
  "stroke": true, 
  "weight": 3
}
                ).addTo(map_a11e733e71494a52a5a1a1025d8522bf);
            
    
            var popup_a9e47d2f845c4f1fa09d42620d46add3 = L.popup({maxWidth: '650'});

            
                var vega_8d90d7f8dc8b4be29c563c96d798915b = $('             <div id="vega_8d90d7f8dc8b4be29c563c96d798915b"></div>             ')[0];
                popup_a9e47d2f845c4f1fa09d42620d46add3.setContent(vega_8d90d7f8dc8b4be29c563c96d798915b);
            

            circle_marker_a94b4532d9db4f1c8b6034b58b85e363.bindPopup(popup_a9e47d2f845c4f1fa09d42620d46add3);

            
                
            vega_parse({"legends": [{"title": "Models", "offset": 0, "properties": {}, "fill": "color"}], "scales": [{"range": "width", "domain": {"field": "data.idx", "data": "table"}, "type": "linear", "name": "x"}, {"range": "height", "domain": {"field": "data.val", "data": "table"}, "name": "y", "nice": true}, {"range": "category20", "domain": {"field": "data.col", "data": "table"}, "type": "ordinal", "name": "color"}], "axes": [{"scale": "x", "type": "x", "title": "Month"}, {"scale": "y", "type": "y", "title": "Potential ET (mm)"}], "height": 200, "padding": "auto", "width": 400, "marks": [{"type": "group", "from": {"data": "table", "transform": [{"keys": ["data.col"], "type": "facet"}]}, "marks": [{"type": "line", "properties": {"enter": {"y": {"field": "data.val", "scale": "y"}, "x": {"field": "data.idx", "scale": "x"}, "stroke": {"field": "data.col", "scale": "color"}, "strokeWidth": {"value": 2}}}}]}], "data": [{"values": [{"val": 39.69976092541729, "col": "thornthwait", "idx": 1}, {"val": 35.6017979942349, "col": "blaney-criddle", "idx": 1}, {"val": 59.98854856179395, "col": "hargreaves", "idx": 1}, {"val": 39.566298545718475, "col": "thornthwait", "idx": 2}, {"val": 32.726322303262705, "col": "blaney-criddle", "idx": 2}, {"val": 54.468701783942606, "col": "hargreaves", "idx": 2}, {"val": 92.36943492569313, "col": "thornthwait", "idx": 3}, {"val": 49.07448954980738, "col": "blaney-criddle", "idx": 3}, {"val": 73.30076921707935, "col": "hargreaves", "idx": 3}, {"val": 112.5779228331876, "col": "thornthwait", "idx": 4}, {"val": 52.291938572237825, "col": "blaney-criddle", "idx": 4}, {"val": 73.85696791228948, "col": "hargreaves", "idx": 4}, {"val": 148.28143537873694, "col": "thornthwait", "idx": 5}, {"val": 62.54380312991095, "col": "blaney-criddle", "idx": 5}, {"val": 80.39596667867583, "col": "hargreaves", "idx": 5}, {"val": 195.48965407547544, "col": "thornthwait", "idx": 6}, {"val": 63.99769079974669, "col": "blaney-criddle", "idx": 6}, {"val": 85.18661294532774, "col": "hargreaves", "idx": 6}, {"val": 222.26712286272223, "col": "thornthwait", "idx": 7}, {"val": 68.43842908225663, "col": "blaney-criddle", "idx": 7}, {"val": 91.56019520681808, "col": "hargreaves", "idx": 7}, {"val": 199.97393669875856, "col": "thornthwait", "idx": 8}, {"val": 63.31269363117351, "col": "blaney-criddle", "idx": 8}, {"val": 90.49570555226732, "col": "hargreaves", "idx": 8}, {"val": 170.0489541813992, "col": "thornthwait", "idx": 9}, {"val": 53.08720963634739, "col": "blaney-criddle", "idx": 9}, {"val": 86.89169185534907, "col": "hargreaves", "idx": 9}, {"val": 126.1752259310396, "col": "thornthwait", "idx": 10}, {"val": 48.50968363357279, "col": "blaney-criddle", "idx": 10}, {"val": 83.49322041589761, "col": "hargreaves", "idx": 10}, {"val": 75.82926853584569, "col": "thornthwait", "idx": 11}, {"val": 38.10354279292547, "col": "blaney-criddle", "idx": 11}, {"val": 71.58242055696967, "col": "hargreaves", "idx": 11}, {"val": 79.22695462560152, "col": "thornthwait", "idx": 12}, {"val": 38.88132752684752, "col": "blaney-criddle", "idx": 12}, {"val": 75.64522565370162, "col": "hargreaves", "idx": 12}], "name": "table"}]},vega_8d90d7f8dc8b4be29c563c96d798915b);
            
            
        
    
            var circle_marker_a22178ffcadc436481cf3fa40156ac79 = L.circleMarker(
                [62.45,-114.383],
                {
  "bubblingMouseEvents": true, 
  "color": "crimson", 
  "dashArray": null, 
  "dashOffset": null, 
  "fill": true, 
  "fillColor": "crimson", 
  "fillOpacity": 0.2, 
  "fillRule": "evenodd", 
  "lineCap": "round", 
  "lineJoin": "round", 
  "opacity": 1.0, 
  "radius": 10, 
  "stroke": true, 
  "weight": 3
}
                ).addTo(map_a11e733e71494a52a5a1a1025d8522bf);
            
    
            var popup_29becf628b324aa4a4a083f4c1e5c743 = L.popup({maxWidth: '650'});

            
                var vega_6b8867458c994b1c939dac8afaec2ec2 = $('             <div id="vega_6b8867458c994b1c939dac8afaec2ec2"></div>             ')[0];
                popup_29becf628b324aa4a4a083f4c1e5c743.setContent(vega_6b8867458c994b1c939dac8afaec2ec2);
            

            circle_marker_a22178ffcadc436481cf3fa40156ac79.bindPopup(popup_29becf628b324aa4a4a083f4c1e5c743);

            
                
            vega_parse({"legends": [{"title": "Models", "offset": 0, "properties": {}, "fill": "color"}], "scales": [{"range": "width", "domain": {"field": "data.idx", "data": "table"}, "type": "linear", "name": "x"}, {"range": "height", "domain": {"field": "data.val", "data": "table"}, "name": "y", "nice": true}, {"range": "category20", "domain": {"field": "data.col", "data": "table"}, "type": "ordinal", "name": "color"}], "axes": [{"scale": "x", "type": "x", "title": "Month"}, {"scale": "y", "type": "y", "title": "Potential ET (mm)"}], "height": 200, "padding": "auto", "width": 400, "marks": [{"type": "group", "from": {"data": "table", "transform": [{"keys": ["data.col"], "type": "facet"}]}, "marks": [{"type": "line", "properties": {"enter": {"y": {"field": "data.val", "scale": "y"}, "x": {"field": "data.idx", "scale": "x"}, "stroke": {"field": "data.col", "scale": "color"}, "strokeWidth": {"value": 2}}}}]}], "data": [{"values": [{"val": 0.0, "col": "thornthwait", "idx": 1}, {"val": -1.56151899259339, "col": "blaney-criddle", "idx": 1}, {"val": 0.0, "col": "hargreaves", "idx": 1}, {"val": 0.0, "col": "thornthwait", "idx": 2}, {"val": -4.688859043449918, "col": "blaney-criddle", "idx": 2}, {"val": 0.0, "col": "hargreaves", "idx": 2}, {"val": 0.0, "col": "thornthwait", "idx": 3}, {"val": 4.736439646095456, "col": "blaney-criddle", "idx": 3}, {"val": 0.0, "col": "hargreaves", "idx": 3}, {"val": 0.0, "col": "thornthwait", "idx": 4}, {"val": 13.01759636462963, "col": "blaney-criddle", "idx": 4}, {"val": 0.0, "col": "hargreaves", "idx": 4}, {"val": 55.517096940924944, "col": "thornthwait", "idx": 5}, {"val": 36.38386618327985, "col": "blaney-criddle", "idx": 5}, {"val": 25.36738511650597, "col": "hargreaves", "idx": 5}, {"val": 101.2163439894127, "col": "thornthwait", "idx": 6}, {"val": 45.84288167814345, "col": "blaney-criddle", "idx": 6}, {"val": 44.722389234223826, "col": "hargreaves", "idx": 6}, {"val": 121.29948880713677, "col": "thornthwait", "idx": 7}, {"val": 52.6813915697266, "col": "blaney-criddle", "idx": 7}, {"val": 55.91885695621447, "col": "hargreaves", "idx": 7}, {"val": 98.20061640179954, "col": "thornthwait", "idx": 8}, {"val": 45.35025051340272, "col": "blaney-criddle", "idx": 8}, {"val": 47.70050682126428, "col": "hargreaves", "idx": 8}, {"val": 51.08043066868101, "col": "thornthwait", "idx": 9}, {"val": 30.223662002157294, "col": "blaney-criddle", "idx": 9}, {"val": 27.167477846090364, "col": "hargreaves", "idx": 9}, {"val": 20.175927475574174, "col": "thornthwait", "idx": 10}, {"val": 22.922735346927457, "col": "blaney-criddle", "idx": 10}, {"val": 13.753677391582112, "col": "hargreaves", "idx": 10}, {"val": 12.640035815829428, "col": "thornthwait", "idx": 11}, {"val": 18.3029943365345, "col": "blaney-criddle", "idx": 11}, {"val": 10.510550091122541, "col": "hargreaves", "idx": 11}, {"val": 0.0, "col": "thornthwait", "idx": 12}, {"val": 3.875617737075448, "col": "blaney-criddle", "idx": 12}, {"val": 0.0, "col": "hargreaves", "idx": 12}], "name": "table"}]},vega_6b8867458c994b1c939dac8afaec2ec2);
            
            
        
</script>