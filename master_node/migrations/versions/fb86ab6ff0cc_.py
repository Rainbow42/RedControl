"""empty message

Revision ID: fb86ab6ff0cc
Revises: 
Create Date: 2022-06-11 20:10:26.734739

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = 'fb86ab6ff0cc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('configuration',
                    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('version', sa.String(length=255), nullable=False),
                    sa.Column('created_at', sa.DateTime(), nullable=True),
                    sa.Column('updated_at', sa.DateTime(), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('id')
                    )


def downgrade() -> None:
    op.drop_table('configuration')
