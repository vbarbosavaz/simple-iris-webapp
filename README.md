# DSIA5201A

## Running the project

1. **cd** into **DSIA5201A_app**
2. **Create the environment and install libraries**
3. **Activate the environment**
4. **flask run**

**Exit the project**

5. Quit the application with **CTRL+C**
6. Deactivate the environment

**Create the environment and install libraries**

Ensure that you are using the right **pip**:

```bash
which -a pip
```

Output: should be something like **path_to/DSIA5201A/DSIA5201A_app/venv/bin/pip**

If not:
```bash
alias pip=path_to/DSIA5201A/DSIA5201A_app/venv/bin/pip
```

```bash
python3 -m venv venv/
pip install -r requirements.txt
```

**Activate the environment**

```bash
. venv/bin/activate
```

**Deactivate the environment**

```bash
deactivate
```

**Misc**

export FLASK_APP=DSIA5201A_app
pip install -e .

pip freeze > requirements.txt

pip freeze
