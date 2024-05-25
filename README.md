# Flight Tracking and Simulation System

## DEMO
http://65.2.33.151/map/flight/

## Presentation Link
https://docs.google.com/presentation/d/1b_sVmlZYddoggQpvpvYsnxvN7H_mWl6VAHr0RxvzuEM/edit?usp=sharing

## Description

This project is a Flight Tracking and Simulation System built using Django. The system integrates multiple components including a flight simulator, weather and GPS APIs, and a frontend map interface to provide real-time flight tracking and simulation capabilities.

## Architecture Overview

![Architecture Diagram](https://drive.google.com/file/d/1BHzaZnbEwWG4AisyXphwTjqx39eel2lh/view?usp=sharing)

The system architecture consists of the following components:

- **Backend Server (Django)**: The central server that handles API requests, processes data, and communicates with other components.
- **Database (Postgres)**: Stores flight data and other relevant information.
- **Flight Simulator**: Simulates flight data and sends updates to the backend server via webhooks.
- **APIs (Weather, GPS)**: Provides real-time weather and GPS data.
- **Frontend**: The user interface for displaying flight information.
- **Map**: Visualizes flight paths and locations.
- **Path Calculation Signal & Script**: Calculates flight paths based on current data.

## Prerequisites

Before you begin, ensure you have the following software installed:

- Python 3.x
- Django
- PostgreSQL
- Git

## Setup Instructions

### Backend Server

1. **Clone the Repository**

    ```bash
    git clone https://github.com/your-username/flight-management-system.git
    cd flight-management-system
    ```

2. **Create a Virtual Environment**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install Backend Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Setup PostgreSQL Database**

    - Install PostgreSQL if not already installed.
    - Create a new database and user.
    - Update `DATABASES` settings in `settings.py` with your database credentials.

5. **Apply Migrations**

    ```bash
    python manage.py migrate
    ```

6. **Run the Development Server**

    ```bash
    python manage.py runserver
    ```


### Path Calculation Script

1. **Configure the Path Calculation Script**

    Ensure the script is configured to trigger on flight location updates and is properly connected to the backend server.

## Usage

1. **Access the Frontend**

    Open your web browser and navigate to `http://localhost:3000` to access the frontend interface.

2. **Simulate a Flight**

    Use the flight simulator to start a flight simulation. The backend server will receive updates and process them accordingly.

3. **View Flight Path**

    The frontend map will visualize the flight path and provide real-time updates based on the data received from the backend server.

## Contributing

We welcome contributions! Please read our [Contributing Guidelines](CONTRIBUTING.md) for more information on how to get started.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

Thank you for using our Flight Tracking and Simulation System! We hope it meets your needs and provides a great experience.
