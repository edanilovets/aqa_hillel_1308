from pytest import mark
import platform

from lesson10.src.functions import triangle_area

def should_skip_platform():
    return platform.system().lower() == "darwin"

class TestTriangleArea:
    """Triangle area tests

    """

    @mark.area_feature
    def test_triangle_area(self):
        assert triangle_area(3, 4, 5) == 6

    @mark.regression
    @mark.smoke
    def test_triangle_area2(self):
        assert triangle_area(6, 8, 10) == 24

    # @mark.xfail(reason="QA-1234")
    @mark.skip
    def test_triangle_area3(self):
        # TODO: need to add another function
        assert triangle_area(5, 12, 13) == 30

    @mark.skipif(should_skip_platform(), reason="Skip if run on Linux")
    def test_triangle_area3(self):
        # TODO: need to add another function
        assert triangle_area(5, 12, 13) == 30
