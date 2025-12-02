from sqlmodel import SQLModel, Field

# ---------- ACCOUNT MODEL ----------
class Account(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    fullname: str
    contact_email: str

# ---------- ITEM MODEL ----------
class Item(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    item_name: str
    unit_price: float
    available_stock: int

# ---------- PURCHASE MODEL ----------
class Purchase(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    qty: int
    amount: float
    item_ref: int | None = Field(default=None, foreign_key="item.id")
    account_ref: int | None = Field(default=None, foreign_key="account.id")
