import datetime
import random

def task_add():
    date = request.now
    bot_game = db(db.game.creator==None).count()
    print bot_game
    if bot_game == 0:
        bot()
    all_games = db(db.game.is_over != True).select()
    for game in all_games:
        if game.creator == None:
            if date > game.date_ended:
                game.update_record(is_over=True, winner=result())
                db.commit()
                bot()
        if date > game.date_ended:
            game.update_record(is_over=True) 
            db.commit()
    return "test"

def bot():
    current_time = request.now
    end_time = current_time + datetime.timedelta(minutes=2)
    db.game.insert(game_name="Bot Game", gametype="coin flip", is_over=False, teams=["Heads","Tails"], 
        date_started = current_time, date_ended = end_time)
    db.commit()
    #bot_game = db(db.game.creator == None).select()[0]

def result():
    number = random.randint(0,100)
    if number % 2 == 0:
        result = "Heads"
    else:
        result = "Tails"
    return result

from gluon.scheduler import Scheduler
scheduler = Scheduler(db,tasks=dict(demo1=task_add))
