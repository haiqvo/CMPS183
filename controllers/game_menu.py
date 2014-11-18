# This controller will be used to display the list of open game to join

@auth.requires_login() 
def index():
	first_name = auth.user.first_name
	open_games = db(not db.game.is_over).select(db.game.ALL)
	grid = SQLFORM.grid(db.game.is_over==False,
		fields=[db.game.game_name, db.game.creator, db.game.is_over, db.game.date_started, db.game.date_ended],
		deletable=False,
		editable=False,
		details=False,
		csv=False,
		links = [lambda row: A('Join',_href=URL("game_menu","join",args=[row.id]))]
		)
	return dict(message=T('testing' + first_name), open_games=open_games, grid=grid)

@auth.requires_login() 
def join():
	form=FORM(INPUT(_type='submit', _value='Yes'))
	form.add_button('No', URL("game_menu","index"))
	if form.accepts(request, session):
		game = db.game(request.args(0,cast=int))
		player_game = db((db.game_play.player_id == auth.user)&(db.game_play.game_id == game)).select(db.game_play.ALL).first()
		if player_game is None:
			db.game_play.insert(game_id=game, player_id=auth.user, amount_bet=0, win=False)
		else:
			player_game.update(game_id=game)	
		redirect(URL("game_menu","game",args=[request.args(0,cast=int)]))
	return dict(form=form)

def game():
	game = db.game(request.args(0,cast=int)) or redirect(URL("game_menu", "index"))
	return dict(message=T('testing'), game=game)