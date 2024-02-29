"""
Contains the models which comprise the database schema
"""

from typing import List
from typing import Optional

from datetime import datetime

from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import ForeignKey

from sqlalchemy import String


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

user_task_association = Table(
    TableName.USER_TASK_ASSOCIATION.value,
    Base.metadata,
    Column("user_id", ForeignKey(f"{TableName.USER.value}.id"), primary_key=True),
    Column("task_id", ForeignKey(f"{TableName.TASK.value}.id"), primary_key=True),
)


class Meeting(Base):
    """
    Table for the meeting object
    """

    __tablename__ = TableName.MEETING.value

    id: Mapped[int] = mapped_column(primary_key=True)

    date: Mapped[Optional[datetime]] = mapped_column()
    is_cancelled: Mapped[bool] = mapped_column()

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

    tasks: Mapped[List["Task"]] = relationship(
        secondary=user_task_association, back_populates="users"
    )


class Note(Base):
    """
    Table for a note object
    """

    __tablename__ = TableName.NOTE.value

    id: Mapped[int] = mapped_column(primary_key=True)

    text: Mapped[str] = mapped_column()

    meeting_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey(f"{TableName.MEETING.value}.id")
    )
    meeting: Mapped[Optional["Meeting"]] = relationship(back_populates="notes")


class Task(Base):
    """
    Table for a task object
    """

    __tablename__ = TableName.TASK.value

    id: Mapped[int] = mapped_column(primary_key=True)

    text: Mapped[str] = mapped_column()
    completed_at: Mapped[Optional[datetime]] = mapped_column()
    created_at: Mapped[datetime] = mapped_column()

    feature_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey(f"{TableName.FEATURE.value}.id")
    )
    feature: Mapped[Optional["Feature"]] = relationship(back_populates="tasks")

    users: Mapped[List["User"]] = relationship(
        secondary=user_task_association, back_populates="tasks"
    )

    @property
    def is_complete(self):
        """
        Property returns true if the completed at is not a null value
        """

        return self.completed_at is not None


class Feature(Base):
    """
    Table for a feature object
    """

    __tablename__ = TableName.FEATURE.value

    id: Mapped[int] = mapped_column(primary_key=True)

    created_at: Mapped[datetime] = mapped_column()
    completed_at: Mapped[Optional[datetime]] = mapped_column()
    projected_completion: Mapped[Optional[datetime]]

    label: Mapped[str] = mapped_column(String(128))
    description: Mapped[str] = mapped_column()

    tasks: Mapped[List["Task"]] = relationship(back_populates="feature")
