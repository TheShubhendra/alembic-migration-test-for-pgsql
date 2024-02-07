import os
from datetime import datetime as dt
from enum import Enum

import pytz
from sqlalchemy import (Boolean, Column, DateTime, ForeignKey, Integer,
                        MetaData, String)
from sqlalchemy.types import Enum as SQLEnum
from sqlalchemy.orm import DeclarativeBase, relationship

SCHEMA_NAME = os.environ["SCHEMA_NAME"]
# Create tz timezone object
timezone = pytz.timezone("Asia/Kolkata")


class Base(DeclarativeBase):
    metadata = MetaData(schema=SCHEMA_NAME)


class AccountStatus(Enum):
    active = "active"
    inactive = "inactive"


class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    phone_number = Column(String(15), nullable=False)
    country_code = Column(String(5), nullable=False)
    password_hash = Column(String(256), nullable=False)
    salt = Column(String(32), nullable=False)
    deleted_at = Column(DateTime)
    is_deleted = Column(Boolean, default=False)
    status = Column(
        SQLEnum(AccountStatus, inherit_schema=True), default=AccountStatus.active
    )

    students = relationship("Student", back_populates="account")


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    account_id = Column(Integer, ForeignKey("accounts.id"), nullable=False)
    first_name = Column(String(50))
    last_name = Column(String(50))
    is_deleted = Column(Boolean, default=False)
    deleted_at = Column(DateTime)

    account = relationship("Account", back_populates="students")
    logins = relationship("Login", back_populates="student")
