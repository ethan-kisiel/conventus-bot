"""
Contains all of the functionality for immidiate touching of the database
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from .constants import TableName

from .models import Base
from .models import Meeting
from .models import User
from .models import Note
from .models import Task


class DatabaseManager:
    """
    Manages database connection and retrieval
    """

    DATABASE_ROUTE = "sqlite:///api.db"

    def __init__(self, verbose: bool = False) -> None:
        self.engine = create_engine(self.DATABASE_ROUTE, echo=verbose)

        Base.metadata.create_all()
