from flask import Flask, jsonify, request
import mysql.connector
import os

app = Flask(__name__)


def db():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        database=os.getenv("DB_NAME", "shopscale")
    )


# Health check endpoint
@app.get("/health")
def health():
    try:
        conn = db()
        cur = conn.cursor()

        cur.execute("SELECT 1")
        cur.fetchone()

        cur.close()
        conn.close()

        return jsonify(
            status="ok",
            db="connected"
        )

    except Exception as e:
        return jsonify(
            status="error",
            db="disconnected",
            error=str(e)
        ), 500


# Get all products
@app.get("/api/products")
def products():
    conn = db()
    cur = conn.cursor(dictionary=True)

    cur.execute("SELECT * FROM products ORDER BY id")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return jsonify(rows)


# Search products
@app.get("/api/search")
def search():
    q = request.args.get("q", "").strip()

    conn = db()
    cur = conn.cursor(dictionary=True)

    cur.execute(
        """
        SELECT * FROM products
        WHERE name LIKE %s
        OR category LIKE %s
        ORDER BY id
        """,
        (f"%{q}%", f"%{q}%")
    )

    rows = cur.fetchall()

    cur.close()
    conn.close()

    return jsonify(rows)


# Add product to cart
@app.post("/api/cart")
def add_to_cart():
    data = request.get_json(silent=True) or {}

    product_id = int(data.get("product_id", 0))
    quantity = int(data.get("quantity", 1))

    conn = db()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO carts (product_id, quantity)
        VALUES (%s, %s)
        """,
        (product_id, quantity)
    )

    conn.commit()

    cur.close()
    conn.close()

    return jsonify(
        status="added",
        product_id=product_id,
        quantity=quantity
    ), 201


# ShopScale website
@app.get("/")
def home():

    instance = os.getenv("INSTANCE_ID", "unknown")

    return f"""
<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width, initial-scale=1.0">

<title>ShopScale</title>

<style>

* {{
    box-sizing: border-box;
}}

body {{
    margin: 0;
    font-family: Arial, sans-serif;
    background: #f5f7fb;
    color: #172033;
}}

/* Navigation */

nav {{
    padding: 18px 7%;
    background: white;

    display: flex;
    justify-content: space-between;
    align-items: center;

    box-shadow: 0 2px 12px #0001;
}}

.logo {{
    font-size: 25px;
    font-weight: 800;
}}

.instance {{
    font-size: 12px;
    opacity: 0.7;
}}

/* Hero */

.hero {{
    padding: 55px 7%;

    background:
        linear-gradient(
            120deg,
            #1d4ed8,
            #7c3aed
        );

    color: white;
}}

.hero h1 {{
    font-size: 45px;
    margin: 0 0 12px;
}}

.hero p {{
    font-size: 18px;
    max-width: 650px;
}}

/* Products */

.grid {{
    padding: 35px 7%;

    display: grid;

    grid-template-columns:
        repeat(
            auto-fit,
            minmax(220px, 1fr)
        );

    gap: 20px;
}}

.card {{
    background: white;

    border-radius: 16px;

    padding: 20px;

    box-shadow:
        0 5px 20px #0001;

    transition:
        transform 0.2s,
        box-shadow 0.2s;
}}

.card:hover {{
    transform: translateY(-5px);

    box-shadow:
        0 10px 30px #0002;
}}

.product-icon {{
    font-size: 45px;
}}

.card h2 {{
    margin-bottom: 8px;
}}

.category {{
    color: #667085;
    font-size: 14px;
}}

.price {{
    font-size: 22px;
    font-weight: 800;
    margin: 12px 0;
}}

button {{
    border: 0;

    border-radius: 10px;

    padding: 11px 16px;

    background: #1d4ed8;

    color: white;

    cursor: pointer;

    font-weight: 600;
}}

button:hover {{
    background: #163fae;
}}

</style>

</head>

<body>

<nav>

    <div class="logo">
        🛒 ShopScale
    </div>

    <div class="instance">
        Serving Instance: {instance}
    </div>

</nav>


<section class="hero">

    <h1>
        Shop smarter.
    </h1>

    <p>
        A scalable shopping application
        powered by Flask, EC2, Auto Scaling,
        Application Load Balancer and RDS.
    </p>

</section>


<div id="products" class="grid">

    <p>Loading products...</p>

</div>


<script>

/*
Load products from Flask API
*/

fetch("/api/products")

    .then(response => response.json())

    .then(items => {{

        const container =
            document.getElementById("products");

        container.innerHTML =
            items.map(product => `

                <div class="card">

                    <div class="product-icon">
                        🛍️
                    </div>

                    <h2>
                        ${{product.name}}
                    </h2>

                    <div class="category">
                        ${{product.category || ""}}
                    </div>

                    <div class="price">
                        ₹${{product.price}}
                    </div>

                    <button
                        onclick="addToCart(${{product.id}})"
                    >
                        Add to cart
                    </button>

                </div>

            `).join("");

    }})

    .catch(error => {{

        document.getElementById("products").innerHTML =
            "<p>Unable to load products.</p>";

        console.error(error);

    }});


/*
Add product to cart
*/

function addToCart(id) {{

    fetch("/api/cart", {{

        method: "POST",

        headers: {{
            "Content-Type": "application/json"
        }},

        body: JSON.stringify({{
            product_id: id,
            quantity: 1
        }})

    }})

    .then(response => response.json())

    .then(data => {{

        alert("Product added to cart!");

    }})

    .catch(error => {{

        alert("Unable to add product.");

        console.error(error);

    }});

}}

</script>

</body>

</html>
"""


# Run Flask directly for local development
if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000
    )
