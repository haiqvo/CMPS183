def index():

	grid = SQLFORM.grid(db.game_play.player_id==auth.user,
		fields=[db.game_play.game_id, db.game_play.amount_bet],
		deletable=False,
		editable=False,
		details=False,
		csv=False,
		create=False,
		links = [lambda row: A('Go To Game',_href=URL("game_menu","game",args=[row.id]))]
		)
	return dict(grid=grid)
