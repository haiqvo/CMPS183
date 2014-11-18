db.define_table('game',
	Field('creator', db.auth_user),
	Field('game_name', 'string'),
	Field('gametype', 'string'),
	Field('is_over', 'boolean', represent=lambda v,r: 'Yes' if v else 'No'),
	Field('teams', 'list:string'),
	Field('date_started', 'datetime'),
	Field('date_ended', 'datetime'),
	format='%(game_name)s')

db.game.creator.requires = IS_IN_DB(db, db.auth_user.id)

db.define_table('game_play',
	Field('game_id', db.game),
	Field('player_id', db.auth_user),
	Field('amount_bet', 'integer'),
	Field('win', 'boolean'))

db.game_play.game_id.requires = IS_IN_DB(db, db.game.id)
db.game_play.player_id.requires = IS_IN_DB(db, db.auth_user.id)

db.define_table('user_status',
	Field('user_id', db.auth_user),
	Field('user_type', 'string'),
	Field('total_currency', 'integer'))
