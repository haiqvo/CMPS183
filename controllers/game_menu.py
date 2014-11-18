# This controller will be used to display the list of open game to join

def index():
	first_name = auth.user.first_name
	open_games = db(not db.game.is_over).select(db.game.ALL)
	grid = SQLFORM.grid(db.game.is_over==False)
	return dict(message=T('testing' + first_name), open_games=open_games, grid=grid)