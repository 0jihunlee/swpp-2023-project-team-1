"""Add prompt field to Image model

Revision ID: 89697afa66b5
Revises: cfc17af8302c
Create Date: 2023-10-28 17:40:32.093270

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '89697afa66b5'
down_revision: Union[str, None] = 'cfc17af8302c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('image', sa.Column('prompt', sa.TEXT(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('image', 'prompt')
    # ### end Alembic commands ###