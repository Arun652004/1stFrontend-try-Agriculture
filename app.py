# import matplotlib.pyplot as plt
# import turtle

# # Create a Turtle screen
# #screen = turtle.Screen()

# # Create a Turtle object
# t = turtle.Turtle()
# t.left(90)

# functionValues = [1, 3, 1, 4, 1]

# for element in functionValues:
#     if element == 1:
#         t.forward(100)
#     if element == 2:
#         t.backward(100)
#     if element == 3:
#         t.left(90)
#         t.forward(100)
#         t.right(90)
#     if element == 4:
#         t.right(90)
#         t.forward(100)
#         t.left(90)
#     if element == 5:
#         t.left(90)
#     if element == 6:
#         t.right(90)

# # Close the screen when clicked
# #screen.exitonclick()
# app.py

# app.py

from flask import Flask, render_template
import matplotlib.pyplot as plt
import base64
import io
import turtle

app = Flask(__name__)


def create_turtle_diagram():
    t = turtle.Turtle()
    #t.left(90)

    function_values = [1,1,1, 6, 1, 1,6, 1,1,1,6,1,1,6]
    #function_values = [1,4,1,3,3,2,2,4]

    for element in function_values:
        if element == 1:
            t.forward(100)
        if element == 2:
            t.backward(100)
        if element == 3:
            t.left(90)
            t.forward(100)
            t.right(90)
        if element == 4:
            t.right(90)
            t.forward(100)
            t.left(90)
        if element == 5:
            t.left(90)
        if element == 6:
            t.right(90)

    turtle.done()

@app.route('/')
def index():
    # Create a Turtle graphics diagram
    create_turtle_diagram()

    # Convert the Turtle canvas to an image
    img_data = convert_turtle_to_image()

    # Pass the image data to the HTML template
    return render_template('index.html', img_data=img_data)

def convert_turtle_to_image():
    # Convert the Turtle canvas to an image and encode it to base64
    ps = turtle.getcanvas().postscript(colormode='color')
    img = io.BytesIO()
    img.write(ps.encode('utf-8'))
    img_data = base64.b64encode(img.getvalue()).decode('utf-8')

    return img_data

if __name__ == '__main__':
    app.run(debug=True, threaded=False)
