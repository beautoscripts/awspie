#!/usr/bin/env python3

from datetime import datetime
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column,String,DateTime,Integer,create_engine
import os




Base = declarative_base()
run_engine = create_engine()

class ProfileTable(Base):
    __table__ = "profile"
    id = Column(Integer(),primary_key=True)
    profile_name = Column(String(10),nullable=False,unique=True)
    aws_accesskey_id = Column(String(50),nullable=False,unique=True)
    aws_secretkey = Column(String(50),nullable=False,unique=True)
    aws_region = Column(String(10),default="us-east-1")
    date_created = Column(DateTime(),default=datetime.utcnow)
