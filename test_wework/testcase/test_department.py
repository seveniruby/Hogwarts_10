from test_wework.api.department import Department
from test_wework.utils.Utils import Utils


class TestDepartment:
    def test_list(self):
        #list json assert
        #assert depart.list(2)['ddd']=222
        department=Department()
        r=department.list("")
        assert r["errcode"] == 0
        assert r["department"][0]['name']=="霍格沃兹学院"
