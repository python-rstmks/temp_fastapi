"""edit question table categories relationship

Revision ID: 285566a81732
Revises: f79525630eee
Create Date: 2024-07-06 15:57:41.909660

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '285566a81732'
down_revision: Union[str, None] = 'f79525630eee'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_table('subcategory_question')
    op.drop_table('category_question')
    op.drop_table('questions')

def downgrade() -> None:
    op.create_table(
        'questions',
        sa.Column('id', sa.Integer, primary_key=True),
        # 他のカラムをここに追加します
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False, default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime, nullable=False, default=sa.func.now(), onupdate=sa.func.now())
    )
