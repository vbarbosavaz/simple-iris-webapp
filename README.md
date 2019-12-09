# DSIA5201A

Authors:

- Vincent Barbosa Vaz
- Dhanashri Rajput
- Clea Ngouansavanh
- Elias Bouillanne

## Running the project

1. **cd** into **DSIA5201A_app**
2. Create the environment **[1]**
3. Activate the environment and install libraries **[2]**
4. Export the environment variable and run the app **[3]**

**Exit the project:**

5. Quit the application with **CTRL+C**
6. Deactivate the environment **[4]**

**[1] Create the environment**

```bash
python3 -m venv venv/
```

**[2] Activate the environment and install libraries**

```bash
. venv/bin/activate
pip install -r requirements.txt
```

Ensure that you are using the right **pip**:

```bash
which pip
```

Output should be something like : *path_to/DSIA5201A/DSIA5201A_app/venv/bin/pip*

If not:

```bash
alias pip=path_to/DSIA5201A/DSIA5201A_app/venv/bin/pip
```

Alternatively you can specify the path to the **pip** binary you want to use before any pip command:

```bash
path_to/venv/bin/pip yourcommand
```

**[3] Export the environment variable and run the app**

```bash
export FLASK_APP=DSIA5201A_app
pip install -e .
python3 -m flask run
```

**[4] Deactivate the environment**

```bash
deactivate
```

**Misc**

Output installed packages in requirements format (alternative *pip list*):

```bash
pip freeze
```

Generate a requirements file:

```bash
pip freeze > requirements.txt
```

Turn on the development features

```bash
export FLASK_ENV=development
```

## Dependencies
