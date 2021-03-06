# NOTE: Generated By HttpRunner v3.1.4
# FROM: har\demo.json


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseDemo(HttpRunner):

    config = Config("testcase description")

    teststeps = [
        Step(
            RunRequest("/sugrec")
            .get("https://www.baidu.com/sugrec")
            .with_params(
                **{
                    "prod": "pc_his",
                    "from": "pc_web",
                    "json": "1",
                    "sid": "32810_1447_32879_31254_32706_7516_32270_32115_32846_32913",
                    "hisdata": '[{"time":1599309718,"kw":"windows升级python的命令"},{"time":1599309780,"kw":"python"},{"time":1599318199,"kw":"pip安装本地包"},{"time":1599320514,"kw":"faker"},{"time":1599320534,"kw":"python faker包"},{"time":1599320571,"kw":"python安装faker包"},{"time":1599355026,"kw":"webdriver"},{"time":1599371777,"kw":"随机姓名"},{"time":1599371793,"kw":"python随机姓"},{"time":1599383235,"kw":"谷歌webdriver"}]',
                    "_t": "1604214515348",
                    "req": "2",
                    "csor": "0",
                }
            )
            .with_headers(
                **{
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
                    "Sec-Fetch-Site": "same-origin",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Dest": "empty",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "text/plain; charset=UTF-8")
        ),
    ]


if __name__ == "__main__":
    TestCaseDemo().test_start()
