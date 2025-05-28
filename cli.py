from database import SessionLocal, engine
from models import Base, Business, Resource, Category
from utils import print_header, input_float

def initialize_database():
    Base.metadata.create_all(bind=engine)

def add_business():
    session = SessionLocal()
    name = input("Enter business name: ")
    total_budget = input_float("Enter total budget: ")
    description = input("Enter description: ")
    business = Business(name=name, total_budget=total_budget, description=description)
    session.add(business)
    session.commit()
    print("Business added!")
    session.close()

def add_resource():
    session = SessionLocal()
    businesses = session.query(Business).all()
    if not businesses:
        print("No businesses found. Add a business first.")
        session.close()
        return
    print("Businesses:")
    for b in businesses:
        print(f"{b.id}: {b.name}")
    business_id = int(input("Enter business ID: "))
    name = input("Enter resource name: ")
    budget = input_float("Enter resource budget: ")
    description = input("Enter resource description: ")
    category_name = input("Enter category (e.g., marketing, staffing): ")
    category = session.query(Category).filter_by(name=category_name).first()
    if not category:
        category = Category(name=category_name)
        session.add(category)
        session.commit()
    resource = Resource(name=name, budget=budget, description=description,
                        business_id=business_id, category_id=category.id)
    session.add(resource)
    session.commit()
    print("Resource added!")
    session.close()

def view_businesses():
    session = SessionLocal()
    businesses = session.query(Business).all()
    for b in businesses:
        print_header(f"{b.id}: {b.name}")
        print(f"Total Budget: {b.total_budget}")
        print(f"Description: {b.description}")
        for r in b.resources:
            print(f"  - {r.name} (${r.budget}) [{r.category.name}]")
    session.close()

def main_menu():
    initialize_database()
    while True:
        print_header("BizPlanner CLI")
        print("1. Add Business")
        print("2. Add Resource")
        print("3. View Businesses")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_business()
        elif choice == '2':
            add_resource()
        elif choice == '3':
            view_businesses()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
