from fastapi import FastAPI, HTTPException
from typing import List
from datetime import datetime
from models import Customer

app = FastAPI(title="Customer API", version="1.0.0")

# In-memory storage
customers_db = []
customer_id_counter = 1

@app.post("/add-customer", response_model=Customer)
async def add_customer(customer: Customer):
    """Add a new customer"""
    global customer_id_counter

    if not customer.name:
        raise HTTPException(status_code=400, detail="Name is required")

    customer.id = customer_id_counter
    customer.created_at = datetime.now()
    customer_id_counter += 1

    customers_db.append(customer.dict())
    return customer


@app.get("/get-customers", response_model=List[Customer])
async def list_customers():
    """List all customers"""
    return customers_db

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
