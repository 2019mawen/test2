import pytest

def test_1():
    """用例描述：先登录，再去执行xxx"""
    print("xxx")
@pytest.mark.repeat(5)
def test_2():
    """用例描述：先登录，再去执行yyy"""
    print("yyy")
if __name__ == '__main__':
    pytest.main(["-s","test_rep.py"])