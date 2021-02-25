from starlette.applications import Starlette
from starlette.responses import HTMLResponse, RedirectResponse
from fastai.vision import load_learner, open_image
from io import BytesIO
from pathlib import Path
import sys
import uvicorn
import aiohttp
from html_strings import main_html, generate_response_html


async def get_bytes(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.read()


app = Starlette()

model = load_learner(Path("."), "marvel-classifier.pkl")


@app.route("/upload", methods=["POST"])
async def upload(request):
    data = await request.form()
    bytes = await (data["file"].read())
    return predict_image_from_bytes(bytes)


@app.route("/classify-url", methods=["GET"])
async def classify_url(request):
    try:
        bytes = await get_bytes(request.query_params["url"])
    except aiohttp.InvalidURL:
        return RedirectResponse("/")
    return predict_image_from_bytes(bytes)


def predict_image_from_bytes(bytes):
    img = open_image(BytesIO(bytes))
    _, _, losses = model.predict(img)
    predictions = sorted(
        zip(model.data.classes, map(float, losses.tolist())),
        key=lambda p: p[1],
        reverse=True,
    )
    response_html = generate_response_html(predictions)
    return HTMLResponse(response_html)


@app.route("/")
def form(request):
    return HTMLResponse(main_html)


@app.route("/form")
def redirect_to_homepage(request):
    return RedirectResponse("/")