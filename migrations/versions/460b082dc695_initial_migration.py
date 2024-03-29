"""Initial migration

Revision ID: 460b082dc695
Revises: 
Create Date: 2019-12-03 08:01:51.669623

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '460b082dc695'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blogposts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('photo_uri', sa.String(length=255), nullable=True),
    sa.Column('blog_text', sa.Text(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('blog_id', sa.Integer(), nullable=True),
    sa.Column('comment', sa.String(), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=True),
    sa.Column('email', sa.String(length=80), nullable=True),
    sa.Column('password_secure', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_table('votes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('blog_id', sa.Integer(), nullable=True),
    sa.Column('upvotes', sa.Integer(), nullable=True),
    sa.Column('downvotes', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('votes')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_table('comments')
    op.drop_table('blogposts')
    # ### end Alembic commands ###
