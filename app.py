from flask import Flask, jsonify, request, render_template
from flask_restful import Resource ,Api
from flask.views import View
# import models for getting database models object
from models import *

# API object
api = Api(app)

#  meter list view for rendering data to index page 
class MeterList(View):

    def dispatch_request(self):
        # query all objects from meters table
        all_meter_obj = Meters.query.all()
        return render_template("index.html",objects=all_meter_obj)

# restapi class for showing json data
class MetersDetails(Resource):

    def get(self,pk):
        # get Meters data though pk 
        try:
            meters_obj = Meters_data.query.filter_by(meter_id=pk).all()
        except:
            meters_obj = None
        # create meter list 
        if meters_obj:
            meter_list = []
            for meter in meters_obj:
                meter_details = {
                        'meter_id': meter.meter_id,
                    'timestamp': meter.timestamp,
                    'value': meter.value
                }
                meter_list.append(meter_details)
            return jsonify({'data': meter_list})
        else:
            return jsonify({'data': "Records not Found"})

# url route for view and json 
app.add_url_rule("/", view_func=MeterList.as_view("meter_list"))
api.add_resource(MetersDetails,'/<int:pk>')

if __name__ == '__main__':
    # app run 
    app.run(debug = True)