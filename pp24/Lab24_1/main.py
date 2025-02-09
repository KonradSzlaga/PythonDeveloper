import ShapeFactory

shapes = [

ShapeFactory.Factory.create_shape('Rectangle'),
ShapeFactory.Factory.create_shape('Triangle'),
ShapeFactory.Factory.create_shape('CIrchle'),

]


for shape in shapes:
    if shape:  # Sprawdzenie, czy obiekt został poprawnie utworzony
        print(f"Created shape: {shape.get_type()}")
    else:
        print("Shape creation failed.")