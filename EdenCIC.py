#from DatabaseModels import PIXEL,ORB
from google.appengine.api import users
from google.appengine.api import channel
from google.appengine.ext import ndb

import json
import webapp2
#import EdenDataOfficer as edo
#import EdenUniCon as euc
#import ProxyModels as prox
from EdenModels import *
import EdenWishes as wish


#import datetime
#import time
import json
#import random

#cXUSE =  users.get_current_user() #External ID = Google ID
#cpix = prox.cPixel()

def jsonify(data):
    if isinstance(data, str):
        return json.dumps(data)
    else:
        try:
            return json.dumps(data.to_dict())
        except AttributeError:
            try:
                return json.dumps(data.__dict__)
            except:
                pass


class aSession(webapp2.RequestHandler):
    def get(self):
        sesh = wish.aSession()
        self.response.out.write(jsonify(sesh))

class Eden(webapp2.RequestHandler):
    def get(self):
        source = ndb.Key('Crystal','1').get()
        if source:
            pass
        else:
            source = Crystal(id='1', name='Eden Source Crystal',info='The Tree of Wisdom.',uCount=0,oCount=0, evekey='adam')
            source.put()
        self.response.out.write(jsonify(source))

#class Immigration(webapp2.RequestHandler):
#    def get(self):
#        if cXUSE:   self.Customs()
#        else:       self.xLogin()
#    def xLogin(self):
#        self.redirect(users.create_login_url("/"))
#    def Customs(self):
#        cPIXEL = edo.lPIXEL()
#        #cORB = lORB()
#        if cPIXEL:
#            #cpix.data = cPIXEL.to_dict()
#            self.response.out.write(edo.jsonify(cpix))
#            #self.response.write('test')
##            pulse = PULSE.get()
##            pulse.content = 'stuff'
##            pulse.console = 'it worked'
##            pulse.send('system')
##            self.response.out.write(edo.dictsonify(cMUSE))
#        else:
#            pixel = euc.aPIXEL()
#            self.response.out.write(edo.jsonify(pixel))

        
app = webapp2.WSGIApplication([
#                               ('/cic/newSession', NewSession),
#                               ('/cic/incTutorial', IncrementTutorial),
#                               ('/cic/asession', aSession),
                               ('/cic/asession', aSession),
                               ('/cic/eden', Eden),
#                               ('/cic/jsonwish', JSONWish),
#                               ('/cic/pulse', PULSE),
                               ],
                              debug=True) 