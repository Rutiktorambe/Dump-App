from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    __tablename__ = 'ems_users'
    EmployeeID = db.Column(db.String(50), primary_key=True)
    Fname = db.Column(db.String(50))
    Lname = db.Column(db.String(50))
    Role = db.Column(db.String(50))
    Team = db.Column(db.String(50))
    ManagerName = db.Column(db.String(50))
    EMSlogin = db.Column(db.String(50))
    Password = db.Column(db.String(50))
    Email = db.Column(db.String(100))
    ManagerID = db.Column(db.Integer)

    def get_id(self):
        return self.EmployeeID  # Return the unique identifier for the user
    
    def is_manager(self):
        # Check if there are any employees that have the current user's EmployeeID as their ManagerID
        return User.query.filter_by(ManagerID=self.EmployeeID).count() > 0


class TimesheetEntry(db.Model):
    __tablename__ = 'timesheet_entries'
    entree_id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.String(50), db.ForeignKey('ems_users.EmployeeID'))
    fname = db.Column(db.String(50))
    lname = db.Column(db.String(50))
    team = db.Column(db.String(50))
    manager_name = db.Column(db.String(50))
    date = db.Column(db.Date)
    duration_hours = db.Column(db.Integer)
    duration_minutes = db.Column(db.Integer)
    billable_time = db.Column(db.Float)
    nonbillable_admin_time = db.Column(db.Float)
    nonbillable_training_time = db.Column(db.Float)
    unavailable_time = db.Column(db.Float)
    total_time = db.Column(db.Float)
    allocation_type = db.Column(db.String(50))
    category_1 = db.Column(db.String(50))
    category_2 = db.Column(db.String(50))
    category_3 = db.Column(db.String(50))
    comments = db.Column(db.String(255))
    entry_timestamp = db.Column(db.Float)
    project_code = db.Column(db.String(100))
