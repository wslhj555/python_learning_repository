import pytest
import allure
import os
os.chdir(os.path.abspath(os.path.dirname(__file__)))
@allure.feature('User Management')
class TestUserManagement:

    @allure.story('Add User')
    
    def test_add_user(self):
        '''测试添加用户'''

        with allure.step("Step 1: Open user management page"):
            print("Opening user management page")

        with allure.step("Step 2: Fill in user details"):
            print("Filling in user details")

        with allure.step("Step 3: Submit user details"):
            print("Submitting user details")

        with allure.step("Step 4: Verify user added successfully"):
            assert True

    @allure.story('Delete User')
    def test_delete_user(self):
        '''测试删除用户'''
        with allure.step("Step 1: Open user management page"):
            print("Opening user management page")

        with allure.step("Step 2: Select user to delete"):
            print("Selecting user to delete")

        with allure.step("Step 3: Confirm deletion"):
            print("Confirming deletion")

        with allure.step("Step 4: Verify user deleted successfully"):
            assert True


if __name__ == '__main__':
    pytest.main(

        ["--alluredir", "./allure_reports_1", '-sv', "test_allure_1.py"])


# allure generate testcases/pytest_allure/allure_reports_1 -o testcases\pytest_allure\allure_html_report
