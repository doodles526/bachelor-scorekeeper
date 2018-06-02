"""birthday

Revision ID: 33104c3036c3
Revises: 
Create Date: 2018-05-31 17:46:00.827449

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33104c3036c3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contestant',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('bio', sa.Text(), nullable=True),
    sa.Column('hometown', sa.String(length=256), nullable=True),
    sa.Column('headshot_ref', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('player',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('score_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=256), nullable=False),
    sa.Column('points', sa.Integer(), nullable=False),
    sa.Column('upgrades_to_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['upgrades_to_id'], ['score_type.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('description')
    )
    op.create_table('season',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('is_bachelor', sa.Boolean(), nullable=False),
    sa.Column('lead', sa.String(length=256), nullable=True),
    sa.Column('number', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('contestant_seasons',
    sa.Column('contestant_id', sa.Integer(), nullable=False),
    sa.Column('season_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['contestant_id'], ['contestant.id'], ),
    sa.ForeignKeyConstraint(['season_id'], ['season.id'], ),
    sa.PrimaryKeyConstraint('contestant_id', 'season_id')
    )
    op.create_table('episode',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('number', sa.Integer(), nullable=False),
    sa.Column('season_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['season_id'], ['season.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('final_four_roster',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('season_id', sa.Integer(), nullable=False),
    sa.Column('player_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['player_id'], ['player.id'], ),
    sa.ForeignKeyConstraint(['season_id'], ['season.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('episode_roster',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('episode_id', sa.Integer(), nullable=False),
    sa.Column('player_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['episode_id'], ['episode.id'], ),
    sa.ForeignKeyConstraint(['player_id'], ['player.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('final_four_roster_contestants',
    sa.Column('contestant_id', sa.Integer(), nullable=False),
    sa.Column('final_four_roster_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['contestant_id'], ['contestant.id'], ),
    sa.ForeignKeyConstraint(['final_four_roster_id'], ['final_four_roster.id'], ),
    sa.PrimaryKeyConstraint('contestant_id', 'final_four_roster_id')
    )
    op.create_table('score_event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('score_type_id', sa.Integer(), nullable=False),
    sa.Column('contestant_id', sa.Integer(), nullable=False),
    sa.Column('episode_id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['contestant_id'], ['contestant.id'], ),
    sa.ForeignKeyConstraint(['episode_id'], ['episode.id'], ),
    sa.ForeignKeyConstraint(['score_type_id'], ['score_type.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('episode_roster_contestants',
    sa.Column('contestant_id', sa.Integer(), nullable=False),
    sa.Column('episode_roster_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['contestant_id'], ['contestant.id'], ),
    sa.ForeignKeyConstraint(['episode_roster_id'], ['episode_roster.id'], ),
    sa.PrimaryKeyConstraint('contestant_id', 'episode_roster_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('episode_roster_contestants')
    op.drop_table('score_event')
    op.drop_table('final_four_roster_contestants')
    op.drop_table('episode_roster')
    op.drop_table('final_four_roster')
    op.drop_table('episode')
    op.drop_table('contestant_seasons')
    op.drop_table('season')
    op.drop_table('score_type')
    op.drop_table('player')
    op.drop_table('contestant')
    # ### end Alembic commands ###
