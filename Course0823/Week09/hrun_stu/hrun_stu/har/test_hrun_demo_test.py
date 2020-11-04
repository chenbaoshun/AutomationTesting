# NOTE: Generated By HttpRunner v3.1.4
# FROM: har\test_hrun_demo.json

import pytest
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase, Parameters


class TestCaseTestHrunDemo(HttpRunner):

    @pytest.mark.parametrize("param", Parameters({"userName": ['root', 'admin', 'test']}))
    def test_start(self, param):
        super(TestCaseTestHrunDemo, self).test_start(param)

    config = Config("testcase description").variables(**{"userName": "$get_username()"})


    teststeps = [
        Step(
            RunRequest("/api/v1/admin/register")
            .post("http://127.0.0.1:6666/api/v1/admin/register")
            .with_headers(
                **{
                    "Content-Type": "application/json",
                    "User-Agent": "PostmanRuntime/7.26.8",
                    "Postman-Token": "092f4152-fbe4-4c35-b7a3-74b7f2be9907",
                }
            )
            .with_json({"userName": "$userName", "passWord": "123123"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json")
        ),
        Step(
            RunRequest("/api/v1/admin/login")
            .post("http://127.0.0.1:6666/api/v1/admin/login")
            .with_headers(
                **{
                    "Content-Type": "application/json",
                    "User-Agent": "PostmanRuntime/7.26.8",
                    "Postman-Token": "4aa023f8-6bd0-44a6-9757-59915ce486c0",
                }
            )
            .with_json({"userName": "user", "passWord": "123123"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "application/json")
        ),
    ]


if __name__ == "__main__":
    TestCaseTestHrunDemo().test_start()