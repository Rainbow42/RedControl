# Import all the models, so that Base has them before being
# imported by Alembic

from application.db.base_class import Base  # noqa
from detection.models import StatusService  # noqa
