from sqlalchemy import create_engine, Column, Integer, String, Text, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Form966(Base):
    __tablename__ = 'form_966'

    id = Column(Integer, primary_key=True)
    case_id = Column(Integer, index=True)  # Link to the case this form is associated with

    # --- Form Fields ---
    company_name = Column(String)
    ein = Column(String)
    address = Column(Text)
    date_incorporated = Column(Date)
    place_incorporated = Column(String)
    liquidation_type = Column(String)  # "Complete" or "Partial"
    resolution_adoption_date = Column(Date)
    last_tax_year_end_month = Column(String)
    last_tax_year_end_day = Column(Integer)
    last_tax_year_end_year = Column(Integer)
    final_tax_year_end_month = Column(String)
    final_tax_year_end_day = Column(Integer)
    final_tax_year_end_year = Column(Integer)
    common_shares_outstanding = Column(Integer)
    preferred_shares_outstanding = Column(Integer)
    amendment_dates = Column(Text)  # Consider storing as a list of dates (JSON)
    code_section = Column(String)
    previous_filing_date = Column(Date)
    consolidated_return = Column(Boolean)  # True if part of a consolidated return
    common_parent_name = Column(String)
    common_parent_ein = Column(String)
    consolidated_return_service_center = Column(String)

    # --- Metadata ---
    # You can add metadata fields as needed, such as:
    # created_at = Column(DateTime, default=datetime.utcnow)
    # updated_at = Column(DateTime, onupdate=datetime.utcnow)
    # status = Column(String, default='draft')  # 'draft', 'reviewed', 'filed'
    # review_notes = Column(Text) 

# --- Database Setup (in your main.py) ---
engine = create_engine('sqlite:///dissolution.db')  
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)