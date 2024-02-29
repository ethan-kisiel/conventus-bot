"""
Contains the models which comprise the database schema
"""

from typing import List
from typing import Optional

from datetime import datetime

from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import ForeignKey


from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


from .constants import TableName


class Base(DeclarativeBase):
    """Declarative base class"""

    pass


user_meeting_association = Table(
    TableName.USER_MEETING_ASSOCIATION.value,
    Base.metadata,
    Column("user_id", ForeignKey(f"{TableName.USER.value}.id"), primary_key=True),
    Column("meeting_id", ForeignKey(f"{TableName.MEETING.value}.id"), primary_key=True),
)

# user_task_association = Table()


class Meeting(Base):
    """
    Table for the meeting object
    """

    __tablename__ = TableName.MEETING.value

    id: Mapped[int] = mapped_column(primary_key=True)

    date: Mapped[datetime]

    notes: Mapped[List["Note"]] = relationship(back_populates="meeting")

    users: Mapped[List["User"]] = relationship(
        "User", secondary=user_meeting_association, back_populates="meetings"
    )  # users in attendance


class User(Base):
    """
    Table for the user object
    """

    __tablename__ = TableName.USER.value

    id: Mapped[int] = mapped_column(primary_key=True)

    meetings: Mapped[List["Meeting"]] = relationship(
        secondary=user_meeting_association, back_populates="users"
    )  # meetings this user has attended


class Note(Base):
    """
    Table for a note object
    """

    __tablename__ = TableName.NOTE.value

    id: Mapped[int] = mapped_column(primary_key=True)

    meeting_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey(f"{TableName.MEETING.value}.id")
    )
    meeting: Mapped[Optional["Meeting"]] = relationship(back_populates="notes")


# class Task(Base):
#     pass


# class Feature(Base):
#     pass
