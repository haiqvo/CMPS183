# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - api is an example of Hypermedia API support and access control
#########################################################################
import datetime
import random 
@auth.requires_login() 
def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    date = request.now
    bot_game = db(db.game.creator==None).count()
    print bot_game
    if bot_game == 0:
        bot()
    all_games = db(db.game.id>0).select()
    for game in all_games:
        if game.creator == None and game.is_over == False:
            if date > game.date_ended:
                game.update_record(is_over=True, winner=result())
                bot()
        if date > game.date_ended:
            game.update_record(is_over=True) 
    return dict(message=T('Hello World'))


def bot():
    current_time = request.now
    end_time = current_time + datetime.timedelta(minutes=2)
    db.game.insert(game_name="Bot Game", gametype="coin flip", is_over=False, teams=["Heads","Tails"], 
        date_started = current_time, date_ended = end_time)
    #bot_game = db(db.game.creator == None).select()[0]

def result():
    number = random.randint(0,100)
    if number % 2 == 0:
        result = "Heads"
    else:
        result = "Tails"
    return result


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_login() 
def api():
    """
    this is example of API with access control
    WEB2PY provides Hypermedia API (Collection+JSON) Experimental
    """
    from gluon.contrib.hypermedia import Collection
    rules = {
        '<tablename>': {'GET':{},'POST':{},'PUT':{},'DELETE':{}},
        }
    return Collection(db).process(request,response,rules)
