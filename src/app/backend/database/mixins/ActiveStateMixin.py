# Soft-delete y estado de registros

from sqlalchemy import Column, Boolean, DateTime, func

# Este mixin permite:
# - Controlar si un registro está activo (campo "estado")
# - Marcar la fecha en que fue eliminado lógicamente (campo "deleted_at")

class ActiveStateMixin:
    estado = Column(Boolean, default=True, comment="Indica si el registro está activo")
    deleted_at = Column(DateTime(timezone=True), nullable=True, comment="Fecha en que fue eliminado lógicamente")


    