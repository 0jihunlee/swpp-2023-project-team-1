"""Added Timedata to PostLike Model

Revision ID: dc55c6de3e8a
Revises: 9b726a1f866e
Create Date: 2023-10-15 01:23:21.752509

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dc55c6de3e8a'
down_revision: Union[str, None] = '9b726a1f866e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
