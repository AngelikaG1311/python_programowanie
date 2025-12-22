from magazine import Product


from Classes import Employee
def main():
    employee = Employee(
        first_name="Jan",
        last_name="Kowalski",
        hire_date="2019-01-10",
        birth_date="1999-05-12",
        city="Krakow",
        street="Grodzka 1",
        zip_code="30001",
        phone="999-777-555",
    )
    print(employee)
if __name__ == "__main__":
    main()