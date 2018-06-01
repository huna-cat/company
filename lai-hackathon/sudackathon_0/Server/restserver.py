# -*- coding: utf-8 -*-
"""
Created on Thu May 31 09:59:27 2018

@author: sodekawa-mi
"""

from wsgiref import simple_server
import falcon
import resource as rsc
import pandas as pd

def initApp() :
    app = falcon.API()
    df = pd.DataFrame([["1", "4"]], columns = ["table_id", "seat_number"])
    app.add_route('/api/table', rsc.TablesResource(df))
    app.add_route('/api/us', rsc.UltraSonicResource())
    return app

def main() :
    app = initApp()
    httpd = simple_server.make_server("localhost", 80, app)
    httpd.serve_forever()

if __name__ == "__main__" :
    main()