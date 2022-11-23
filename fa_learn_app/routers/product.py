from typing import List
import uuid
from fastapi import APIRouter, Depends, Request
from fa_learn_app.dependencies import get_product_repo
from fa_learn_app.models.product import ProductIn, ProductOut
from fa_learn_app.repositories.product import BaseProductRepository


router = APIRouter()

@router.get("/products", response_model = List[ProductOut])
async def get_products(
    product_repo :BaseProductRepository = Depends(get_product_repo),
    limit :int = 100, 
    skip :int = 0
    ):
    return product_repo.get_all(limit=limit, skip=skip)

@router.get("/product", response_model = ProductOut)
async def get_product(
    id :uuid.UUID,
    product_repo :BaseProductRepository = Depends(get_product_repo),
    ):
    return product_repo.get_by_id(id)


@router.post("/product", response_model = ProductOut)
async def create_product(
    product_in :ProductIn,
    product_repo :BaseProductRepository = Depends(get_product_repo),
    ):
    return product_repo.create(product_in)