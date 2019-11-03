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
        r=self.department.create("子部门7", 494, 1001)
        assert r["errcode"] == 0
        assert r["id"]!=None
        exist=False
        for depart in self.department.list("")["department"]:
            if depart["id"]==r["id"]:
                exist=True

        assert exist==True
