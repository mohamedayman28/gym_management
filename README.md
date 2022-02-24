# Django Gym Management

**NOTE:** The app in the development process.

Django + HTMX(Ajax library) CRUD app that covers:

* CBV(Class Based View)
* TDD(Test Driven Development) implemented for CBV.
* Implementing Ajax on HTML.
* RESTful API. **Yet to finish**
* TDD(Test Driven Development) implemented on RESTful API. **Yet to finish**

## Setting up locally

To set the site up locally, you'll need to have Python 3.6 or higher version installed on your local machine. Once that is done and ready, proceed to download the repository with the next steps.

### 1. Create development directory

```bash
mkdir gym_management
cd gym_management
```

### 2. Create virtualenv

**Note:** You may want to change the Python version, I'm also using Linux Ubuntu-based OS, so depending on your OS you may use different commands for creating a python virtual environment.

```bash
sudo apt-get install python3-pip
sudo apt-get install python3.6-venv
python3.6 -m venv env
```

### 3. Activate virtualenv

```bash
source env/bin/activate
```

### 4. Clone the repository

```bash
git init
git clone https://github.com/mohamedayman28/gym_management
```

### 5. Install required packages

```bash
cd gym_management
pip install -r requirements.txt
```

### 6. Migrate

```bash
python manage.py makemigrations
python manage.py migrate
```

If the migrations doesn't apply to all apps, you may need to migrate each app individually

```bash
python manage.py makemigrations gym
python manage.py migrate gym
```

### 7. Run the app

```bash
python manage.py runserver
```
