# CapableDjangoBackend

A small Django + Django REST Framework backend to expose a simple **Todo** REST API.

This project is mainly for learning the end-to-end flow of a modern Django REST backend:
models → serializers → views → URLs → JSON responses.

---

## Tech Stack

- Python 3.x
- Django 5.x
- Django REST Framework (DRF)

---

## Project Structure (simplified)

```text
CapableDjangoBackend/
├── manage.py
├── db.sqlite3
├── todo_project/        # Django project (settings, root URLs, WSGI/ASGI)
│   ├── settings.py
│   ├── urls.py          # routes /admin/ and /api/ to the app
│   └── ...
└── todo_app/            # Django app containing the Todo API
    ├── models.py        # Todo model (title, completed, created_at)
    ├── serializers.py   # TodoSerializer (model ↔ JSON)
    ├── views.py         # TodoListCreateView, TodoRetrieveUpdateDestroyView
    └── urls.py          # /api/todos/ and /api/todos/<id>/
