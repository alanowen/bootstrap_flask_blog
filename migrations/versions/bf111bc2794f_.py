"""empty message

Revision ID: bf111bc2794f
Revises: 4043cc4402bf
Create Date: 2019-01-28 23:00:02.328563

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bf111bc2794f'
down_revision = '4043cc4402bf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('private_messages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_private_messages_timestamp'), 'private_messages', ['timestamp'], unique=False)
    op.add_column('users', sa.Column('image_hash', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'image_hash')
    op.drop_index(op.f('ix_private_messages_timestamp'), table_name='private_messages')
    op.drop_table('private_messages')
    # ### end Alembic commands ###
