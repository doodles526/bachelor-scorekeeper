from app import db

final_four_roster_contestants = db.Table('final_four_roster_contestants',
        db.Column('contestant_id', db.Integer, db.ForeignKey('contestant.id'), primary_key=True),
        db.Column('final_four_roster_id', db.Integer, db.ForeignKey('final_four_roster.id'), primary_key=True),
    )

episode_roster_contestants = db.Table('episode_roster_contestants',
        db.Column('contestant_id', db.Integer, db.ForeignKey('contestant.id'), primary_key=True),
        db.Column('episode_roster_id', db.Integer, db.ForeignKey('episode_roster.id'), primary_key=True),
    )

contestant_seasons = db.Table('contestant_seasons',
        db.Column('contestant_id', db.Integer, db.ForeignKey('contestant.id'), primary_key=True),
        db.Column('season_id', db.Integer, db.ForeignKey('season.id'), primary_key=True),
    )

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), unique=True, nullable=False)
    episode_rosters = db.relationship('EpisodeRoster', backref='player', lazy=True)
    final_four_rosters = db.relationship('FinalFourRoster', backref='player', lazy=True)

class EpisodeRoster(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contestants = db.relationship('Contestant', secondary=episode_roster_contestants, lazy='subquery',
            backref=db.backref('episode_rosters', lazy=True))

    episode_id = db.Column(db.Integer, db.ForeignKey('episode.id'), nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)

class FinalFourRoster(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contestants = db.relationship('Contestant', secondary=final_four_roster_contestants, lazy='subquery',
            backref=db.backref('final_four_rosters', lazy=True))

    season_id = db.Column(db.Integer, db.ForeignKey('season.id'), nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)

class Contestant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    bio = db.Column(db.Text)
    hometown = db.Column(db.String(256))
    headshot_ref = db.Column(db.String(256))

    points = db.relationship('ScoreEvent', backref='contestant', lazy=True)


    def __repr__(self):
        return 'Contestant {}'.format(self.name)

class ScoreType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(256), unique=True, nullable=False)
    points = db.Column(db.Integer, nullable=False)
    upgrades_to_id = db.Column(db.Integer, db.ForeignKey('score_type.id'))

    upgrades_to = db.relationship('ScoreType', uselist=False, backref='downgrades_to', lazy=True)

class ScoreEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    score_type_id = db.Column(db.Integer, db.ForeignKey('score_type.id'), nullable=False)
    contestant_id = db.Column(db.Integer, db.ForeignKey('contestant.id'), nullable=False)
    episode_id = db.Column(db.Integer, db.ForeignKey('episode.id'), nullable=False)

    timestamp = db.Column(db.DateTime)

    score_type = db.relationship('ScoreType', uselist=False)

class Episode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    points = db.relationship('ScoreEvent', backref='episode', lazy=True)
    number = db.Column(db.Integer, nullable=False)
    player_rosters = db.relationship('EpisodeRosters', backref='episode', lazy=True)

    season_id = db.Column(db.Integer, db.ForeignKey('season.id'), nullable=False)

class Season(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    is_bachelor = db.Column(db.Boolean, nullable=False)
    lead = db.Column(db.String(256))
    number = db.Column(db.Integer, nullable=False)
    episodes = db.relationship('Episode', backref='season', lazy=True)
    final_four_rosters = db.relationship('FinalFourRoster', backref='season', lazy=True)
    contestants = db.relationship('Contestant', secondary=contestant_seasons, lazy='subquery',
            backref=db.backref('seasons', lazy=True))

