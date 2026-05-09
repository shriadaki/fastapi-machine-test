class ProductOut(BaseModel):
    id: int
    name: str
    price: int

    class Config:
        orm_mode = True
