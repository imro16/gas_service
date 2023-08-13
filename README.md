# gas_service


```
# Gas Service

Gas Service CRM is a web application built using Django that allows customers to submit and track service requests related to gas services.

## Features

- Submit Service Requests: Customers can submit service requests online, providing details and attaching files if needed.
- Track Request Status: Customers can track the status of their service requests, including submission and resolution timestamps.

## Getting Started

Follow these steps to set up and run the Gas Service CRM application locally:

1. Clone the repository:

   ```sh
   git clone https://github.com/imro16/gas-service.git
   cd gas-service
   ```

2. Create and activate a virtual environment (optional but recommended):

   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

4. Set up the database:

   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a superuser account for admin access:

   ```sh
   python manage.py createsuperuser
   ```

6. Run the development server:

   ```sh
   python manage.py runserver
   ```

7. Access the application in your web browser at http://127.0.0.1:8000/

## Usage

- Admin Access: Access the Django admin panel at http://127.0.0.1:8000/admin/ to manage service requests and other data.
- Customer Access: Customers can submit service requests and track their status at http://127.0.0.1:8000/customer-service/.

## Contributing

Contributions are welcome! If you find a bug or have a feature suggestion, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

