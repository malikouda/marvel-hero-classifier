main_html = """
<style>
    body {
        margin: 0;
        padding: 0;
        font-family: sans-serif;
        background-color: #000000;
    }
    .box {
        width: 500px;
        padding: 40px;
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background:#191919;
        text-align: center;
        color: white;
    }
    .box > ul {
        text-align: left;
        display: inline-block;
    }
    .box h1 {
        color: #e23636;
        text-transform: uppercase;
        font-weight: 500;
    }
    .box input, .box input[type=submit], .box label {
        overflow: hidden;
        border: 0;
        background: none;
        display: block;
        margin: 20px auto;
        text-align: center;
        border: 2px solid 	#518cca;
        padding: 14px 10px;
        width: 200px;
        outline: none;
        transition: 0.25s;
        color: white;
    }
    .box input[type=submit] {
        border-radius: 24px;
        border: 2px solid #f78f3f;
        color: white;
        cursor: pointer;
    }
    .box input[type=submit]:hover {
        background-color:#f78f3f
    }
    .box label:hover {
        background-color: #518cca;
    }
    .box input[type=url]:focus {
        width: 350px;
    }
    .box input[type="file"] {
        display: none;
    }
    .box label {
        cursor: pointer;
    }
</style>
<div class="box">
    <h1 class="title-text">Marvel Hero Classifier</h1>
    <p>Upload a picture of one of the following heroes:</p>
    <ul>
        <li>Spider-Man</li>
        <li>Iron Man</li>
        <li>Captain America</li>
        <li>Black Widow</li>
        <li>Thor</li>
        <li>The Hulk</li>
    </ul>
    <p>And I'll try and figure out who it is!</p>
    <form action="/upload" method="post" enctype="multipart/form-data">
        <p>Select image to upload:</p>
        <label for="upload-photo"><span id='filename'>Browse...</span></label>
        <input id="upload-photo" type="file" name="file" onchange="FileSelected()">
        <input type="submit" value="Upload Image">
    </form>
    <form action="/classify-url" method="get">
        <p>Or submit a URL:</p>
        <input type="url" name="url">
        <input type="submit" value="Fetch and analyze image">
    </form>
</div>
<script>
function FileSelected(e) {
    file = document.getElementById('upload-photo').files[document.getElementById('upload-photo').files.length - 1];
    document.getElementById('filename').innerHTML = file.name;
}
</script>
"""


def generate_response_html(predictions):
    style_html = """
        <style>
            body {
                margin: 0;
                padding: 0;
                font-family: sans-serif;
                background-color: #000000;
            }
            .box {
                width: 500px;
                padding: 40px;
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                background:#191919;
                text-align: center;
            }
            .box table {
                color: white;
                margin: auto auto;
                border-collapse: collapse;
                font-size: 1em;
                min-width: 400px;
            }
            .box table thead tr {
                background-color: #518cca;
                color: white;
                text-align: left;
            }
            .box table th, .box table td {
                padding: 12px 20px;
            }
            .box table tbody tr {
                border-bottom: 1px solid #dddddd;
            }
            .box table tbody tr:nth-of-type(even) {
                background-color: 	#504a4a;
            }
            .box table tbody tr:last-of-type {
                border-bottom: 2px solid #f78f3f;
            }
            .box table tbody tr:hover {
                font-weight: bold;
                color: 	#518cca;
            }
            .box h1 {
                color: #e23636;
                text-transform: uppercase;
                font-weight: 500;
            }
            .box .button {
                width: 150px;
                text-decoration: none;
                display: block;
                margin: 40px auto 0 auto;
                padding: 14px 10px;
                outline: none;
                transition: 0.25s;
                border-radius: 24px;
                border: 2px solid #f78f3f;
                color: white;
                cursor: pointer;
                font-weight: bold;
            }
            .box .button:hover {
                background-color:#f78f3f
            }
        </style>
    """
    table_html = "<div class='box'><table><thead><tr><th>Hero</th><th>Probability</th></tr></thead><tbody>"
    table_html += (
        "".join(
            [f"<tr><td>{str(p[0])}</td><td>{p[1]:.5f}</td></tr>" for p in predictions]
        )
        + "</tbody></table>"
        + "<a href='/' class='button'>Upload Another</a></div>"
    )

    return style_html + table_html