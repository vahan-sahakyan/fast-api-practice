from fastapi import APIRouter, status
from fastapi.responses import Response, HTMLResponse, PlainTextResponse

router = APIRouter(
    prefix="/product",
    tags=["product"],
)

products = ["watch", "camera", "phone"]


@router.get("/all")
def get_all_products():
    data = " ".join(products)
    return Response(content=data, media_type="text/plain")


@router.get("/{id}", responses={
    200: {"content": {"text/html": {"example": "<div>Product</div>"}}, "description": "Returns the HTML for an object"},
    404: {"content": {"text/plain": {"example": "Product not available"}}, "description": "A plain text error message"},
})
def get_product(id: int):
    if id > len(products):
        out = "product not available"
        return PlainTextResponse(status_code=status.HTTP_404_NOT_FOUND, content=out, media_type="text/plain")
    else:
        product = products[id]
        out = f"""
        <head>
            <style>
            .product {{
                width: 500px;
                height: 30px;
                border: 2px inset green;
                background-color: lightblue;
                text-align: center
             }}
            </style>
        </head>
        <body>
            <div class="product">{product}</div>
        </body>
        """
        return HTMLResponse(status_code=status.HTTP_200_OK, content=out, media_type="text/html")
