db.define_table('game',
	Field('creator', db.auth_user),
	Field('game_name', 'string'),
	Field('gametype', 'string'),
	Field('is_over', 'boolean', represent=lambda v,r: 'Yes' if v else 'No'),
	Field('date_started', 'datetime'),
	Field('date_ended', 'datetime'))

db.define_table('game_play',
	Field('game_id', db.game),
	Field('amount_bet', 'integer'),
	Field('win', 'boolean'))

db.define_table('user_status',
	Field('user_id', db.auth_user),
	Field('user_type', 'string'),
	Field('total_currency', 'integer'))
