from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Butterfly Life Cycle</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: linear-gradient(to right, #fef6e4, #ffe5ec);
                margin: 0;
                padding: 0;
                color: #333;
            }
            header {
                background-color: #ff9ebb;
                color: white;
                text-align: center;
                padding: 20px;
            }
            main {
                max-width: 800px;
                margin: 30px auto;
                background-color: #fff;
                border-radius: 12px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                padding: 30px;
            }
            h1, h2 {
                color: #d63384;
            }
            p {
                line-height: 1.6;
                text-align: justify;
            }
            footer {
                text-align: center;
                padding: 15px;
                background-color: #ff9ebb;
                color: white;
                margin-top: 40px;
            }
            img {
                display: block;
                max-width: 100%;
                border-radius: 8px;
                margin: 20px auto;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>The Butterfly and Its Life Cycle</h1>
        </header>
        <main>
            <img src="https://upload.wikimedia.org/wikipedia/commons/0/09/Lifecycle_of_a_butterfly.png" alt="Butterfly Life Cycle">
            
            <h2>About Butterflies</h2>
            <p>Butterflies are beautiful, colorful insects that belong to the order Lepidoptera. 
            They are known for their delicate wings covered in tiny scales and their important role as pollinators in the ecosystem. 
            Butterflies are found all over the world and come in thousands of species, each with unique patterns and colors.</p>

            <h2>Life Cycle of a Butterfly</h2>
            <p>The life cycle of a butterfly consists of <strong>four stages</strong>, known as complete metamorphosis:</p>

            <h3>1. Egg</h3>
            <p>The butterfly's life begins as an egg, usually laid on a leaf. These eggs are tiny and vary in shape and texture depending on the species.</p>

            <h3>2. Caterpillar (Larva)</h3>
            <p>When the egg hatches, a caterpillar emerges. This stage is focused on growth, and the caterpillar spends most of its time eating leaves. 
            It sheds its skin several times as it grows.</p>

            <h3>3. Chrysalis (Pupa)</h3>
            <p>After reaching full size, the caterpillar forms a chrysalis or pupa. Inside this case, it undergoes a remarkable transformation called metamorphosis.</p>

            <h3>4. Adult Butterfly</h3>
            <p>Finally, the adult butterfly emerges from the chrysalis. Once its wings are dry and strong enough, it begins to fly and search for nectar and mates, completing the life cycle.</p>

            <p><strong>This process shows how nature transforms a simple caterpillar into one of the most graceful creatures on Earth.</strong></p>
        </main>
        <footer>
            <p>© 2025 Butterfly Life Project | Built with Flask</p>
        </footer>
    </body>
    </html>
    """
    return render_template_string(html_content)

if __name__ == "__main__":
    app.run(debug=True)

