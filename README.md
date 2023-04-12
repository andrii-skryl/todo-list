# todo-list

This project was created for managing any kind of your daily tasks.

Using this project you can create, update and delete two objects - tasks ang tags (like home, work, pets, shop, etc) which you can add to any task.
After you create a task, the system automatically puts the data about the date and time it was created and assigns it status as "Not done".
After you finish the task you can change its status on "Done" by pressing a green button "Complete" located right from the task.
You can put the deadline to every task if you like.

## Set up

1. Copy this repository on your PC using the next command in your IDEA terminal:

```
git clone https://github.com/andrii-skryl/todo-list
```

2. Open this project.

3. Install venv, with the next command:

```
python -m venv venv
```

4. Activate venv with following commands:

- for Windows:

```
venv/Scripts/activate
```

- for Linux or macOS:

```
source venv/bin/activate
```
4. Install dependencies from requirements.txt:

```
pip install -r requirements.txt
```

5. Create .env file in the project's root directory.
6. Write a SECRET_KEY environmental variable inside .env file (example of how it should be written you can find at ".env_sample" file) 

5. Run the server:

```
python manage.py runserver
```