from datetime import datetime

from test_wework.api.department import Department
from test_wework.utils.Utils import Utils


class TestDepartment:
    department = Department()
    def setup_class(self):
        pass

    def test_list(self):
        #list json assert
        #assert depart.list(2)['ddd']=222

        r=self.department.list("")
        assert r["errcode"] == 0
        assert r["department"][0]['name']=="霍格沃兹学院"

    def test_create(self):
        now=datetime.now()
        name="子部门_"+ str(now.hour) +  str(now.second)
        r=self.department.create(name, 494, 1001)
        assert r["errcode"] == 0
        assert r["id"]!=None
        self.department.list("")
        assert self.department.jsonpath("$.department[?(@.id==%s)]" % r["id"])[0]["name"]==name
