import drawing

def test_rectangle_will_fit():
    assert drawing.rectangle_will_fit(200,200,100,50) == 2
    assert drawing.rectangle_will_fit(100,100,100,150) == 2

def test_circle_will_fit():
    assert drawing.circle_will_fit(200,200,100) == 2
    assert drawing.circle_will_fit(100,100,200) == 2

def test_triangle_will_fit():
    assert drawing.triangle_will_fit(200,200,100) == 2
    assert drawing.triangle_will_fit(100,100,200) == 2