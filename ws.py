import json
import cherrypy

class MyWebService(object):

   @cherrypy.expose
   # @cherrypy.tools.json_out()
   @cherrypy.tools.json_in()
   def process(self):
    #   data = cherrypy.request.json
      output = {'points': [0, 0]}
      return json.dumps(output)

if __name__ == '__main__':
   config = {'server.socket_host': '0.0.0.0'}
   cherrypy.config.update(config)
   cherrypy.quickstart(MyWebService())