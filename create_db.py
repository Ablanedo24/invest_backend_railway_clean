
from app.core.database import Base, engine
from app.models import user

Base.metadata.create_all(bind=engine)
print("Base de datos creada.")
