Для установки проекта откройте консоль и введите следующие команды:

```
git clone https://github.com/p17m0/EPG_ServiceREST
```

```
python -m venv venv
```

```
source venv/Scripts/activate
```

```
pip install fastapi
```

> Чтобы запустить код воспользуйтесь командой ниже

```
uvicorn main:app --reloaduvicorn main:app --reload
```
