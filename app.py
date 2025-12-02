from fastapi import FastAPI, HTTPException
from sqlmodel import Session, select
from database import init_db, engine
from models import Account, Item, Purchase
from contextlib import asynccontextmanager

# ---------- APP LIFECYCLE ----------
@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(
    title="Backend Activity – Arcel Version",
    description="CRUD API for Accounts, Items, and Purchases",
    lifespan=lifespan
)

# ============================================================
# ACCOUNT CRUD OPERATIONS
# ============================================================

@app.post("/accounts/create")
def add_account(data: Account):
    with Session(engine) as session:
        session.add(data)
        session.commit()
        session.refresh(data)
        return data

@app.get("/accounts/all")
def get_accounts():
    with Session(engine) as session:
        return session.exec(select(Account)).all()

@app.get("/accounts/{acc_id}")
def get_account(acc_id: int):
    with Session(engine) as session:
        account = session.get(Account, acc_id)
        if not account:
            raise HTTPException(404, "Account does not exist.")
        return account

@app.put("/accounts/{acc_id}")
def modify_account(acc_id: int, info: Account):
    with Session(engine) as session:
        account = session.get(Account, acc_id)
        if not account:
            raise HTTPException(404, "Account does not exist.")
        account.fullname = info.fullname
        account.contact_email = info.contact_email
        session.commit()
        session.refresh(account)
        return account

@app.delete("/accounts/{acc_id}")
def remove_account(acc_id: int):
    with Session(engine) as session:
        account = session.get(Account, acc_id)
        if not account:
            raise HTTPException(404, "Account does not exist.")
        session.delete(account)
        session.commit()
        return {"status": "Account removed successfully"}

# ============================================================
# ITEM CRUD OPERATIONS
# ============================================================

@app.post("/items/add")
def add_item(item: Item):
    with Session(engine) as session:
        session.add(item)
        session.commit()
        session.refresh(item)
        return item

@app.get("/items")
def list_items():
    with Session(engine) as session:
        return session.exec(select(Item)).all()

@app.get("/items/{item_id}")
def get_item(item_id: int):
    with Session(engine) as session:
        itm = session.get(Item, item_id)
        if not itm:
            raise HTTPException(404, "Item not found.")
        return itm

@app.put("/items/{item_id}")
def modify_item(item_id: int, data: Item):
    with Session(engine) as session:
        itm = session.get(Item, item_id)
        if not itm:
            raise HTTPException(404, "Item not found.")
        itm.item_name = data.item_name
        itm.unit_price = data.unit_price
        itm.available_stock = data.available_stock
        session.commit()
        session.refresh(itm)
        return itm

@app.delete("/items/{item_id}")
def remove_item(item_id: int):
    with Session(engine) as session:
        itm = session.get(Item, item_id)
        if not itm:
            raise HTTPException(404, "Item not found.")
        session.delete(itm)
        session.commit()
        return {"status": "Item deleted"}

# ============================================================
# PURCHASE CRUD OPERATIONS
# ============================================================

@app.post("/purchases/new")
def add_purchase(p: Purchase):
    with Session(engine) as session:
        session.add(p)
        session.commit()
        session.refresh(p)
        return p

@app.get("/purchases")
def show_purchases():
    with Session(engine) as session:
        return session.exec(select(Purchase)).all()

@app.get("/purchases/{p_id}")
def get_purchase(p_id: int):
    with Session(engine) as session:
        purchase = session.get(Purchase, p_id)
        if not purchase:
            raise HTTPException(404, "Purchase not found.")
        return purchase

@app.delete("/purchases/{p_id}")
def remove_purchase(p_id: int):
    with Session(engine) as session:
        purchase = session.get(Purchase, p_id)
        if not purchase:
            raise HTTPException(404, "Purchase not found.")
        session.delete(purchase)
        session.commit()
        return {"status": "Purchase removed"}
