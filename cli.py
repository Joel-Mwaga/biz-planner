from database import SessionLocal, engine
from models import Base, Business, Resource, Category
from utils import print_header, input_float
import csv

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

def edit_business():
    session = SessionLocal()
    businesses = session.query(Business).all()
    if not businesses:
        print("No businesses found.")
        session.close()
        return
    print("Businesses:")
    for b in businesses:
        print(f"{b.id}: {b.name}")
    business_id = int(input("Enter business ID to edit: "))
    business = session.query(Business).get(business_id)
    if not business:
        print("Business not found.")
        session.close()
        return
    business.name = input(f"Enter new name [{business.name}]: ") or business.name
    business.total_budget = input_float(f"Enter new total budget [{business.total_budget}]: ") or business.total_budget
    business.description = input(f"Enter new description [{business.description}]: ") or business.description
    session.commit()
    print("Business updated!")
    session.close()

def delete_business():
    session = SessionLocal()
    businesses = session.query(Business).all()
    if not businesses:
        print("No businesses found.")
        session.close()
        return
    print("Businesses:")
    for b in businesses:
        print(f"{b.id}: {b.name}")
    business_id = int(input("Enter business ID to delete: "))
    business = session.query(Business).get(business_id)
    if not business:
        print("Business not found.")
        session.close()
        return
    session.delete(business)
    session.commit()
    print("Business deleted!")
    session.close()

def edit_resource():
    session = SessionLocal()
    resources = session.query(Resource).all()
    if not resources:
        print("No resources found.")
        session.close()
        return
    print("Resources:")
    for r in resources:
        print(f"{r.id}: {r.name} (Business: {r.business.name})")
    resource_id = int(input("Enter resource ID to edit: "))
    resource = session.query(Resource).get(resource_id)
    if not resource:
        print("Resource not found.")
        session.close()
        return
    resource.name = input(f"Enter new name [{resource.name}]: ") or resource.name
    resource.budget = input_float(f"Enter new budget [{resource.budget}]: ") or resource.budget
    resource.description = input(f"Enter new description [{resource.description}]: ") or resource.description
    session.commit()
    print("Resource updated!")
    session.close()

def delete_resource():
    session = SessionLocal()
    resources = session.query(Resource).all()
    if not resources:
        print("No resources found.")
        session.close()
        return
    print("Resources:")
    for r in resources:
        print(f"{r.id}: {r.name} (Business: {r.business.name})")
    resource_id = int(input("Enter resource ID to delete: "))
    resource = session.query(Resource).get(resource_id)
    if not resource:
        print("Resource not found.")
        session.close()
        return
    session.delete(resource)
    session.commit()
    print("Resource deleted!")
    session.close()

def validate_budgets():
    session = SessionLocal()
    businesses = session.query(Business).all()
    for b in businesses:
        total_resource_budget = sum(r.budget for r in b.resources)
        if b.total_budget < total_resource_budget:
            print(f"Budget Error: Business '{b.name}' has total budget {b.total_budget} but resources sum to {total_resource_budget}")
    session.close()

def export_to_csv():
    session = SessionLocal()
    businesses = session.query(Business).all()
    with open('business_plan.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Business', 'Total Budget', 'Description', 'Resource', 'Resource Budget', 'Resource Description', 'Category'])
        for b in businesses:
            for r in b.resources:
                writer.writerow([
                    b.name, b.total_budget, b.description,
                    r.name, r.budget, r.description, r.category.name
                ])
    print("Exported to business_plan.csv")
    session.close()

def main_menu():
    initialize_database()
    while True:
        print_header("BizPlanner CLI")
        print("1. Add Business")
        print("2. Add Resource")
        print("3. View Businesses")
        print("4. Edit Business")
        print("5. Delete Business")
        print("6. Edit Resource")
        print("7. Delete Resource")
        print("8. Validate Budgets")
        print("9. Export Business Plan to CSV")
        print("0. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_business()
        elif choice == '2':
            add_resource()
        elif choice == '3':
            view_businesses()
        elif choice == '4':
            edit_business()
        elif choice == '5':
            delete_business()
        elif choice == '6':
            edit_resource()
        elif choice == '7':
            delete_resource()
        elif choice == '8':
            validate_budgets()
        elif choice == '9':
            export_to_csv()
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()
