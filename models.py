from sqlalchemy import column, Integer, String, DateTime, Column
from datetime import datetime
from database import Base

class url(Base):
    __tablename__ = 'urls'
    url_id = Column(Integer, primary_key=True,index=True)
    original_url = Column(String,nullable=False)
    short_url = Column(String,unique=True,index=True)
    click_count = Column(Integer,default=0)
    created_at = Column(DateTime,default=datetime.utcnow)