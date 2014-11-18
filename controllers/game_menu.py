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

	return dict(message=T('testing'))